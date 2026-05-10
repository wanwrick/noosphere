# Agentic AI Platform — 3-Layer Architecture

> **Source:** Bain & Company. *The Three Layers of an Agentic AI Platform* (Apr 2026). [Read it](https://www.bain.com/insights/the-three-layers-of-an-agentic-ai-platform/).

## Core insight

Legacy "model + API + ETL" stacks break for agentic AI. Modern platforms converge on **three layers** — Orchestration, Observability, Data + Knowledge — with **security and governance embedded by design** across all layers.

## The 3 Layers

| Layer | Purpose | What "good" looks like |
|---|---|---|
| **1. Application + Orchestration** | The "command center" — routes work to specialized agents, runs multi-step workflows, manages context handoffs, enforces tool access | Shared orchestration runtime · agent registry · tool catalog via MCP · governed reusable agent skills · identity propagation for non-human principals · audit tooling |
| **2. Analytics + Insight (Observability)** | Make agentic systems **operable, auditable, and governable** as they evolve nondeterministically | Full execution trace · per-agent + per-workflow + cross-agent logs and metrics · cost / token monitoring · behavioral drift detection · dashboards + anomaly detection |
| **3. Data + Knowledge** | Governed context for agents — the runtime substrate they reason over | Unified access across structured / unstructured / vector / graph · data contracts + schema governance · federated catalog with discoverability + lineage · streaming freshness · classification, masking, retention, cross-domain controls |

## Why this framing matters for interviews

Bain's framing is **the** reference architecture cited in MBB / strategy-consulting conversations about agentic AI. Three load-bearing claims:

1. **Orchestration becomes the center of gravity** — not the model.
2. **Observability is mandatory** for control, compliance, and operational safety.
3. **Governed context is runtime infrastructure** for agents.

## When to use this in this practice

- **Tech-strategy conversations** — Bain's 3-layer framing is more credible than "we built it ourselves" when proposing enterprise AI architecture.
- **Build-vs-buy decisions** per layer (orchestration / observability / data + knowledge).
- **Capability gap analysis** — score the org 1–5 on each layer; the lowest score is the next investment.

## How it applies in this practice

| Bain layer | This practice's component |
|---|---|
| Orchestration | MCP servers + Agent Bricks references in `practice-context/stack.md`; `templates/dabs-data-product-template/` registers UC Functions as governed agent tools |
| Observability | UC system tables + DLT pipeline observability + `_Logs/feedback.md` (agentic metadata feedback loop) |
| Data + Knowledge | The entire `ip/authored/no-lac-principle.md` + `ai-ready-platinum-layer.md` stack |

## Gaps the article doesn't address (track for execution)

The Bain article is a frame, not a blueprint. Concrete details left to the implementer:

- Which orchestration engine; how agent-to-agent (A2A) is implemented in practice.
- How entitlements are expressed, enforced, audited, reviewed.
- Memory strategy: what's persisted, retention, governance.
- Evaluation harness: offline evals, online canaries, rollback triggers, SLO regression thresholds.
- Security threat model: prompt injection, tool misuse, exfiltration, model supply chain.
- Operational ownership per layer (platform vs product teams), incident response, runbooks.
- Cost governance: token budgets, tool cost controls, chargeback / showback.

## Cross-references

- `context-wall-meta-knowledge-graph.md` (Tekiner) — the meta knowledge graph **is** the Data + Knowledge layer.
- `../authored/ai-ready-platinum-layer.md` — Principle 5 (Data Exchange becomes MCP marketplace) maps to Bain's Orchestration tool catalog.
- `defending-ai-spend-12q.md` (Grover) — Q3 (dependency mapping) becomes tractable if the 3 layers are mapped.
