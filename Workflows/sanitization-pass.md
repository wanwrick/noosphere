# Workflow -- Sanitization Pass

**Purpose:** Step-by-step procedure for refreshing IP from Notion into the repo without leaking employer / team / stakeholder / JIRA / vendor / Databricks-internal references.

**When to run:** Any time you pull content from Notion (or any private source) into a file under `ip/`, `playbooks/`, `templates/`, `Workflows/`, or `decisions/`.

**Prerequisites:**
- `ripgrep` installed (the `rg` binary).
- `python3` available.
- `pre-commit install` already run in your local clone (so commit-time gates fire).
- **A local lexicon.** The real banned-token list is not in this repository —
  it names the very terms it protects, and this repo is public. Bootstrap once
  per clone:

  ```
  cp .sanitization-lexicon.example .sanitization-lexicon.local
  # then replace the placeholders with your real terms
  ```

  The canonical copy lives in `noosphere-private`. Without a local lexicon
  every tool here runs on placeholders and says so loudly — it will not
  silently pass.

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
bash scripts/lint_sanitization.sh --require-real-lexicon
gitleaks detect --redact --config=.gitleaks.toml --source .
```

Both must return clean. `--require-real-lexicon` makes the run fail rather than
fall back to placeholders, which is what you want before a commit.

`gitleaks` covers secrets and structural IDs only; proper-noun matching lives
entirely in `lint_sanitization.sh`, driven by your local lexicon.

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

The lexicon is now **one file**, not three call sites. Both
`scripts/lint_sanitization.sh` and `scripts/sanitize_from_notion.py` read it at
runtime, so there is no lockstep edit to get wrong.

Adding a new banned token:
1. Add a line to `.sanitization-lexicon.local` --
   `category<TAB>flags<TAB>pattern<TAB>replacement`. Tabs, not spaces.
2. Mirror it into the canonical copy in `noosphere-private`, and update the
   `SANITIZATION_LEXICON` repo secret so CI sees it too.
3. Append to `_Logs/sanitization-audit.md` with the rationale. (Record the
   *category and reason*, not the term itself -- that log is public.)
4. Run `bash scripts/lint_sanitization.sh --require-real-lexicon` over the full
   tree -- if existing committed content matches, escalate before merging.

Removing a banned token (rare):
1. Document the rationale in `_Logs/sanitization-audit.md`.
2. Get explicit sign-off in the PR description.
3. Remove the line from the local lexicon, the canonical copy, and the secret.

**Never** add a real term to `.sanitization-lexicon.example`. That file is
committed and public; it holds placeholders only.

---

*Owned by: the human reviewer running the pass. Reviewed at every v1.x.0 minor release.*
