# Workflow -- Sanitization Pass

**Purpose:** Step-by-step procedure for refreshing IP from Notion into the repo without leaking employer / team / stakeholder / JIRA / vendor / Databricks-internal references.

**When to run:** Any time you pull content from Notion (or any private source) into a file under `ip/`, `playbooks/`, `templates/`, `Workflows/`, or `decisions/`.

**Prerequisites:**
- `ripgrep` installed (the `rg` binary).
- `python3` available.
- `pre-commit install` already run in your local clone (so commit-time gates fire).

---

## Procedure

### Step 1 -- Pull raw content
Use the Notion MCP `notion-fetch` tool with the source page ID. Save the raw markdown locally outside the repo (e.g., `~/scratch/raw-<id>.md`). **Do not** paste raw content into a tracked file before sanitization.

### Step 2 -- Run the sanitizer
```
python scripts/sanitize_from_notion.py \
    --source ~/scratch/raw-<id>.md \
    --target ip/authored/<file>.md \
    --source-id <notion-page-id> \
    --reviewer "<your name>" \
    --diff-out ~/scratch/diff-<id>.txt \
    --audit
```

The script applies the banned-token lexicon, writes a sanitized draft to the target path, emits a unified diff for review, and appends an entry to `_Logs/sanitization-audit.md`.

### Step 3 -- Human review (mandatory)
Open the diff (`~/scratch/diff-<id>.txt`). For every replacement, confirm the substitution is correct. If a banned token survived sanitization, **stop**: update the rules in `scripts/sanitize_from_notion.py` and `scripts/lint_sanitization.sh`, re-run, and re-review.

Human review is the load-bearing step; the script is a force-multiplier, not a guarantee.

### Step 4 -- Run the linters
```
bash scripts/lint_sanitization.sh
gitleaks detect --redact --config=.gitleaks.toml --source .
```

Both must return clean.

### Step 5 -- Commit
```
git add <target> _Logs/sanitization-audit.md
git commit -m "chore(ip): sanitize and add <target> from <source-id>"
```

The pre-commit hook re-runs the sanitization lint as a final guardrail.

---

## Verification Loop

Before marking a sanitization pass complete:

1. **Diff review** -- Did every replacement land where expected?
2. **Lint clean** -- `bash scripts/lint_sanitization.sh` returns 0 matches?
3. **Gitleaks clean** -- `gitleaks detect --redact` returns 0 findings?
4. **Audit entry present** -- New row in `_Logs/sanitization-audit.md` with reviewer name + token count?
5. **No raw source in repo** -- `git status` should NOT show `~/scratch/` files staged.

If any pass fails, fix and re-run. The v1.2.0+ release tag is blocked until every file under `ip/authored/` and `playbooks/` has at least one entry in the audit log.

---

## Common Mistakes

- **Skipping human review.** The script handles 95% of cases; the remaining 5% are paraphrases, tone, and context that only a human catches.
- **Forgetting `--audit`.** If you sanitize without auditing, the release gate will block the freeze. Re-run with `--audit`.
- **Editing the lexicon without rationale.** Every change to the banned-token list belongs in `_Logs/sanitization-audit.md` with a one-line reason.
- **Pasting raw content into the repo first, sanitizing later.** Git history retains raw content even after later sanitization. Always sanitize *before* `git add`.

---

## When the Lexicon Needs to Change

Adding a new banned token:
1. Edit both `scripts/lint_sanitization.sh` (PATTERNS array) and `scripts/sanitize_from_notion.py` (RULES list).
2. Add a matching rule to `.gitleaks.toml`.
3. Append to `_Logs/sanitization-audit.md` with the rationale.
4. Run `bash scripts/lint_sanitization.sh` over the full tree -- if existing committed content matches, escalate before merging.

Removing a banned token (rare):
1. Document the rationale in `_Logs/sanitization-audit.md`.
2. Get explicit sign-off in the PR description.
3. Update all three files in lockstep.

---

*Owned by: the human reviewer running the pass. Reviewed at every v1.x.0 minor release.*
