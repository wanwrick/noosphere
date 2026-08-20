# Scripts — Routing

Executable gates. Nothing here is documentation; every file either blocks a
commit or reports a verdict.

| File | Purpose |
|---|---|
| `lint_sanitization.sh` | Invariant #0 — banned-token guard over the working tree |
| `sanitize_from_notion.py` | Rewrites private-source content into placeholder form |
| `verify_all.sh` | Runner for the 9 verification checks; non-zero exit on any FAIL |
| `verify/` | The 9 checks themselves |

## Run the gates

```bash
bash scripts/lint_sanitization.sh   # Invariant #0 only, fast
bash scripts/verify_all.sh          # all 9 checks, what CI runs
```

`lint_sanitization.sh` needs `ripgrep`. `06`/`07` need `pyyaml`.
`04` needs the `databricks` CLI plus `pytest`; it prints SKIP when either is
absent rather than failing.

## The 9 checks

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

## Editing root CLAUDE.md

Checks 01–03 make the root file the most constrained file in the repo. Before
committing a change to it:

1. **Budget.** The file sits close to the cap. Every added word costs a removed
   word. Note that `wc -w` counts a standalone `·` as a word.
2. **Routing.** Any backticked token ending in `.md`, `.sh`, `.py`, `.yaml`,
   `.yml`, `.json`, or `/` must exist. Add the target file before the route.
3. **Skills.** Under the `## Skills` heading, backtick only real skill or
   subagent names. Check 03 reads that section literally.

Then run `bash scripts/verify_all.sh` and confirm 9 pass · 0 fail.

## Adding a check

Drop `verify/<NN>_<name>.{sh,py}` in, add it to the `CHECKS` array in
`verify_all.sh`, and log the addition per `_Logs/CLAUDE.md`. Shell checks are
invoked with `bash`, Python with `python3`; both receive `ROOT`. Exit non-zero
to fail. Print `SKIP:` and exit 0 when a tool is genuinely unavailable.

## Wired into

`.pre-commit-config.yaml` (sanitization lint + gitleaks + hygiene hooks),
`.github/workflows/sanitization.yml` (banned-token guard + gitleaks),
`.github/workflows/verify.yml` (all 9 checks). Both workflows run on pull
requests to `main` and pushes to `main`.
