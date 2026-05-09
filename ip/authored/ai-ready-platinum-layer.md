# AI-Ready Platinum Layer

> **Core shift:** BI semantics live in Power BI (DAX). **AI semantics must live in Unity Catalog metadata.** A platform that serves BI well does not automatically serve AI agents well — the metadata bar is materially higher.

## Executive TL;DR

- **Design stance:** keep wide BI tables. Add narrow agent-scoped views and governed UC Functions.
- **Governance stance:** one governance model (Unity Catalog ABAC) powering two interfaces (DirectQuery + MCP).
- **Network-effect:** **1× publish → 1× govern → 5+ consume** (Power BI · AI/BI Genie · Claude via MCP · cloud-native agents · future MCP clients).
- **Coverage target:** 100% metadata coverage in Platinum, measured against the 6-question rubric below.

---

## Why this matters now

Three changes have made the Platinum layer the new center of gravity:

1. **Managed MCP servers** are in production.
2. **MCP Catalog + DBSQL MCP servers** make UC tables and UC Functions agent-discoverable.
3. **Multi-agent orchestration** is supervisor-pattern-mature; agents call other agents and share UC context.

The result: every Platinum table now has at least two consumer archetypes (BI human + AI agent) and the metadata expectations diverge sharply.

---

## BI vs AI consumption — what changes in practice

| Dimension | BI | AI |
|---|---|---|
| Where intelligence lives | Power BI (DAX) | Unity Catalog metadata |
| Optimal table shape | Wide, denormalized, pre-aggregated | Scoped, well-described, question-oriented |
| Naming + descriptions | Nice-to-have | Critical — input signal for SQL generation |
| Error mode | Wrong chart; humans catch | Hallucinated answer; humans may trust |
| Discovery | Manual via reports | Programmatic via MCP Catalog |
| Trust | Earned over years | Built per session via metadata + lineage |

**Key insight:** for AI, metadata is not documentation. **Metadata IS the semantic layer.**

---

## The 5 Principles

### Principle 1 — Metadata becomes product

Treat metadata coverage and quality as critical-path work, not housekeeping. Target: **100% Platinum metadata coverage** against the 6-question rubric (next section). Lint enforces.

### Principle 2 — Scoped views for agents

Keep existing wide BI tables. Add **question-oriented views** with 5–8 columns each, named for what they answer (`vw_account_summary_for_agents`, not `account_dim`). Register the views as discoverable tools in the MCP Catalog.

### Principle 3 — UC Functions as business logic

Encode approved calculations as deterministic, governed UC Functions (e.g., `classify_balance_band`, `calculate_book_value`). Agents call functions; functions are auditable; outputs are consistent across BI and AI.

### Principle 4 — Dual interface, shared governance

| Interface | Path |
|---|---|
| Power BI | DirectQuery → SQL Warehouse → UC ABAC |
| AI Agents | MCP → Genie / DBSQL / UC Functions → UC ABAC |

Both enforce the same Unity Catalog ABAC. Governance is built once; consumers grow naturally.

### Principle 5 — Data Exchange becomes MCP marketplace

Publish internal Platinum data products as managed MCP servers. The MCP Catalog becomes the AI-facing discovery layer alongside the BI catalog.

---

## The 6-question metadata rubric

Every Platinum table or view description must explicitly answer all six:

1. **Grain** — one row per *what*?
2. **Answerable questions** — what is this table/view *for*? List 3–8 questions it cleanly answers.
3. **Time coverage** — what period is included? Earliest fact date and latest.
4. **Freshness** — refresh schedule and expected lag (with SLA).
5. **Currency / units** — what units apply? Currency? Time zone? Boolean conventions?
6. **Out of scope** — what does this table/view explicitly *not* cover?

Unity Catalog can autogenerate description drafts; **human review is mandatory** to meet the bar. Stub descriptions block agent consumption.

---

## Reference architecture (top-down)

```
+--------------------------------------------------+
| AI agents (Claude/MCP, Genie, cloud-native, …)   |
+--------------------------------------------------+
| MCP layer: Managed servers, MCP Catalog, OAuth   |
+--------------------------------------------------+
| Services: Genie Spaces, Vector Search, UC Funcs, |
| DBSQL                                             |
+--------------------------------------------------+
| Governance: Unity Catalog ABAC, governed tags,   |
| audit logs                                        |
+--------------------------------------------------+
| Data: Platinum schemas (one per domain)          |
+--------------------------------------------------+
```

---

## AI Consumption Contract section (mandatory in PRDs)

Every new data product PRD must include an "AI Consumption Contract" section with:

- **Answerable questions** — explicit list, scoped to the agent's job.
- **UC Functions exposed** — names + governance owner.
- **Metadata commitments** — coverage % against the 6-question rubric; freshness semantics.
- **Ownership** — who owns the metadata, who owns the UC Functions, who reviews drift.

The skill `ai-consumption-contract` (`.claude/skills/ai-consumption-contract/SKILL.md`) drafts this section automatically from a `data-contract.yml`. The DABs Golden Path subproject ships with `scripts/generate_ai_contract.py` that produces this section from the contract YAML.

Template: `templates/ai-consumption-contract.md`.

---

## Producer-side impact

Producer teams that adopt this layer absorb three new responsibilities:

1. **Metadata work escalates** from "governance hygiene" to "AI readiness foundation." Audience becomes LLMs, not only human catalog users.
2. **ABAC becomes agent policy.** Misconfiguration risk becomes materially higher: PII leakage through agent answers is harder to detect than through dashboards. Test coverage of MCP access paths is mandatory.
3. **Data product PRDs expand.** Every new data product carries an AI Consumption Contract section, not optional.

---

## 12-week pilot timeline (template)

| Week | Activity |
|---|---|
| W1–W2 | Define AI-ready metadata rubric; agree on definition of "100% coverage" |
| W2–W3 | Audit one Platinum domain's metadata; baseline coverage % |
| W3–W4 | Design top-10 scoped views for that domain |
| W4–W5 | Implement views in SIT; register UC Functions |
| W5–W6 | Test MCP server access to scoped views |
| W6–W7 | Validate ABAC for MCP access paths (PII masking, RLS, policy enforcement) |
| W7–W8 | Demo to leadership |
| W8–W10 | Extend to second Platinum domain |
| W10–W12 | Update PRD template ("AI Consumption Contract" section mandatory) |

---

## Risks + mitigations

| Risk | Mitigation |
|---|---|
| Metadata quality insufficient | 100% coverage rubric + mandatory human review on UC autogenerated descriptions |
| ABAC gaps for MCP access path | Dedicated MCP-path testing for masking + RLS + policy enforcement |
| Capacity constraints | Pilot scope: views/functions are lower-effort than pipelines; ship the pilot before extending |
| Vendor metadata gaps | Bake AI-ready description deliverables into vendor / source-team contracts |

---

## Cross-references

- `no-lac-principle.md` — Platinum is the layer where the LAC commitment manifests for both BI and AI.
- `dabs-data-contract-golden-path.md` — the contract YAML's `ai_consumption` section drives Platinum view generation.
- `../curated/context-wall-meta-knowledge-graph.md` — Tekiner's meta knowledge graph extends this principle to multi-domain agentic workflows.
- `../curated/bain-3-layer-agentic.md` — Bain's "Data + Knowledge" layer formalizes what AI-Ready Platinum delivers.
- `../curated/dataplex-six-data-product-principles.md` — Dataplex's 6 principles align with this layer's discipline.

---

## Diagram

See `_Diagrams/ai-ready-platinum-5-principles.md`.

---

*Owned by: the producer team's metadata steward. Reviewed: quarterly against the 6-question rubric.*
