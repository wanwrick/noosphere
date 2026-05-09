# Enterprise CLAUDE.md Pattern

> Pattern for a `CLAUDE.md` that anchors a regulated-industry data engineering team's AI work partner. The single source of engineering truth that every Claude session — across every engineer — inherits. Paired with `templates/enterprise-claude-md-skeleton.md`.

## Why an Enterprise CLAUDE.md matters

In enterprise data engineering the stakes are higher than a personal project:

- **Regulatory compliance** — every PII column carries audit obligations.
- **Multi-team coordination** — dozens of engineers, multiple domains, shared platform.
- **Complex infrastructure** — Databricks + cloud substrate + Terraform + CI/CD.
- **Data quality** — mistakes in Bronze cascade to Gold/Platinum downstream.

A shared `CLAUDE.md` becomes the contract that turns "AI assistant" into "AI work partner" — because every session inherits the same engineering rules, the same gotchas, and the same verification expectations.

## The anatomy of a good Enterprise CLAUDE.md

| Section | Purpose | Lines |
|---|---|---|
| 1. Project + description | Frame the AI's mental model | 3–5 |
| 2. Code style (per language) | Style the AI defaults to | 30–60 |
| 3. Key commands | The 10–15 commands engineers run most | 15–25 |
| 4. Architecture | Medallion layers + cross-platform topology + access model | 40–80 |
| 5. **Gotchas** | The hidden traps unique to this codebase | 30–60 |
| 6. Verification | What "done" looks like before merge | 15–25 |
| 7. Workflow rules | Plan Mode triggers · subagent triggers · review cadence | 15–25 |
| 8. Team conventions | Branching · PR description · commit messages · review counts | 10–20 |

Total: ~150–300 lines. Longer than that, and it becomes hard to keep accurate.

### What makes the gotchas section load-bearing

This is the section that earns the file its place. Every team has a list of "I learned this the hard way" rules. Most live in tribal knowledge. Putting them in CLAUDE.md means every new engineer (and every Claude session) inherits the lessons without re-paying the tuition.

Pattern:

```
### [Subsystem]
- [Imperative rule] — [Consequence if ignored]
```

Examples:
- "ALWAYS use explicit schema on Bronze tables — auto-detection causes silent data loss."
- "BigQuery external tables require Delta format on GCS, NOT Parquet."
- "DLT pipelines fail silently on schema mismatch — check DQ monitors after every deploy."

The imperative + consequence pairing is what gives Claude (and the engineer) a reason to remember.

## The trio of atomic subagents

Any Enterprise CLAUDE.md should ship with three atomic subagents:

| Subagent | What it validates |
|---|---|
| `dq-validator` | After pipeline changes: freshness, row count, null rates, schema, DLT expectation results |
| `schema-reviewer` | Schema changes for backwards compatibility, PII tagging, partitioning, DLT expectations |
| `compliance-checker` | Regulatory pattern compliance: PII tags, masking, audit logging, classification, secure-tenant rules |

These ship in this practice OS at `.claude/skills/{dq-validator,schema-reviewer,compliance-checker}/SKILL.md`. They are deliberately atomic — single-responsibility, low-token-budget, callable from any session — and parameterized by the regulator pattern (OSFI-style / GDPR / HIPAA / SOC 2 / SOX) the team operates under.

## Slash commands worth shipping

| Command | Purpose |
|---|---|
| `/deploy-dlt <env>` | Validate + deploy a bundle to env |
| `/validate-schema` | Compare current vs proposed schema against the data contract |
| `/run-dq-check <table>` | Run DQ monitor against a specific table |
| `/sanitize-from-notion` | Wrap `scripts/sanitize_from_notion.py` with friendly args |
| `/10q-intake` | Bootstrap a 10Q discovery session for a new source |

Each lives in `.claude/commands/<name>.md` (or equivalent) and reads from the skill registry.

## MCP setup checklist

| MCP | Use case |
|---|---|
| Lakehouse (Databricks / Snowflake / BigQuery) | Query data, validate tables, check federation |
| Notification (Slack) | Post DQ alerts, deployment status, team notifications |
| Observability (Sentry / DataDog) | Investigate production errors |
| Source control (GitHub) | PR management, issue tracking, code review |

All MCPs respect the same UC ABAC. No MCP gets data access that bypasses the governance plane.

## ROI you can promise leadership

| Metric | Before Enterprise CLAUDE.md | After (~4 weeks) |
|---|---|---|
| Claude correction rate | 3–5 per session | <1 per session |
| Code review turnaround | Hours | Minutes (subagent pre-review) |
| Schema-related incidents | Monthly | Near-zero (validator catches) |
| Compliance findings | Occasional | Zero (compliance-checker) |
| New engineer onboarding | 1–2 weeks to productive | Days |

These numbers are attainable, not aspirational — the win compounds because every session contributes back via `_Logs/feedback.md`.

## How to bootstrap one

The `claude-md-bootstrap` skill (`.claude/skills/claude-md-bootstrap/SKILL.md`) generates a starter Enterprise CLAUDE.md given:

- Project description (one paragraph).
- Stack signals (the skill auto-detects from `databricks.yml`, `dbt_project.yml`, `pyproject.toml`, `dataform.json`).
- Regulatory regime (OSFI-style / SOX / GDPR / HIPAA / SOC 2 / none).
- Subagent set (default trio + any custom additions).

Output is a complete CLAUDE.md draft. Engineer reviews + commits.

## Cross-references

- `templates/enterprise-claude-md-skeleton.md` — the filled-in skeleton this pattern produces.
- `.claude/skills/claude-md-bootstrap/SKILL.md` — the skill that automates draft generation.
- `.claude/skills/{dq-validator,schema-reviewer,compliance-checker}/SKILL.md` — the trio of atomic subagents.
- `practice-context/voice-and-style.md` — the verification loop pattern that the CLAUDE.md verification section enforces.

---

## Implementation roadmap

| Week | What ships |
|---|---|
| W1 | `CLAUDE.md` in main repo + `/init` bootstrap command |
| W2 | Add subagents (dq-validator, schema-reviewer) + slash commands |
| W3 | Connect MCP servers + post-edit hooks |
| W4+ | Compound — update `CLAUDE.md` from every PR review and retro |

The compounding step is the load-bearing one. The file gets better every week if and only if the team treats it as a living artifact.

---

*Owned by: data engineering lead. Reviewed: every retro.*
