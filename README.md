# openziti_python_client

This repository generates the OpenZiti `openziti_edge_client` and `openziti_edge_management` clients for Kasm ZTNA support. It is responsible for:

- Generating the modules
- Vendoring certain dependencies

Additionally this repository contains the `openziti_kasm_client`. It is developed in-house and is responsible for managing sessions.

## Getting started

For other Kasm repositories using these modules:

```
pip install "openziti-edge-client@git+https://github.com/kasmtech/openziti_python_client.git@develop#subdirectory=packages/openziti_edge_client"
pip install "openziti-edge-management@git+https://github.com/kasmtech/openziti_python_client.git@develop#subdirectory=packages/openziti_edge_management"
pip install "openziti-kasm-client@git+https://github.com/kasmtech/openziti_python_client.git@develop#subdirectory=packages/openziti_kasm_client"
```

For local development and testing:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e packages/openziti_edge_client
python -m pip install -e packages/openziti_edge_management
python -m pip install -e packages/openziti_kasm_client --no-deps
```

Example:

```bash
source .venv/bin/activate
pip install cryptography
python example/provision_identity2.py '<identity.json>'
```

## Common Routes

“Admin / control-plane / management” client generated from management.yml

- Create identity: POST /identities
- Create an outstanding enrollment (OTT/OTTCA/UPDB): POST /enrollments

“Enrollment / data-plane bootstrap / client” client generated from client.yml

- Enroll with an OTT token: POST /enroll/ott

## Generating

- (Optional) The client is generated from the Swagger OpenAPI. To update the Swagger schema run `01_update.sh`
- [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) with the [Python Generator](https://openapi-generator.tech/docs/generators/python/) is used to generate the Python modules. Run `02_generate.sh`
- The `urllib3` version used in the generated code differs from the version used in the Kasm API/Manager. To allow for this client we vendor in conflicting dependencies. Run `03_vendor.sh`
