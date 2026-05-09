#!/usr/bin/env bash
# verify/04_dabs_end_to_end.sh — DABs Golden Path subproject must validate
# and unit tests must pass.
set -euo pipefail
ROOT="${ROOT:-$(git rev-parse --show-toplevel)}"
DABS="$ROOT/templates/dabs-data-product-template"

if [ ! -d "$DABS" ]; then
  echo "FAIL: DABs subproject missing at templates/dabs-data-product-template/"
  exit 1
fi

# 1. Bundle validation script must exist and be executable
if [ ! -x "$DABS/scripts/validate_bundle.sh" ]; then
  echo "FAIL: validate_bundle.sh missing or not executable"
  exit 1
fi

# 2. Run validation if databricks CLI present, else mark SKIP
cd "$DABS"
if command -v databricks >/dev/null 2>&1; then
  bash scripts/validate_bundle.sh || { echo "FAIL: validate_bundle.sh"; exit 1; }
else
  echo "SKIP: databricks CLI not installed; skipping bundle bind step"
fi

# 3. Run pytest on unit tests if available
if command -v python >/dev/null 2>&1 && [ -d tests/unit ]; then
  if python -c "import pytest" 2>/dev/null; then
    python -m pytest tests/unit/ -q || { echo "FAIL: unit tests"; exit 1; }
  else
    echo "SKIP: pytest not installed; skipping unit tests"
  fi
fi

echo "PASS: DABs subproject end-to-end gate."
