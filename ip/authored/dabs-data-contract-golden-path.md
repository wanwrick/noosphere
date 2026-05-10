# DABs Data-Contract Golden Path

> The flagship deliverable. A real, working, forkable Databricks Asset Bundle subproject that turns a single `data-contract.yml` into a contract-enforcing pipeline. Not docs about a pattern — *the pattern*, runnable.

**Subproject location:** `templates/dabs-data-product-template/`

## What it is

A complete DABs template project. Clone it, fill in `data-contract.yml`, run two commands, get a deployable pipeline. The `data-contract.yml` declares everything; the bundle wires the contract into Bronze ingestion, Silver DLT expectations, Gold transformations, Platinum AI-ready views, Unity Catalog ABAC, and CI/CD validation.

## Why this is the load-bearing artifact

This subproject is the answer to "ready-to-play for data teams." It operationalizes six named methodologies in one runnable package:

1. **No LAC (authored)** — the architecture pattern the subproject implements.
2. **AI-Ready Platinum Layer (authored)** — the Platinum scoped views and UC Functions are auto-generated from the contract's `ai_consumption` section.
3. **Data Contracts as Producer-Consumer Interface (Baeyens)** — the `data-contract.yml` schema formalizes the producer-consumer interface.
4. **Data Product Architecture: 5 Engineering Pillars (Czarnas)** — the subproject embodies clear boundaries, ROI through reuse, scalable infra, standard templates, and emergent quality.
5. **Metadata-Driven Lakehouse Ingestion Framework (Kocyigit, OSS)** — direct architectural inspiration: YAML metadata as single source of truth.
6. **DABs Custom Templates + DABs CI/CD (Shi)** — `databricks bundle init` pattern + `bundle validate` / `bundle deploy` discipline.

## How the contract flows

```
data-contract.yml  (single source of truth)
       |
       +-- bronze.ingestion_strategy --> Bronze pipeline (snapshot/incremental/cdc)
       +-- schema.columns[]            --> Bronze explicit schema + UC tags + masking
       +-- quality_expectations[]      --> Silver DLT @expect / @expect_or_drop / @expect_or_fail
       +-- freshness.sla_minutes       --> Silver freshness expectation
       +-- metadata.classification     --> UC permissions + ABAC grants
       +-- metadata.owner_team         --> ownership tags + alerting routes
       +-- ai_consumption.scoped_views --> Platinum views + UC Function registration
       +-- ai_consumption.uc_functions --> Governed callable logic for agents
       |
       +-- generate_ai_contract.py     --> AI Consumption Contract markdown
       +-- validate_bundle.sh          --> 6-check CI/CD gate
```

See `templates/dabs-data-product-template/docs/how-the-contract-flows.md` for the full ASCII diagram and `_Diagrams/dabs-contract-flow.md` for the Mermaid version.

## What the subproject ships

| Folder | Contents |
|---|---|
| `data-contract.yml` + `data-contract.schema.json` | The contract + its JSON Schema validator |
| `databricks.yml` + `resources/` | Bundle config + per-resource YAML |
| `src/contract/` | Contract loader · schema check · freshness check · quality check · AI contract generator |
| `src/pipelines/` | Bronze · Silver · Gold · Platinum scaffolds |
| `src/shared/` | Medallion helpers · UC helpers · ingestion strategies |
| `tests/` | Unit tests on each contract check + integration test on bundle validation |
| `scripts/` | `validate_bundle.sh` · `deploy.sh` · `generate_ai_contract.py` |
| `.github/workflows/` | CI (lint + test + bundle validate) + Deploy on merge |
| `docs/` | 4 walkthrough docs (contract flow · extending · contract-to-AI · golden-path-walkthrough) |
| `examples/` | Worked example: incremental-CDC ingestion with PII masking + AI consumption |

## Six checks in `validate_bundle.sh`

1. Bundle syntax valid.
2. `data-contract.yml` valid against `data-contract.schema.json`.
3. Every PII column carries a `masking_function`.
4. `freshness.sla_minutes` defined.
5. `quality_expectations[]` non-empty.
6. `metadata.owner_team` and `metadata.classification` non-null.

## Fork-and-deploy flow

```
git clone <your-fork>/noosphere
cp -r templates/dabs-data-product-template/ ../<your-platform-repo>/data-product-<name>/
cd ../<your-platform-repo>/data-product-<name>/
# Edit data-contract.yml
databricks bundle validate
pytest tests/
databricks bundle deploy --target dev
```

End state: a contract-enforcing data product live in dev, ready to promote.

## Cross-references

- `templates/dabs-data-product-template/README.md` — operational README of the subproject.
- `templates/dabs-data-product-template/docs/golden-path-walkthrough.md` — 30-minute fork-to-running guide.
- `templates/dabs-data-product-template/docs/from-contract-to-ai-consumption.md` — how AI Consumption Contracts are auto-generated.
- `no-lac-principle.md` — the architectural commitment this subproject implements.
- `ai-ready-platinum-layer.md` — the metadata rubric that Platinum views satisfy.
- `../curated/data-contracts-producer-consumer.md` — the contract pattern this formalizes.
- `../curated/metadata-driven-ingestion-framework.md` — the YAML-as-source-of-truth approach.

---

*Owned by: producer team's platform engineering lead. Forked + extended per project.*
