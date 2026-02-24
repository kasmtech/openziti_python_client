#!/usr/bin/env bash
set -euo pipefail

# Save Swagger files to swagger directory
mkdir -p swagger
curl -o swagger/management.yml https://raw.githubusercontent.com/openziti/edge-api/refs/heads/main/management.yml
curl -o swagger/client.yml https://raw.githubusercontent.com/openziti/edge-api/refs/heads/main/client.yml
