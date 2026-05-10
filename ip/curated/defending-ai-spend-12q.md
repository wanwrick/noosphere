# Defending AI & Architecture Spend — 12-Question Board Pressure Test

> **Source:** Raj Grover. LinkedIn post on enterprise AI / architecture investment defense.

## Core question

**Could you defend your AI and architecture spend to the board *tomorrow*?** If your answers depend on narrative rather than numbers, value transparency is weak.

## The 12 questions

| # | Question | What it tests |
|---|---|---|
| 1 | Which technology investments are generating measurable enterprise value today, and what is the quantified impact? | **Value realization** |
| 2 | How much of your data and AI spend is directly tied to value streams vs. shared platform overhead? | **Capital allocation** |
| 3 | If one major platform were defunded tomorrow, which business capability would degrade, and by how much? | **Dependency mapping** |
| 4 | How did architecture shape the last capital allocation decision before approval? | **Architecture influence** |
| 5 | What percentage of AI initiatives are embedded into operational workflows with defined performance KPIs? | **AI maturity** |
| 6 | Who owns your top ten data products at business level, and what outcomes are they accountable for? | **Data ownership** |
| 7 | What is the cost of duplication across analytics tooling and data pipelines? | **Waste visibility** |
| 8 | Can you model the operational and financial impact of a strategic initiative before committing capital? | **Forecasting maturity** |
| 9 | What is the cycle time from strategy approval to architecture-informed execution readiness? | **Speed to value** |
| 10 | Which data domains are material to enterprise risk, and who holds decision rights over them? | **Risk governance** |
| 11 | How much of your architecture repository is actively used in executive investment decisions? | **Architecture utilization** |
| 12 | If asked to justify total technology and data spend in terms of enterprise value contribution, could you respond within one reporting cycle? | **Readiness** |

## Strong vs weak signals

| 🟢 Strong | 🔴 Weak |
|---|---|
| Answers backed by quantified metrics | Answers depend on narrative, not numbers |
| Funding mapped to business capabilities | Funding can't be mapped to capabilities |
| Architecture shapes investment timing | Architecture is advisory, not decision-shaping |
| AI embedded in operational workflows | AI can't demonstrate operational impact |

> **Key insight:** High-performing organizations don't *defend* architecture maturity. They *demonstrate* **value traceability**. Structural gaps are not resolved by better dashboards or another maturity assessment — they are resolved by redesigning how funding, accountability, and decision rights actually work.

## When to use this in this practice

- **Quarterly initiative review** — score every active archetype 1–5 on each question; identify which initiative closes the lowest-scoring gap.
- **Board / steering committee prep** — `defending-ai-spend-memo` skill auto-generates the 12-question scorecard for a given initiative portfolio.
- **CFO conversations** — Q1 + Q7 + Q9 are the questions a CFO asks; have answers ready.

## Cross-references

- `cdo-top-10-deliverables.md` — Deliverable 8 (Data Monetization) is what makes Q1 answerable.
- `../authored/ai-ready-platinum-layer.md` — gives Q5 a concrete answer ("how AI is embedded").
- `bain-3-layer-agentic.md` — provides the orchestration / observability / data layers that make Q3 (dependency mapping) tractable.
- `.claude/skills/defending-ai-spend-memo/SKILL.md` — auto-runs the 12 questions against the initiative registry.
