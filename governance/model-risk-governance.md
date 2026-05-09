# Model Risk Governance

> Lifecycle governance for AI / ML models from inception to retirement. Pattern-driven; forks should map to their actual model risk regime (e.g., SR 11-7 in US banking, ECB TRIM, OSFI E-23).

## Lifecycle stages

| Stage | What governance checks |
|---|---|
| **1. Design** | Business need · expected impact · data sources · methodology choice · alternatives considered |
| **2. Development** | Train/test split discipline · feature engineering documented · disparate impact tested · explainability artifacts |
| **3. Validation** | Independent validator (not the developer) · benchmark comparison · stress test · backtesting |
| **4. Deployment** | Production-readiness · monitoring · incident response · rollback plan |
| **5. Monitoring** | Performance drift · data drift · concept drift · disparate-impact re-test |
| **6. Retirement** | Formal decommissioning · archival · downstream-impact assessment |

## Risk tiering

Tier each model at design:

| Tier | Definition | Governance burden |
|---|---|---|
| **High** | Material financial impact · regulatory reporting · automated decisions affecting customers / employees | Full lifecycle review · independent validation · exec approval |
| **Medium** | Operational efficiency · internal decision support | Lifecycle review · peer validation |
| **Low** | Internal experimentation · prototypes · advisory only | Self-attested · sandbox-only |

## Mandatory artifacts (High-tier)

- **Model card** — name · version · purpose · training data · performance metrics · disparate-impact test · known limitations.
- **Data sheet** — sources · lineage · classification per column · consent basis · refresh cadence.
- **Validation report** — independent validator · methodology review · sensitivity analysis · stress tests · sign-off.
- **Monitoring spec** — metrics · thresholds · alert routes · escalation.
- **Incident playbook** — rollback procedure · stakeholder notification · post-mortem template.

## Common failure modes

- **Drift unmonitored.** Models silently degrade until a customer complaint surfaces it.
- **Validation by the developer.** "Independent" must be organizationally independent.
- **Unaudited prompt injection** for LLM-based features. Prompt injection is the new SQL injection.
- **Data subject's consent doesn't cover AI training.** Re-purposing is a regulatory trap.
- **Missing rollback plan.** When the model fails, the only option is "turn it off" — and that's a customer-facing event.

## Applied to AI agents

Agentic AI systems compound model risk:

- The agent's reasoning trace is itself a model output — log it (`context-wall-meta-knowledge-graph.md`).
- Tool calls are model decisions — entitlement-check before execution.
- Multi-agent workflows have emergent failure modes — observe at the workflow level (Bain Layer 2).
- Memory + tool access raises blast radius — segregated tenants per agent risk tier.

## Cross-references

- `data-ethics-policy.md` — ethical underpinning.
- `dpia-template.md` — DPIA is mandatory for High-tier models with material impact.
- `../ip/curated/bain-3-layer-agentic.md` — Bain's Observability layer is the technical implementation of monitoring.
- `../ip/curated/defending-ai-spend-12q.md` — Q5 (AI maturity in operations) and Q10 (risk governance) test this discipline.
