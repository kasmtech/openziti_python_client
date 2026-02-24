"""Minimal provisioning example: input admin identity JSON -> output identity_new JSON."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from typing import TypedDict
from uuid import uuid4

import openziti_edge_client
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from openziti_edge_client.api.enroll_api import EnrollApi
from openziti_edge_client.models.enrollment_certs import EnrollmentCerts
from openziti_edge_client.models.enrollment_certs_envelope import (
    EnrollmentCertsEnvelope,
)
from openziti_edge_client.models.ott_enrollment_request import OttEnrollmentRequest
from openziti_edge_management.api.enrollment_api import EnrollmentApi
from openziti_edge_management.api.identity_api import IdentityApi
from openziti_edge_management.models.create_envelope import CreateEnvelope
from openziti_edge_management.models.enrollment_create import EnrollmentCreate
from openziti_edge_management.models.enrollment_detail import EnrollmentDetail
from openziti_edge_management.models.detail_enrollment_envelope import (
    DetailEnrollmentEnvelope,
)
from openziti_edge_management.models.identity_create import IdentityCreate
from openziti_edge_management.models.identity_type import IdentityType
from openziti_kasm_client import ZitiClient


class IdentityInput(TypedDict):
    ca: str


class AdminIdentityInput(TypedDict):
    ztAPI: str
    id: IdentityInput


def _create_key_and_csr(common_name: str) -> tuple[str, str]:
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    csr = (
        x509.CertificateSigningRequestBuilder()
        .subject_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, common_name)]))
        .sign(private_key, hashes.SHA256())
    )

    key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode("utf-8")
    csr_pem = csr.public_bytes(serialization.Encoding.PEM).decode("utf-8")
    return key_pem, csr_pem


def provision_identity(admin_identity: AdminIdentityInput):
    identity_name = f"identity_new_{uuid4().hex[:8]}"

    zt_api = admin_identity["ztAPI"]
    ca_pem = admin_identity["id"]["ca"].removeprefix("pem:")

    with ZitiClient(identity_json=dict(admin_identity), mgmt_api=True) as admin_client:
        identity_api = IdentityApi(admin_client.api_client)
        identity_response: CreateEnvelope = identity_api.create_identity(
            IdentityCreate(name=identity_name, isAdmin=False, type=IdentityType.DEFAULT)
        )
        identity_location = identity_response.data
        assert identity_location is not None
        identity_id = str(identity_location.id)

        enrollment_api = EnrollmentApi(admin_client.api_client)
        enrollment_response: CreateEnvelope = enrollment_api.create_enrollment(
            EnrollmentCreate(
                identityId=identity_id,
                method="ott",
                expiresAt=datetime.now(timezone.utc) + timedelta(minutes=30),
            )
        )
        enrollment_location = enrollment_response.data
        assert enrollment_location is not None
        enrollment_id = str(enrollment_location.id)

        enrollment_detail_response: DetailEnrollmentEnvelope = (
            enrollment_api.detail_enrollment(enrollment_id)
        )
        enrollment_detail: EnrollmentDetail = enrollment_detail_response.data
        ott_token = enrollment_detail.token

    key_pem, csr_pem = _create_key_and_csr(identity_name)

    enroll_configuration = openziti_edge_client.Configuration(
        host=zt_api, ca_cert_data=ca_pem
    )
    with openziti_edge_client.ApiClient(enroll_configuration) as enroll_client:
        enrollment_certs_response: EnrollmentCertsEnvelope = EnrollApi(
            enroll_client
        ).enroll_ott(
            OttEnrollmentRequest(clientCsr=csr_pem, token=ott_token),
        )
        certs = enrollment_certs_response.data
        assert certs is not None

    response_ca = certs.ca or ca_pem
    response_cert = certs.cert

    identity_new_json = {
        "ztAPI": zt_api,
        "ztAPIs": None,
        "configTypes": None,
        "id": {
            "ca": f"pem:{response_ca}",
            "cert": f"pem:{response_cert}",
            "key": f"pem:{key_pem}",
        },
        "enableHa": False,
    }
    return identity_new_json


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Provision identity_new from an admin identity JSON"
    )
    parser.add_argument("admin_identity_json", help="Admin identity JSON content")
    args = parser.parse_args()

    admin_identity: AdminIdentityInput = json.loads(args.admin_identity_json)
    identity_json = provision_identity(admin_identity)
    print(json.dumps(identity_json, indent=2))


if __name__ == "__main__":
    main()
