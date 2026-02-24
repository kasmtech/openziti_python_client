#!/usr/bin/env bash
set -euo pipefail

mkdir -p packages
rm -rf packages/openziti_edge_client packages/openziti_edge_management

echo "Generating openziti_edge_client from client.yml..."
docker run --rm -v "./swagger:/swagger" -v "./packages:/packages" openapitools/openapi-generator-cli generate \
    -i /swagger/client.yml \
    -g python \
    --additional-properties packageName=openziti_edge_client \
    -o /packages/openziti_edge_client

echo "Generating openziti_edge_management from management.yml..."
docker run --rm -v "./swagger:/swagger" -v "./packages:/packages" openapitools/openapi-generator-cli generate \
    -i /swagger/management.yml \
    -g python \
    --additional-properties packageName=openziti_edge_management \
    -o /packages/openziti_edge_management

sudo chown -R $(id -u):$(id -g) ./packages
