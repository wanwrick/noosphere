# Data Product Architecture — 5 Engineering Pillars + Quality Framework

> **Source:** Piotr Czarnas, data quality / governance expert. LinkedIn post on data product architecture. [Read it](https://www.linkedin.com/posts/piotr-czarnas_dataquality-dataengineering-datagovernance-activity-7433143575938355201-Leps).

## Core insight

Transitioning to a data product architecture **isn't rebranding your platform** — it's a fundamental redesign. True data products are born from bounded domains and designed around specific use cases. Data quality isn't a layer on top; it's an **emergent property** of sound engineering.

## The 5 Engineering Pillars

| # | Pillar | What it means | The hard part |
|---|---|---|---|
| 1 | **Clear Boundaries** | Define where a data product starts and ends — lock down inputs (sources) and outputs (interfaces / APIs) | This is your contract with the rest of the mesh |
| 2 | **Tangible ROI** | Calculate the return on rebuilding an existing pipeline into a standalone product | Hardest part of any refactoring — find new internal customers |
| 3 | **Scalable Infra** | Identify reusable components (service mesh, logging, metadata layer) so new products deploy without reinventing | Building a platform for many, not just one |
| 4 | **Standard Templates** | Every new product bootstraps from a standardized template — catalog registration and DQ checks automated | "How do I register this?" should never be a question |
| 5 | **Quality Framework** | Quality surrounds the product as an emergent property, not bolted on top | Requires all 4 pillars above to work |

## The Quality Framework

```
Data Contracts            ─────► Data Quality Standards
(precise format + I/O)            (freshness SLAs, volume SLAs)
       │                                    │
       └─────► Incident-driven Monitoring   │
              (auto-notify upstream/down)   │
                              │             ▼
                              └────► Standardized Quality Metrics
                                     (uniform calc + reporting)
```

Quality = emergent property of: contracts + standards + monitoring + metrics.

## When to use this in this practice

- **Pre-build review** — every new data product passes Pillars 1–4 before code is written.
- **Quality as architecture** — reframes DQ triage from "fix nulls" to "fix the architecture that produces nulls."
- **DABs Golden Path** — `templates/dabs-data-product-template/` operationalizes all 5 pillars.

## How it applies in this practice

| Pillar | Where it lives in this OS |
|---|---|
| 1 — Clear Boundaries | `data-contract.yml` `metadata.id` + `grain` + `consumed_by` |
| 2 — Tangible ROI | `initiatives/initiatives.yaml` `fee_tier_band` + initiative scorecard |
| 3 — Scalable Infra | `templates/dabs-data-product-template/src/shared/` reusable helpers |
| 4 — Standard Templates | The DABs Golden Path subproject IS the standard template |
| 5 — Quality Framework | `data-contract.yml` `quality_expectations[]` + Silver DLT decorators |

## Cross-references

- `data-contracts-producer-consumer.md` (Baeyens) — Pillar 1 implementation pattern.
- `metadata-driven-ingestion-framework.md` (Kocyigit) — Pillar 4 implementation pattern.
- `dabs-custom-templates.md` (Shi) — Pillar 4 tooling.
- `../authored/dabs-data-contract-golden-path.md` — operationalizes all five pillars in one runnable subproject.
