#!/usr/bin/env bash
# lint_sanitization.sh — sanitization gate for Noosphere Practice OS.
#
# Scans the working tree for any banned token before allowing a commit / merge.
# Returns 0 if clean; non-zero (and a human-readable report) if any banned token
# is found. Wired into .pre-commit-config.yaml and .github/workflows/sanitization.yml.
#
# THE LEXICON IS NOT STORED IN THIS REPOSITORY.
#   The banned-token lexicon enumerates the employer / team / vendor /
#   stakeholder proper nouns it exists to protect. Committing it to a public
#   repo publishes exactly what it is meant to hide. So it loads at runtime
#   from a gitignored file. See .sanitization-lexicon.example for the format
#   and _Logs/sanitization-audit.md for the audit trail.

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

REQUIRE_REAL_LEXICON=0
FILES_ONLY=0
for arg in "$@"; do
  case "$arg" in
    --require-real-lexicon) REQUIRE_REAL_LEXICON=1 ;;
    --files-only|--ci) FILES_ONLY=1 ;;
    -h|--help)
      sed -n '2,15p' "$0" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    *) echo "Unknown argument: $arg" >&2; exit 2 ;;
  esac
done

if ! command -v rg >/dev/null 2>&1; then
  echo "ERROR: ripgrep (rg) is required. Install with: brew install ripgrep / apt install ripgrep"
  exit 2
fi

# ---------------------------------------------------------------------------
# Resolve the lexicon. First match wins.
# ---------------------------------------------------------------------------
EXAMPLE_LEXICON=".sanitization-lexicon.example"
LOCAL_LEXICON=".sanitization-lexicon.local"
USING_PLACEHOLDERS=0

if [[ -n "${NOOSPHERE_LEXICON:-}" ]]; then
  LEXICON="$NOOSPHERE_LEXICON"
  if [[ ! -f "$LEXICON" ]]; then
    echo "ERROR: NOOSPHERE_LEXICON points at a missing file: $LEXICON" >&2
    exit 2
  fi
elif [[ -f "$LOCAL_LEXICON" ]]; then
  LEXICON="$LOCAL_LEXICON"
elif [[ -f "$EXAMPLE_LEXICON" ]]; then
  LEXICON="$EXAMPLE_LEXICON"
  USING_PLACEHOLDERS=1
else
  echo "ERROR: no lexicon found. Expected one of:" >&2
  echo "         \$NOOSPHERE_LEXICON, $LOCAL_LEXICON, $EXAMPLE_LEXICON" >&2
  exit 2
fi

# ---------------------------------------------------------------------------
# Excluded paths. The lexicon files are the ONLY legitimate holders of banned
# tokens, so they are the only exclusions. Every other file is scanned —
# previous versions excluded the tooling itself, which is precisely how the
# lexicon stayed unnoticed inside tracked files.
# ---------------------------------------------------------------------------
EXCLUDES=(
  '--glob' '!.git/**'
  '--glob' '!*.png'
  '--glob' "!$EXAMPLE_LEXICON"
  '--glob' "!$LOCAL_LEXICON"
)
[[ -n "${NOOSPHERE_LEXICON:-}" ]] && EXCLUDES+=('--glob' "!$NOOSPHERE_LEXICON")

echo "Sanitization lint over: $REPO_ROOT"
echo "Lexicon:                $LEXICON"
echo

if [[ $USING_PLACEHOLDERS -eq 1 ]]; then
  echo "=============================================================="
  echo " WARNING: running with PLACEHOLDER terms — YOU ARE NOT PROTECTED."
  echo " The example lexicon contains fake names only. To protect real"
  echo " content:   cp $EXAMPLE_LEXICON $LOCAL_LEXICON"
  echo " then replace the placeholders with your real terms."
  echo "=============================================================="
  echo
  if [[ $REQUIRE_REAL_LEXICON -eq 1 ]]; then
    echo "FAIL: --require-real-lexicon was passed but only placeholders are available."
    exit 3
  fi
fi

# ---------------------------------------------------------------------------
# Scan, one rule per lexicon line.
# ---------------------------------------------------------------------------
FAIL=0
RULES=0

while IFS=$'\t' read -r category flags pattern replacement canary || [[ -n "${category:-}" ]]; do
  # Skip comments, blanks, and malformed lines.
  [[ -z "${category// }" ]] && continue
  case "$category" in \#*) continue ;; esac
  if [[ -z "${pattern:-}" ]]; then
    echo "WARN: skipping malformed lexicon line (need 4 tab-separated fields): $category" >&2
    continue
  fi

  RULES=$((RULES + 1))
  RG_FLAGS=()
  [[ "$flags" == *i* ]] && RG_FLAGS+=('-i')

  # Canary check. A regex typo (a doubled backslash, an unbalanced group) is
  # still a valid regex — it just matches nothing, so the gate reports "clean"
  # while protecting nothing. That silent failure is indistinguishable from
  # success, so a rule that cannot match its own canary is a hard error.
  if [[ -n "${canary:-}" ]]; then
    if ! printf '%s' "$canary" | rg -q "${RG_FLAGS[@]}" -e "$pattern"; then
      echo "ERROR: lexicon rule [$category] does not match its own canary." >&2
      echo "       This rule would match nothing and the gate would report a" >&2
      echo "       false pass. Check for doubled backslashes." >&2
      exit 2
    fi
  fi

  if [[ $FILES_ONLY -eq 1 ]]; then
    # Print offending FILE PATHS only. Never the pattern, never the matched
    # line: this repo is public, so its CI logs are public, and echoing either
    # would republish the banned token the lint exists to suppress.
    if hits="$(rg -l --color=never "${RG_FLAGS[@]}" "${EXCLUDES[@]}" -e "$pattern" . 2>/dev/null)"; then
      echo "  banned pattern [$category] matched in:"
      printf '    %s\n' $hits
      echo
      FAIL=1
    fi
  else
    if rg -n --color=never "${RG_FLAGS[@]}" "${EXCLUDES[@]}" -e "$pattern" .; then
      echo "  ^ matched banned pattern [$category]: $pattern"
      echo
      FAIL=1
    fi
  fi
done < "$LEXICON"

if [[ $RULES -eq 0 ]]; then
  echo "ERROR: lexicon $LEXICON contained no usable rules." >&2
  exit 2
fi

echo "Rules applied: $RULES"

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
