import json
import logging
import tempfile
import threading
from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Union

import openziti_edge_management
from openziti_edge_management.api.authentication_api import AuthenticationApi
from openziti_edge_management.models.authenticate import Authenticate

logger = logging.getLogger(__name__)


class SessionData:
    """Represents an OpenZiti API session."""

    def __init__(
        self, token: str, expires_at: datetime, identity_id: Optional[str] = None
    ):
        """
        Initialize session data.

        Args:
            token: The session token
            expires_at: When the session expires (should be timezone-aware datetime)
            identity_id: Optional identity ID associated with the session
        """
        self.token = token
        self.expires_at = expires_at
        self.identity_id = identity_id

    def is_expired(self, buffer_seconds: int = 60) -> bool:
        """
        Check if the session is expired or will expire soon.

        Args:
            buffer_seconds: Consider session expired if it expires within this many seconds

        Returns:
            True if the session is expired or will expire within buffer_seconds
        """
        now = datetime.now(timezone.utc)
        expires_at = self.expires_at
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        return now >= (expires_at - timedelta(seconds=buffer_seconds))

    def to_dict(self) -> Dict[str, Any]:
        """Convert session data to a dictionary for serialization."""
        return {
            "token": self.token,
            "expires_at": self.expires_at.isoformat(),
            "identity_id": self.identity_id,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SessionData":
        """Create SessionData from a dictionary."""
        expires_at = datetime.fromisoformat(data["expires_at"])
        return cls(
            token=data["token"],
            expires_at=expires_at,
            identity_id=data.get("identity_id"),
        )


class SessionStorage(ABC):
    """Abstract base class for session storage backends."""

    @abstractmethod
    def save_session(self, session: SessionData) -> None:
        """Save the session data."""
        raise NotImplementedError

    @abstractmethod
    def load_session(self) -> Optional[SessionData]:
        """Load the session data. Returns None if no valid session exists."""
        raise NotImplementedError

    @abstractmethod
    def clear_session(self) -> None:
        """Clear/delete the stored session."""
        raise NotImplementedError


class InMemorySessionStorage(SessionStorage):
    """In-memory session storage. Session is lost when the process ends."""

    def __init__(self):
        self._session: Optional[SessionData] = None
        self._lock = threading.Lock()

    def save_session(self, session: SessionData) -> None:
        with self._lock:
            self._session = session

    def load_session(self) -> Optional[SessionData]:
        with self._lock:
            return self._session

    def clear_session(self) -> None:
        with self._lock:
            self._session = None


class FileSessionStorage(SessionStorage):
    """File-based session storage. Useful for single-node persistence."""

    def __init__(self, file_path: Union[str, Path]):
        """
        Initialize file-based session storage.

        Args:
            file_path: Path to the file where session data will be stored
        """
        self.file_path = Path(file_path)
        self._lock = threading.Lock()

    def save_session(self, session: SessionData) -> None:
        with self._lock:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.file_path, "w", encoding="utf-8") as file_pointer:
                json.dump(session.to_dict(), file_pointer)

    def load_session(self) -> Optional[SessionData]:
        with self._lock:
            if not self.file_path.exists():
                return None
            try:
                with open(self.file_path, "r", encoding="utf-8") as file_pointer:
                    data = json.load(file_pointer)
                return SessionData.from_dict(data)
            except (json.JSONDecodeError, KeyError, ValueError) as exc:
                return None

    def clear_session(self) -> None:
        with self._lock:
            if self.file_path.exists():
                self.file_path.unlink()


class ZitiClient:
    def __init__(
        self,
        host: Optional[str] = None,
        cert_file: Optional[str] = None,
        key_file: Optional[str] = None,
        ca_cert: Optional[str] = None,
        identity_json: Optional[Dict[str, Any]] = None,
        identity_json_path: Optional[str] = None,
        session_storage: Optional[SessionStorage] = None,
        refresh_buffer_seconds: int = 300,
        auth_method: str = "cert",
        auto_refresh: bool = True,
        mgmt_api: bool = True,
    ):
        """
        Initialize the Ziti client.

        Args:
            host: The OpenZiti API host URL - will be read from identity_json if provided
            cert_file: Path to client certificate file (PEM format)
            key_file: Path to client key file (PEM format)
            ca_cert: Path to CA certificate file or PEM data as string
            identity_json: Identity JSON dict with 'id' containing 'ca', 'cert', 'key' (alternative to files)
            identity_json_path: Path to identity JSON file (alternative to cert_file/key_file)
            session_storage: Custom session storage backend (defaults to InMemorySessionStorage)
            refresh_buffer_seconds: Refresh session this many seconds before expiry (default: 300 = 5 minutes)
            auth_method: Authentication method (default: "cert")
            auto_refresh: Automatically refresh session before expiry (default: True)
            mgmt_api: Automatically connect to management endpoint (default: True)
        """
        self.mgmt_api = mgmt_api
        self.host = host
        self.refresh_buffer_seconds = refresh_buffer_seconds
        self.auth_method = auth_method
        self.auto_refresh = auto_refresh

        if self.refresh_buffer_seconds < 0:
            raise ValueError("refresh_buffer_seconds must be >= 0")

        self._session_storage = session_storage or InMemorySessionStorage()
        self._session_lock = threading.RLock()
        self._refresh_timer: Optional[threading.Timer] = None

        self._temp_files: list[str] = []
        self._cert_file = None
        self._key_file = None
        self._ca_cert = None

        if identity_json_path:
            with open(identity_json_path, "r", encoding="utf-8") as file_pointer:
                identity_json = json.load(file_pointer)

        if identity_json:
            self._setup_from_identity_json(identity_json)
        else:
            self._cert_file = cert_file
            self._key_file = key_file
            self._ca_cert = ca_cert

        self._validate_configuration()

        self._configuration: Any = None
        self._api_client: Any = None
        self._init_configuration()

    def _create_temp_pem_file(self, pem_data: str, suffix: str) -> str:
        temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=suffix)
        temp_file.write(pem_data)
        temp_file.close()
        self._temp_files.append(temp_file.name)
        return temp_file.name

    def _setup_from_identity_json(self, identity_json: Dict[str, Any]) -> None:
        """Setup certificates from identity JSON."""
        zt_api = identity_json.get("ztAPI")
        if self.host is None:
            if not zt_api:
                raise ValueError(
                    "identity_json must include 'ztAPI' when host is not provided"
                )
            self.host = (
                zt_api.replace("/client/", "/management/") if self.mgmt_api else zt_api
            )

        id_data = identity_json.get("id")
        if not isinstance(id_data, dict):
            raise ValueError("identity_json must include an 'id' object")

        ca_pem = id_data.get("ca", "").removeprefix("pem:")
        cert_pem = id_data.get("cert", "").removeprefix("pem:")
        key_pem = id_data.get("key", "").removeprefix("pem:")

        if ca_pem:
            self._ca_cert = self._create_temp_pem_file(ca_pem, ".ca.pem")
        if cert_pem:
            self._cert_file = self._create_temp_pem_file(cert_pem, ".cert.pem")
        if key_pem:
            self._key_file = self._create_temp_pem_file(key_pem, ".key.pem")

    def _validate_configuration(self) -> None:
        if not self.host:
            raise ValueError(
                "host must be provided either directly or via identity_json"
            )
        if not self._cert_file or not self._key_file:
            raise ValueError("both cert_file and key_file are required")

    def _init_configuration(self) -> None:
        config_args: Dict[str, Any] = {
            "host": self.host,
            "cert_file": self._cert_file,
            "key_file": self._key_file,
        }

        if self._ca_cert:
            if "-----BEGIN" in self._ca_cert:
                self._ca_cert = self._create_temp_pem_file(self._ca_cert, ".ca.pem")
            config_args["ssl_ca_cert"] = self._ca_cert

        self._configuration = openziti_edge_management.Configuration(**config_args)
        self._api_client = openziti_edge_management.ApiClient(self._configuration)

    def _authenticate(self) -> SessionData:
        """
        Perform authentication and return session data.

        Returns:
            SessionData object with token and expiry

        Raises:
            Exception if authentication fails
        """
        auth_api = AuthenticationApi(self._api_client)
        auth = Authenticate()
        response = auth_api.authenticate(method=self.auth_method, auth=auth)

        token = response.data.token
        expires_at = response.data.expires_at
        identity_id = getattr(response.data, "identity_id", None)

        # Ensure expires_at is a datetime object
        if isinstance(expires_at, str):
            expires_at = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        elif expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)

        return SessionData(token=token, expires_at=expires_at, identity_id=identity_id)

    def _get_valid_session(self) -> SessionData:
        """
        Get a valid session, refreshing if necessary.

        Returns:
            Valid SessionData object
        """
        with self._session_lock:
            session = self._session_storage.load_session()
            if session and not session.is_expired(self.refresh_buffer_seconds):
                return session

            session = self._authenticate()
            self._session_storage.save_session(session)
            self._configuration.api_key["ztSession"] = session.token

            if self.auto_refresh:
                self._schedule_refresh(session)

            return session

    def _schedule_refresh(self, session: SessionData) -> None:
        """Schedule automatic session refresh before expiry."""
        if self._refresh_timer:
            self._refresh_timer.cancel()

        now = datetime.now(timezone.utc)
        expires_at = session.expires_at
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)

        refresh_time = expires_at - timedelta(seconds=self.refresh_buffer_seconds)
        delay = (refresh_time - now).total_seconds()

        if delay > 0:
            self._refresh_timer = threading.Timer(delay, self._background_refresh)
            self._refresh_timer.daemon = True
            self._refresh_timer.start()

    def _background_refresh(self) -> None:
        """Background thread function to refresh the session."""
        try:
            self._get_valid_session()
        except Exception as exc:
            logger.error("Background session refresh failed: %s", exc)

    @property
    def api_client(self) -> Any:
        """
        Get the configured API client with a valid session.

        This property ensures the session is valid before returning the API client.
        """
        session = self._get_valid_session()
        self._configuration.api_key["ztSession"] = session.token
        return self._api_client

    @property
    def session(self) -> Optional[SessionData]:
        """Get the current session data (may be None or expired)."""
        return self._session_storage.load_session()

    def refresh_session(self) -> SessionData:
        """
        Manually refresh the session.

        Returns:
            New SessionData object
        """
        with self._session_lock:
            session = self._authenticate()
            self._session_storage.save_session(session)
            self._configuration.api_key["ztSession"] = session.token
            if self.auto_refresh:
                self._schedule_refresh(session)
            return session

    def close(self) -> None:
        """Clean up resources."""
        if self._refresh_timer:
            self._refresh_timer.cancel()
            self._refresh_timer = None

        if self._api_client:
            try:
                self._api_client.rest_client.pool_manager.clear()
            except Exception as exc:
                logger.info("Failed to cleanup rest client pool: %s", exc)

        for temp_file in self._temp_files:
            try:
                Path(temp_file).unlink(missing_ok=True)
            except Exception as exc:
                logger.warning("Failed to delete temporary file %s: %s", temp_file, exc)

    def __enter__(self) -> "ZitiClient":
        """Context manager entry."""
        self._get_valid_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.close()

    def __del__(self) -> None:
        """Destructor to ensure cleanup."""
        try:
            self.close()
        except Exception:
            pass
