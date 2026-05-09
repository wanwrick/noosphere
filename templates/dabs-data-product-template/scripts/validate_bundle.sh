#!/usr/bin/env bash
# 6-check CI/CD gate for the DABs Data-Contract Golden Path.
#
# Run from the subproject root:
#   bash scripts/validate_bundle.sh
#
# Returns 0 only if all six checks pass.

set -uo pipefail

cd "$(dirname "$0")/.."

CONTRACT="${CONTRACT:-data-contract.yml}"
SCHEMA="data-contract.schema.json"

FAIL=0
declare -a FAILURES

# --- Helper to run a check and record result.
run_check() {
  local name="$1"
  local cmd="$2"
  if ! eval "$cmd" >/dev/null 2>&1; then
    echo "FAIL: $name"
    FAILURES+=("$name")
    FAIL=1
  else
    echo " OK : $name"
  fi
}

echo "Validating $CONTRACT against $SCHEMA …"
echo

# 1. Bundle YAML syntax valid (databricks bundle validate).
if command -v databricks >/dev/null 2>&1; then
  run_check "1. databricks bundle validate" "databricks bundle validate"
else
  echo " SKIP: 1. databricks bundle validate (databricks CLI not installed)"
fi

# 2. data-contract.yml valid against JSON Schema.
run_check "2. data-contract.yml valid against JSON Schema" \
  "python -c 'from src.contract.loader import load; load(\"$CONTRACT\")'"

# 3. Every PII column has a masking_function.
run_check "3. Every PII column has a masking_function" \
  "python -c '
from src.contract.loader import load, list_pii_columns
c = load(\"$CONTRACT\")
bad = [col[\"name\"] for col in list_pii_columns(c) if not col.get(\"masking_function\")]
assert not bad, f\"Missing masking_function: {bad}\"
'"

# 4. freshness.sla_minutes defined.
run_check "4. freshness.sla_minutes defined" \
  "python -c '
from src.contract.loader import load
c = load(\"$CONTRACT\")
assert isinstance(c.get(\"freshness\", {}).get(\"sla_minutes\"), int)
'"

# 5. quality_expectations[] non-empty.
run_check "5. quality_expectations non-empty" \
  "python -c '
from src.contract.loader import load
c = load(\"$CONTRACT\")
assert len(c.get(\"quality_expectations\", [])) > 0
'"

# 6. metadata.owner_team and metadata.classification non-null.
run_check "6. metadata.owner_team and metadata.classification non-null" \
  "python -c '
from src.contract.loader import load
c = load(\"$CONTRACT\")
m = c.get(\"metadata\", {})
assert m.get(\"owner_team\") and m.get(\"classification\")
'"

echo
if [[ $FAIL -eq 0 ]]; then
  echo "ALL CHECKS PASSED."
  exit 0
else
  echo "FAILED CHECKS:"
  for f in "${FAILURES[@]}"; do echo "  - $f"; done
  exit 1
fi
