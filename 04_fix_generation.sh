#!/usr/bin/env bash
set -euo pipefail

# ---------------------------------------------------------------------------
# 04_fix_generation.sh
#
# Post-generation patches for models that the OpenAPI Generator emits
# incorrectly.
#
# Currently fixes:
#   - Tags model: the OpenAPI spec defines Tags as a free-form object
#     (additionalProperties: true, no fixed properties). The generator
#     produces a Pydantic model that forbids extra fields.
# ---------------------------------------------------------------------------

PACKAGES_ROOT="packages"
CLIENT_DIRS=(
    "${PACKAGES_ROOT}/openziti_edge_client"
    "${PACKAGES_ROOT}/openziti_edge_management"
)

echo "[1/1] Patching free-form / additionalProperties models (Tags)..."

for CLIENT_DIR in "${CLIENT_DIRS[@]}"; do
    NAME="$(basename "${CLIENT_DIR}")"

    # Find every model whose __properties list is empty — these are the
    # free-form dict/map models the generator gets wrong.
    #
    # Currently this is only Tags, but the fix is safe for any such model.
    find "${CLIENT_DIR}/${NAME}/models" -name '*.py' -print0 | while IFS= read -r -d '' MODEL_FILE; do

        # Quick check: does this file contain the empty-properties marker?
        if ! grep -qP '__properties:\s*ClassVar\[List\[str\]\]\s*=\s*\[\]' "${MODEL_FILE}"; then
            continue
        fi

        BASENAME="$(basename "${MODEL_FILE}")"
        echo "  Patching ${NAME}/models/${BASENAME}"

        CLIENT_DIR="${CLIENT_DIR}" NAME="${NAME}" MODEL_FILE="${MODEL_FILE}" python3 - <<'PY'
import os, pathlib, re

model_file = pathlib.Path(os.environ["MODEL_FILE"])
txt = model_file.read_text(encoding="utf-8")
orig = txt

# ---------------------------------------------------------------
# 1. Add extra="allow" to model_config so Pydantic accepts and
#    stores arbitrary key/value pairs.  Skip if already present.
# ---------------------------------------------------------------
if 'extra="allow"' not in txt and "extra='allow'" not in txt:
    txt = re.sub(
        r'(model_config\s*=\s*ConfigDict\()',
        r'\1\n        extra="allow",',
        txt,
        count=1,
    )

# ---------------------------------------------------------------
# 2. Fix from_dict() — replace the empty model_validate({}) call
#    with one that passes through the entire input dict.
#
#    Before:  _obj = cls.model_validate({
#             })
#    After:   _obj = cls.model_validate(obj)
# ---------------------------------------------------------------
txt = re.sub(
    r'_obj\s*=\s*cls\.model_validate\(\{\s*\}\)',
    '_obj = cls.model_validate(obj)',
    txt,
    count=1,
)

if txt != orig:
    model_file.write_text(txt, encoding="utf-8")
    print(f"    ✓ patched")
else:
    print(f"    – already patched or no changes needed")
PY

    done
done

echo "Done."
