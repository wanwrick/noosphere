#!/usr/bin/env bash
# verify/08_sanitization_audit.sh — wraps the master sanitization linter.
set -euo pipefail
ROOT="${ROOT:-$(git rev-parse --show-toplevel)}"
bash "$ROOT/scripts/lint_sanitization.sh"
