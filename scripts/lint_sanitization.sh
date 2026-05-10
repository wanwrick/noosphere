#!/usr/bin/env bash
# lint_sanitization.sh — sanitization gate for Noosphere Practice OS.
#
# Scans the working tree for any banned token before allowing a commit / merge.
# Returns 0 if clean; non-zero (and a human-readable report) if any banned token
# is found. Wired into .pre-commit-config.yaml and .github/workflows/sanitization.yml.
#
# The banned-token lexicon is a first-class invariant of the repository.
# See _Logs/sanitization-audit.md for the audit trail and §0 of the Practice OS
# plan for the rationale.

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

if ! command -v rg >/dev/null 2>&1; then
  echo "ERROR: ripgrep (rg) is required. Install with: brew install ripgrep / apt install ripgrep"
  exit 2
fi

# ---------------------------------------------------------------------------
# Banned-token lexicon — case-insensitive, word-boundary aware where useful.
# Each line is one ripgrep -e pattern. Edit with care; every change should
# be logged in _Logs/sanitization-audit.md with the rationale.
# ---------------------------------------------------------------------------

PATTERNS=(
  # Employer / team
  '\bQuestrade\b'
  '\bQFG\b'
  '\bQuestBank\b'
  '\bQuest Bank\b'
  '\bQuest Financial Group\b'
  '\bDataWizards\b'
  '\bData Wizards\b'
  '\bQTG\b'
  '\bQuest Tech Group\b'

  # Internal vendors / systems
  '\bTemenos\b'
  '\bProspector\b'
  '\bPortfolioPlus\b'
  '\bIntellify\b'
  '\bCorpBI\b'
  '\bWestway\b'

  # External vendors when paired with internal context
  '\bMartech Force\b'

  # JIRA / ticket codes (project-specific)
  '\bQB-[0-9]+\b'

  # Internal incident figures
  '\$[0-9]+K?\s+(incident|cost spike|disruption)'

  # Dated meeting attributions (event-stamped quotes from Notion)
  '\bJan 21, 2026\b.*(meeting|invoked)'
  '\bMar 12, 2026\b.*(stated|quote)'
  '\bMar 19, 2026\b.*incident'

  # Internal team-size attributions
  '\b40-45\b.*\bFTE\b'
  '\b15-20 to bank\b'

  # Cross-Hub callouts (Notion-internal markers)
  'Cross-Hub:'

  # Stakeholder full names — banned in any context (the safest rule)
  '\bAdam Muise\b'
  '\bMark Huang\b'
  '\bKriti Sood\b'
  '\bDan Cici\b'
  '\bGabriel Cortes\b'
  '\bYelena Hakhumyan\b'
  '\bHayk Danielyan\b'
  '\bMariano Barrionuevo\b'
  '\bArtur Gyulambaryan\b'

  # Internal Databricks workspace / project / cluster IDs
  '\bdbc-[a-f0-9]{8}-[a-f0-9]{4}\b'      # Databricks workspace ID pattern
  'workspaceId\s*[:=]\s*["'"'"']?[0-9]{16,}["'"'"']?'
  'clusterId\s*[:=]\s*["'"'"']?[0-9]{4}-[0-9]{6}-[a-z0-9]{8}["'"'"']?'
)

# Excluded paths — false positives belong here (e.g., the lint script itself
# and the sanitizer legitimately mention banned tokens as regex patterns).
EXCLUDES=(
  '--glob' '!.git/**'
  '--glob' '!_Diagrams/**.png'
  '--glob' '!scripts/lint_sanitization.sh'
  '--glob' '!scripts/sanitize_from_notion.py'
  '--glob' '!_Logs/sanitization-audit.md'
  '--glob' '!Workflows/sanitization-pass.md'
  '--glob' '!.gitleaks.toml'
  '--glob' '!.pre-commit-config.yaml'
  '--glob' '!.github/workflows/sanitization.yml'
)

FAIL=0
echo "Sanitization lint over: $REPO_ROOT"
echo

for pat in "${PATTERNS[@]}"; do
  if rg -i -n --color=never "${EXCLUDES[@]}" -e "$pat" .; then
    echo "  ↑ matched banned pattern: $pat"
    echo
    FAIL=1
  fi
done

if [[ $FAIL -eq 0 ]]; then
  echo "Sanitization OK — 0 banned tokens detected."
  exit 0
else
  echo
  echo "FAIL: banned tokens present. Resolve before commit / merge."
  echo "       See _Logs/sanitization-audit.md for the audit trail and"
  echo "       Workflows/sanitization-pass.md for the remediation procedure."
  exit 1
fi
