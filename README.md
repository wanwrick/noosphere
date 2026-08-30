# Noosphere — Practice Operating System

**The operating system of a Data & AI Strategy practice. Open-sourced. Authored by Paroz Mehta (Cornell-Queen's EMBA CA26).**

A portable, fork-and-customize, version-controlled practice OS for any Data & AI team operating in regulated industry. Pairs original authored IP with 12 attributed industry methodologies and Cornell-Queen's EMBA framework grounding. Ships with a real, working DABs Data-Contract Golden Path subproject so any data team can clone, fill in `data-contract.yml`, and have a contract-enforcing pipeline running the same week.

---

## Three Killer Signals

> **🚀 No LAC — *No Lack of Analytical Capability.***
> *Land it once. Land it well. Get out of the business's way.*
> Bronze ingests almost everything plausibly needed for analytics; iteration speed lives in the Silver → Gold → Platinum tier; the platform stops being a gatekeeper. **A humility principle as much as a technical one.** See `ip/authored/no-lac-principle.md`.

> **🤖 AI-Ready Platinum Layer.**
> Unity Catalog metadata as the runtime semantic layer for AI agents. 5 Principles + 6-question metadata rubric. Network-effect economics: *1× publish → 1× govern → 5+ consume.* See `ip/authored/ai-ready-platinum-layer.md`.

> **🛠️ DABs Data-Contract Golden Path — a real working forkable subproject.**
> One `data-contract.yml` declares a data product. The bundle wires it into Bronze ingestion + Silver DLT expectations + Gold transformations + Platinum AI-ready views + Unity Catalog ABAC + CI/CD validation. **Forkable today.** See `templates/dabs-data-product-template/`.

---

## Who Authored This

**Paroz Mehta · Data Product Manager · Building agentic-ready data platforms in regulated financial services.**
Cornell-Queen's EMBA CA26 · NBAB5630 Strategic Planning · [LinkedIn](https://linkedin.com/in/parozmehta) · [github.com/wanwrick/noosphere](https://github.com/wanwrick/noosphere)

The repo doubles as a portfolio artifact AND a forkable practice OS. One repo, multiple audiences: data teams cloning the DABs Golden Path; case-interview prep workbook; recruiter-magnet at MBB / Senior Tech PM / Director-level Data & AI roles.

---

## What's New in v1.4.0

| Capability | What landed |
|---|---|
| **PII gate** (Invariant #0, second half) | `scripts/lint_pii.py` blocks any commit carrying personal data — email, phone, SIN/SSN, payment card, IBAN, IP, postal code, street address, date of birth, passport, licence. Runs in pre-commit, in CI, and as verification check 10. Sanitization protects organizations; this protects people. |
| **Rules ship tracked** | Unlike the banned-token lexicon, `.pii-patterns` and `.pii-allowlist` are committed. They hold generic format regexes that identify nobody, so **a fork inherits PII protection with no setup** — the only arrangement that protects people who skip the setup step. |
| **Career Command Center made fork-safe** | Ten files that a session fills with a name, salary expectation, work authorization, and recruiter and interviewer names were tracked, guarded only by a comment. Each now ships as a tracked `.example` with the live copy gitignored and created by `bootstrap.sh`. |
| **Disclosure route** | `SECURITY.md` gives a private way to report an exposure. Previously the only option was a public issue, which republishes the value to everyone watching. |
| **Audit procedure** | `Workflows/pii-audit-pass.md` covers all six exposure surfaces — four of which survive a clean `git status` — plus the triage table separating a leak from a byline, an attribution, and a false positive. |

---

## What's New in v1.3.0

| Capability | What landed |
|---|---|
| **Routing coverage completed** | Seven directories that held real content but no routing brain now have one: `Workflows/`, `Templates/`, `Knowledge/Work/`, `_Registry/`, `_Logs/`, `scripts/`, `templates/`. Every top-level content directory is now reachable from `CLAUDE.md`. |
| **Gates documented where they live** | `scripts/CLAUDE.md` documents the verification checks, the three constraints on editing the root routing brain (token budget, routing targets, skill names), and how to add a check. |
| **Career Command Center routed** | The forkable job-search OS shipped in v1.2.1 but was unreachable from the routing table. `templates/CLAUDE.md` now covers both subprojects and draws the line between a subproject's own `CLAUDE.md` (payload for a fork) and this repo's instructions. |
| **Directory tree corrected** | The tree described a subdivided `playbooks/` and a `templates/dabs-data-product-template/examples/` folder; neither exists. Tree now matches disk. |

---

## What's New in v1.2.0

| Capability | What landed |
|---|---|
| **Sanitization Protocol** (Invariant #0) | Banned-token lint + gitleaks + GitHub Actions gate; no employer / team / stakeholder / JIRA / Databricks-internal IDs in committed content. See `Workflows/sanitization-pass.md` and `_Logs/sanitization-audit.md`. |
| **No LAC Atomic Framework** | Bronze → Silver I/II/III → Gold → Platinum medallion architecture with custom code only at Gold. Cloud-agnostic outputs. See `ip/authored/no-lac-principle.md`. |
| **AI-Ready Platinum Layer** | 5 Principles + 6-question metadata rubric for serving AI agents alongside Power BI. See `ip/authored/ai-ready-platinum-layer.md`. |
| **DABs Data-Contract Golden Path subproject** | ~40-file working Databricks Asset Bundle template. `data-contract.yml` → DLT expectations + UC ABAC + Platinum scoped views + AI Consumption Contract. See `templates/dabs-data-product-template/`. |
| **10Q Framework + toolkit** | New data source onboarding stress-test across 10 dimensions, with intake form, elicitation guide, tracker schema, Miro blueprint spec. See `ip/authored/10q-framework.md`. |
| **Enterprise CLAUDE.md pattern** | Production-ready CLAUDE.md skeleton for regulated-industry data engineering teams. See `ip/authored/enterprise-claude-md.md`. |
| **12 curated industry methodologies** | Mahboub · Grover · Hewing · Tekiner · Czarnas · Baeyens · Bain · Kocyigit · Shi (×2) · Dataplex 6 Principles · CDO Top 10. Every file carries a Source callout. See `ip/curated/`. |
| **EMBA framework expansion** | ~50 framework files across `Knowledge/EMBA/` and `Knowledge/Strategy/` covering Critical Thinking, Negotiation Suite, Corporate Finance core, Operations Management Suite, Cornell 5-Phase Strategic Process, Strategy Meta Framework, Roger Martin's Strategic Choice Cascade. |
| **5 anonymized archetypes** | Engagement archetypes for regulated FSI platform launch, marketing modernization with CDP + clean rooms, self-serve tenant flatpack, agentic self-serve analytics, legacy DW → cloud lakehouse. See `initiatives/archetypes/`. |
| **7 v1.2.0 skills + 3 atomic subagents** | `claude-md-bootstrap`, `data-source-10q-intake`, `dabs-template-init`, `governance-audit`, `ai-consumption-contract`, `defending-ai-spend-memo`, `weekly-practice-synthesis` plus `dq-validator` · `schema-reviewer` · `compliance-checker` atomic subagents. |
| **13 Mermaid architecture diagrams** | Generated and embedded across flagship IP files + DABs Golden Path docs + README. |

---

## Architecture (Three Layers)

```
+--------------------------------------------------------------------+
|  SHARED DISCIPLINE                                                 |
|    governance/ · Workflows/ · _Registry/ · _Logs/ · scripts/       |
|    .claude/skills/ · .claude/agents/ · templates/                  |
+--------------------------------------------------------------------+
|  SHARED QUERIES                                                    |
|    initiatives/ · data-products/ · playbooks/ · talent/            |
+--------------------------------------------------------------------+
|  SHARED CONTEXT                                                    |
|    practice-context/ · methodology/ · ip/{authored,curated}/       |
|    Knowledge/Frameworks/ · Knowledge/EMBA/ · Knowledge/Strategy/   |
+--------------------------------------------------------------------+
```

The DABs Data-Contract Golden Path subproject sits at the boundary of Discipline and Queries: it operationalizes 6 named methodologies (No LAC + AI-Ready Platinum + Czarnas + Baeyens + Kocyigit + Shi×2) into a single forkable Databricks Asset Bundle with `data-contract.yml` as the single source of truth.

---

## Directory Structure (v1.4.0)

```
noosphere/
+-- CLAUDE.md                        Routing brain (CI-capped at 600 tokens)
+-- README.md                        This file
+-- GOALS.md                         Priorities + OKRs (private to your fork)
+-- CONTRIBUTING.md                  Fork-and-customize guide
+-- SECURITY.md                      Private disclosure route + known residual exposure
+-- LICENSE                          MIT
+-- .gitleaks.toml                   Secret scanning + structural ID rules
+-- .pii-patterns                    PII detection rules (tracked: generic formats)
+-- .pii-allowlist                   Justified PII false positives
+-- .pre-commit-config.yaml          Sanitization + PII gates at commit time
+-- .github/workflows/               sanitization.yml + verify.yml CI gates
+--
+-- practice-context/                Identity, voice, stack, regulated context
+-- methodology/                     How we work, attribution policy, diagrams
+-- ip/
|   +-- authored/                    Original IP (sanitized)
|   |   +-- no-lac-principle.md
|   |   +-- ai-ready-platinum-layer.md
|   |   +-- 10q-framework.md
|   |   +-- 10q-toolkit/
|   |   +-- enterprise-claude-md.md
|   |   +-- platform-mandate-playbook.md
|   |   +-- dabs-data-contract-golden-path.md
|   +-- curated/                     12 named industry sources, attributed
+--
+-- initiatives/
|   +-- initiatives.yaml             Engagement registry (anonymized archetypes)
|   +-- archetypes/                  5 archetype examples
+-- data-products/
|   +-- data-products.yaml           Data product registry
|   +-- ai-consumption-contract-template.md
|   +-- _example-platinum-domain.md  Generic example entry (forks replace)
+--
+-- playbooks/
|   +-- producer-onboarding.md       Intake -> bundle -> consumer notification
|   +-- governance-runbook.md        Regulated phase advance, audit, DPIA refresh
|   +-- change-management.md         Platform change + deprecation discipline
|   +-- engagement-kickoff.md        New engagement, discovery week shape
+--
+-- talent/                          Roles, capability matrix, bench policy
+-- governance/                      Ethics, model risk, classification, NDA, DPIA
+-- insights/                        Publishable POV articles
+-- Knowledge/
|   +-- Frameworks/                  8 evergreen MBA framework domains
|   +-- EMBA/                        ~30 Cornell-Queen's EMBA frameworks
|   +-- Strategy/                    Cross-cutting strategy toolkits
|   +-- Work/                        Operational context
|   +-- Decisions/                   Logged decisions
+--
+-- Templates/                       Document formats (decision-memo, status, RCA, story)
+-- Workflows/                       Step-by-step playbooks (incident, briefing, sanitization-pass, …)
+-- _Registry/                       Skills, MCPs, Cadences
+-- _Logs/                           evolution.md, feedback.md, sanitization-audit.md
+-- _Diagrams/                       PNG + Mermaid architecture visuals
+-- scripts/                         Gates: lint_sanitization.sh, sanitize_from_notion.py
|   +-- verify/                      The 10 verification checks
|   +-- verify_all.sh                Runner (what CI executes)
+--
+-- templates/dabs-data-product-template/   ← THE FLAGSHIP SUBPROJECT
    +-- data-contract.yml            Single source of truth
    +-- databricks.yml               Bundle config wires contract → resources
    +-- src/contract/                Contract loader + checks (Python)
    +-- src/pipelines/               Bronze · Silver · Gold · Platinum (Python)
    +-- tests/                       Unit + integration + fixtures
    +-- scripts/                     validate_bundle.sh + deploy.sh + AI contract gen
    +-- .github/workflows/           ci.yml + deploy.yml
    +-- docs/                        4 walkthrough docs
+-- templates/career-command-center/       ← FORKABLE JOB-SEARCH OS
    +-- profile.yml                  User profile (drives every response)
    +-- .claude/skills/              6 slash commands (onboard, tailor-resume, …)
    +-- job-search/ interview-prep/ career-strategy/   Routed subfolders
+-- .claude/skills/                  7 Practice OS skills
+-- .claude/agents/                  3 atomic subagents
```

---

## How to Fork (Ready-to-Play in 4 Weeks)

### Week 1 — Read + identity
- Read `CLAUDE.md`, `practice-context/about.md`, `methodology/how-we-work.md`.
- Populate `practice-context/about.md` with your identity. Keep the structure; replace identity-specific content.
- Run `bash scripts/lint_sanitization.sh` to confirm zero banned-token leakage in your fork.

### Week 2 — Bootstrap your own Enterprise CLAUDE.md
- Use the `claude-md-bootstrap` skill against your own data platform repo.
- Adapt the pattern (`ip/authored/enterprise-claude-md.md`) to your stack — Databricks/Snowflake/dbt/Fabric — and regulator (OSFI/SOX/HIPAA/SOC2/GDPR).

### Week 3 — Seed your first archetype + first 10Q intake
- Copy one of the 5 archetypes to your `initiatives/` registry.
- Run a 10Q discovery session against a real new data source using the toolkit.
- Apply ≥1 IP framework (authored or curated) — log it in `ip_applied`.

### Week 4 — Fork the DABs Golden Path
- Copy `templates/dabs-data-product-template/` into your platform repo.
- Fill in `data-contract.yml`. Run `databricks bundle validate`. Run the test suite.
- Wire the GitHub Actions to your environments. Ship your first contract-enforced data product.

---

## Adoption Models

| Mode | Setup time | Governance overhead | Expected lift |
|---|---|---|---|
| **Solo Practitioner** | 1 day | Light: identity + invariants only | Repeatable methodology + LinkedIn-magnet portfolio |
| **Small Pod (2–5)** | 1 week | Medium: capability matrix + cadences | Shared vocabulary + reusable IP across pod |
| **Full Practice (>5)** | 2 weeks | Full: governance register + DPIA + sanitization audit | Cross-pod consistency + audit trail + compounding IP |

---

## Governance & Trust

- **Sanitization** — `Workflows/sanitization-pass.md` + `_Logs/sanitization-audit.md`. Banned-token lint + gitleaks + CI gate. v1.2.0+ release tag blocked on a clean audit.
- **Personal data** — `Workflows/pii-audit-pass.md` + `scripts/lint_pii.py`. Blocks personal data of any individual, the author's and other people's alike. Report an exposure privately via `SECURITY.md`, never a public issue.
- **Data ethics + classification** — `governance/data-ethics-policy.md`, `governance/client-data-classification.md` (CDMC-aligned 4-tier).
- **NDA + DPIA + regulated-FSI runbook** — `governance/nda-template.md`, `governance/dpia-template.md`, `governance/regulated-fsi-compliance-runbook.md` (OSFI-style + PIPEDA-style).
- **Model risk** — `governance/model-risk-governance.md`.

---

## How to Extend

| Goal | Action |
|---|---|
| Add a knowledge domain | Create a file under `Knowledge/{Frameworks,EMBA,Strategy}/`; add routing rule to `CLAUDE.md`; bump version in `_Logs/evolution.md`. |
| Add an authored IP page | Create under `ip/authored/`; sanitize first; add to `ip/authored/CLAUDE.md` index; bump version. |
| Add a curated framework | Create under `ip/curated/` with a Source callout (author + URL); attribution lint enforces. |
| Add a workflow | Create under `Workflows/`; add to `_Registry/Cadences.md` if trigger-based. |
| Add a skill | Create under `.claude/skills/<name>/SKILL.md` with YAML frontmatter; register in `_Registry/Skills.md`. |
| Add a worked DABs example | Drop into `templates/dabs-data-product-template/`; ensure `databricks bundle validate` and the unit tests pass. |
| Add a routing rule | Create the target file first, then add the row to `CLAUDE.md`; the root file is capped at 600 tokens, so budget a removal for every addition. |
| Add a verification check | Add `scripts/verify/<NN>_<name>.{sh,py}`; register it in the `CHECKS` array in `scripts/verify_all.sh`. |
| Refresh from Notion | Follow `Workflows/sanitization-pass.md`. |
| Update priorities | Edit `GOALS.md` at the start of each quarter. |

---

## License + Acknowledgements

**MIT.** See [LICENSE](LICENSE).

This project stands on the shoulders of named authors. Every curated framework file in `ip/curated/` carries a Source callout citing the original author + URL. Particular thanks to:

- **Yassine Mahboub** (Data Thinking 4 Pillars), **Raj Grover** (Defending AI & Architecture Spend 12-Question Pressure Test), **Sebastian Hewing** (9-Question Canvas to Escape the Dashboard Factory), **Firat Tekiner** (Context Wall + Meta Knowledge Graph), **Piotr Czarnas** (Data Product Architecture: 5 Engineering Pillars), **Tom Baeyens** (Data Contracts as Producer-Consumer Interface), **Yasar Kocyigit** (Metadata-Driven Lakehouse Ingestion Framework, open source), **Mengyu Shi** (DABs Custom Templates + DABs CI/CD Asset Bundles), **Bain & Company** (Agentic AI Platform 3-Layer Architecture, Apr 2026), **Google Cloud** (Dataplex 6 Data Product Principles).
- **Cornell-Queen's EMBA faculty** — Risa Mish (Congress Model), Shai Dubey (Negotiation), Hambrick & Fredrickson (Strategy Diamond), Nadler & Tushman (Congruence Model), Kotter (8-Step Change Management), and the NBAB5630 Strategic Planning toolkit.
- **Boris Jeltsky** (build-in-public AI PM patterns), **Andrej Karpathy** (autoresearch loop pattern), **Aakash Gupta** (Team OS shape).

Built by [Paroz Mehta](https://linkedin.com/in/parozmehta) · Cornell-Queen's EMBA CA26 · [github.com/wanwrick/noosphere](https://github.com/wanwrick/noosphere)
