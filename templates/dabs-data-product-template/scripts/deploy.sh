#!/usr/bin/env bash
# Deploy the bundle to a target environment.
# Usage: bash scripts/deploy.sh <target>     # target: dev|staging|prod

set -euo pipefail

cd "$(dirname "$0")/.."

TARGET="${1:-dev}"
echo "Deploying to: $TARGET"

bash scripts/validate_bundle.sh

databricks bundle validate --target "$TARGET"
databricks bundle deploy --target "$TARGET"

echo "Deployed bundle to $TARGET. Run pipeline with:"
echo "  databricks bundle run data_product_pipeline --target $TARGET"
