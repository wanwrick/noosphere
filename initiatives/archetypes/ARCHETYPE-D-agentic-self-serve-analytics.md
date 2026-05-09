# ARCHETYPE-D — Agentic Self-Serve Analytics

> **Pattern:** Power BI semantic layer + AI/BI Genie + agentic analytics pilot built on the AI-Ready Platinum Layer. Both BI humans and AI agents read from the same governance plane.

## When this archetype fits

- Self-serve analytics is the strategic objective and the org is ready for AI-augmented consumption.
- A semantic layer exists or can be built in the next quarter.
- Producer team owns Platinum and wants both BI + agent consumers as first-class.

## Phases

| Phase | What happens |
|---|---|
| Qualify | Genie / agentic readiness assessment; semantic-layer gap analysis; identify pilot domain |
| Diagnose | Metadata coverage audit on the pilot domain (against the 6-question rubric) |
| Design | AI-Ready Platinum design per `ai-ready-platinum-layer.md`; scoped views designed; UC Functions planned |
| Build | First Platinum domain reaches 100% metadata coverage; scoped views + UC Functions deployed; MCP-path testing |
| Embed | Agentic pilot live; benchmark suite running; Genie space approved by stakeholders |
| Exit | Pilot proven; second domain on the same template |

## IP applied

| IP | Role |
|---|---|
| `ai-ready-platinum-layer.md` (authored) | The headline IP; 5 Principles + 6-question rubric drive everything |
| `no-lac-principle.md` (authored) | Architectural commitment |
| `dabs-data-contract-golden-path.md` (authored) | Per-product implementation; `ai_consumption.*` block becomes the Platinum spec |
| `context-wall-meta-knowledge-graph.md` (curated, Tekiner) | Macro-pattern: meta knowledge graph |
| `bain-3-layer-agentic.md` (curated, Bain) | Reference architecture for the platform conversation |
| `defending-ai-spend-12q.md` (curated, Grover) | Quarterly board readiness |

## Regulatory pattern

PIPEDA-style + OSFI-style. DPIA mandatory for AI agent access to Restricted-class data. MCP-path masking testing mandatory before production.

## Operating cadence

- **Weekly:** Metadata-coverage standup; Genie benchmark run review.
- **Bi-weekly:** Stakeholder demo of new scoped views.
- **Monthly:** Defending AI Spend 12-Q scorecard for this archetype.
- **Quarterly:** Agentic pilot review with execs; expand or stop.

## Talent profile

| Role | Headcount band |
|---|---|
| Producer-side PO | 0.5 |
| Platinum metadata steward | 1 |
| Semantic-layer engineer | 1 |
| Agentic-analytics PM | 0.5 |
| Privacy steward | 0.25 |

## Common gotchas

- Agents in production before MCP-path masking is verified. The PII risk is real and harder to detect than dashboard-PII.
- Wide BI tables exposed directly to agents. Always create scoped views (5–8 columns) per question.
- Metadata coverage at 80% considered "good enough." For agents, 80% means 1-in-5 wrong answers — unacceptable.
- AI Consumption Contract treated as documentation. It IS the contract; auto-generate from `data-contract.yml`.

## Cross-references

- `../initiatives.yaml` row id `ARCHETYPE-D-…`
- `../../ip/authored/ai-ready-platinum-layer.md`
- `../../ip/curated/context-wall-meta-knowledge-graph.md`
- `../../ip/curated/bain-3-layer-agentic.md`
- `../../templates/dabs-data-product-template/docs/from-contract-to-ai-consumption.md`
