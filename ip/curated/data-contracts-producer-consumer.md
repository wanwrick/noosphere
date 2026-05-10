# Data Contracts as Producer-Consumer Interface

> **Source:** Tom Baeyens. LinkedIn post — *"Data contracts are the perfect interface between a data producer and a data consumer."*

## Core insight

Data contracts are the **API equivalent for data pipelines**. They make expectations explicit between producer and consumer. Without them: pipeline changes introduce breaking differences, misaligned expectations, and downstream failures. With them: both sides know what is promised and what is expected.

## The producer-consumer problem

| 🏭 Producer | 📊 Consumer |
|---|---|
| Changes pipelines to meet new requirements | Builds reports / models on assumptions |
| May rename columns, change types, alter logic | Assumptions often **undocumented** |
| Often unaware of downstream dependencies | Breaks silently when upstream changes |

**Without a contract:** changes introduce breaking differences. Nobody knows what broke or why.

## What a contract does

| Role | Responsibility |
|---|---|
| Consumer | Specifies the guarantees they depend on (schema, freshness, completeness, quality) |
| Producer | Takes responsibility for delivering data that conforms |
| Contract validation | Evaluates every dataset update against the published contract before release |

## Software APIs vs Data Contracts

| Concept | Software APIs | Data Contracts |
|---|---|---|
| Purpose | Strict interfaces between services | Strict interfaces between data pipelines |
| Benefit | Teams work independently without breaking each other | Producers and consumers evolve independently |
| Validation | Type checking at compile / runtime | Contract checks at every dataset update |
| Breaking changes | Versioned API, deprecation notice | Contract violation alerts before release |

## When to use this in this practice

- **Every new data product** — contract first, code second.
- **Multi-team consumption** — when 3+ consumers depend on a producer's table, the contract is non-negotiable.
- **Regulatory compliance** — audit-grade evidence of "what the consumer was promised."

## How it applies in this practice

The DABs Data-Contract Golden Path subproject (`templates/dabs-data-product-template/`) **operationalizes** this pattern. Its `data-contract.yml` schema is the formal contract; the bundle wires the contract into runtime enforcement (DLT expectations + UC ABAC + AI Consumption Contract).

The `metadata-driven-ingestion-framework.md` (Kocyigit) is the architectural cousin: same YAML-as-source-of-truth idea, applied to ingestion strategy choice.

## Cross-references

- `metadata-driven-ingestion-framework.md` — same YAML-driven pattern at the ingestion layer.
- `data-product-architecture-5-pillars.md` — Pillar 1 (Clear Boundaries) is what the contract formalizes.
- `dataplex-six-data-product-principles.md` — Principle 4 (Contractual guarantees) maps directly.
- `../authored/dabs-data-contract-golden-path.md` — the runnable subproject that ships this pattern.
