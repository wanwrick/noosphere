# Scripts — Routing

Executable gates. Nothing here is documentation; every file either blocks a
commit or reports a verdict.

| File | Purpose |
|---|---|
| `lint_sanitization.sh` | Invariant #0 — banned-token guard over the working tree; loads a gitignored lexicon |
| `lint_pii.py` | Personal-data guard: email, phone, SIN/SSN, card, IP, address, DOB, ID numbers |
| `sanitize_from_notion.py` | Rewrites private-source content into placeholder form; same lexicon |
| `verify_all.sh` | Runner for the 10 verification checks; non-zero exit on any FAIL |
| `verify/` | The 10 checks themselves |

## The lexicon (read this first)

`lint_sanitization.sh` and `sanitize_from_notion.py` both need a banned-token
lexicon, and **it is not in this repository**. It enumerates the employer,
team, vendor, and stakeholder proper nouns it exists to suppress, so
committing it to a public repo would publish exactly that list. Bootstrap once
per clone:

```bash
cp .sanitization-lexicon.example .sanitization-lexicon.local
# then replace the placeholders with your real terms
```

Load order: `$NOOSPHERE_LEXICON`, then `.sanitization-lexicon.local`, then
`.sanitization-lexicon.example`. Falling through to the example prints a loud
NOT-PROTECTED banner — it never silently passes. Pass
`--require-real-lexicon` to fail instead. The canonical copy lives in
`noosphere-private`; CI reads it from the `SANITIZATION_LEXICON` repo secret.

## The PII rules (tracked, unlike the lexicon)

`lint_pii.py` reads `.pii-patterns` and `.pii-allowlist`, and **both are
committed**. That looks inconsistent with the lexicon rule above until you see
what each file holds.

| | Lexicon | PII rules |
|---|---|---|
| Contains | The actual proper nouns | Generic format regexes |
| Publishing it | Publishes exactly what it protects | Reveals nothing |
| A fork gets | Nothing until it bootstraps | Working protection immediately |

"An email address shaped like `x@y.z`" identifies nobody. Tracking the rules is
the only way a template repo protects the people who fork it.

Each rule carries a **canary** the pattern must match, verified at load. A
regex typo compiles fine and then matches nothing, so the gate reports clean
while protecting nothing — a silent failure indistinguishable from success. A
rule that fails its canary is a hard error. Same discipline as the lexicon.

Allowlist entries match the **matched text**, not the line, so a line carrying
both a documentation IP and a real one still fails. Full procedure and triage
table: `Workflows/pii-audit-pass.md`.

## Run the gates

```bash
bash scripts/lint_sanitization.sh --require-real-lexicon   # Invariant #0, fast
python3 scripts/lint_pii.py                                # personal data, fast
bash scripts/verify_all.sh                                 # all 10 checks, what CI runs
```

Add `--files-only` to report offending paths without echoing the pattern or
the matched line — use it anywhere the output is public, such as CI logs.

`lint_sanitization.sh` needs `ripgrep`. `06`/`07` need `pyyaml`. `lint_pii.py`
needs only the standard library.
`04` needs the `databricks` CLI plus `pytest`; it prints SKIP when either is
absent rather than failing.

## The 10 checks

| Check | Asserts |
|---|---|
| `verify/01_token_budget.sh` | Root `CLAUDE.md` ≤600 tokens, estimated as `LC_ALL=C wc -w` × 1.3 |
| `verify/02_routing.sh` | Every backticked path in root `CLAUDE.md` exists on disk |
| `verify/03_skill_invocation.sh` | Every name under the root `## Skills` heading resolves to `.claude/skills/<name>/SKILL.md`, or to one of the three subagents in `.claude/agents/` |
| `verify/04_dabs_end_to_end.sh` | DABs subproject validates and its unit tests pass |
| `verify/05_attribution_lint.sh` | Invariant #3 — every `ip/curated/*.md` carries a Source callout |
| `verify/06_governance_gate.py` | Every `regulated: true` archetype declares `dpia_required` and `dpia_completed` explicitly |
| `verify/07_ip_coverage.py` | Invariant #1 — every archetype names ≥1 IP file, and every slug resolves |
| `verify/08_sanitization_audit.sh` | Wraps `lint_sanitization.sh` |
| `verify/09_diagram_coverage.sh` | Every diagram declared in `methodology/diagram-generation.md` exists in `_Diagrams/` |
| `verify/10_pii_scan.py` | No personal data in the working tree; wraps `lint_pii.py --files-only` |

## Editing root CLAUDE.md

Checks 01–03 make the root file the most constrained file in the repo. Before
committing a change to it:

1. **Budget.** The file sits close to the cap. Every added word costs a removed
   word. Note that `wc -w` counts a standalone `·` as a word.
2. **Routing.** Any backticked token ending in `.md`, `.sh`, `.py`, `.yaml`,
   `.yml`, `.json`, or `/` must exist. Add the target file before the route.
3. **Skills.** Under the `## Skills` heading, backtick only real skill or
   subagent names. Check 03 reads that section literally.

Then run `bash scripts/verify_all.sh` and confirm 10 pass · 0 fail.

## Adding a check

Drop `verify/<NN>_<name>.{sh,py}` in, add it to the `CHECKS` array in
`verify_all.sh`, and log the addition per `_Logs/CLAUDE.md`. Shell checks are
invoked with `bash`, Python with `python3`; both receive `ROOT`. Exit non-zero
to fail. Print `SKIP:` and exit 0 when a tool is genuinely unavailable.

## Wired into

`.pre-commit-config.yaml` (sanitization lint + PII lint + gitleaks + hygiene
hooks), `.github/workflows/sanitization.yml` (banned-token guard + PII guard +
gitleaks), `.github/workflows/verify.yml` (all 10 checks). Both workflows run
on pull requests to `main` and pushes to `main`.
