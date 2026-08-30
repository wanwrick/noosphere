#!/usr/bin/env bash
# verify_all.sh — run all 10 verification checks. Non-zero exit on
# any FAIL. Used by CI and by the weekly-practice-synthesis ritual.
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel)"
export ROOT

CHECKS=(
  "01_token_budget.sh"
  "02_routing.sh"
  "03_skill_invocation.sh"
  "04_dabs_end_to_end.sh"
  "05_attribution_lint.sh"
  "06_governance_gate.py"
  "07_ip_coverage.py"
  "08_sanitization_audit.sh"
  "09_diagram_coverage.sh"
  "10_pii_scan.py"
)

PASS=0; FAIL=0; SKIP=0
echo "================================"
echo "Noosphere v1.2.0 verification"
echo "================================"
for c in "${CHECKS[@]}"; do
  echo ""
  echo "--- $c ---"
  if [[ "$c" == *.py ]]; then
    if python3 "$ROOT/scripts/verify/$c"; then
      PASS=$((PASS+1))
    else
      rc=$?
      if [ "$rc" -eq 0 ]; then PASS=$((PASS+1)); else FAIL=$((FAIL+1)); fi
    fi
  else
    if bash "$ROOT/scripts/verify/$c"; then
      PASS=$((PASS+1))
    else
      FAIL=$((FAIL+1))
    fi
  fi
done

echo ""
echo "================================"
echo "Result: $PASS pass · $FAIL fail"
echo "================================"
[ "$FAIL" -eq 0 ]
