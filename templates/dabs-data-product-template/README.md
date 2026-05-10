# DABs Data-Contract Golden Path Template

> The flagship deliverable of the Noosphere Practice OS. A real, working, forkable Databricks Asset Bundle that turns one `data-contract.yml` into a contract-enforcing pipeline.

## What this gives you

Clone this directory into your platform repo. Fill in `data-contract.yml`. Run two commands. You get:

- A Bronze pipeline parameterized by `bronze.ingestion_strategy` (snapshot · incremental · CDC).
- A Silver pipeline that applies DLT expectations from `quality_expectations[]`.
- Unity Catalog tags, masking functions, and ABAC grants generated from the contract metadata.
- A Platinum layer with question-oriented scoped views + UC Functions auto-generated from `ai_consumption.*`.
- An AI Consumption Contract markdown doc auto-generated from the contract.
- A 6-check `validate_bundle.sh` CI/CD gate.
- GitHub Actions for `bundle validate` on PR + `bundle deploy` on merge.

## Quick start

```bash
# 1. Copy the template into your repo
cp -r noosphere/templates/dabs-data-product-template/ \
      <your-platform-repo>/data-products/<product-name>/

cd <your-platform-repo>/data-products/<product-name>/

# 2. Fill in the contract
$EDITOR data-contract.yml

# 3. Validate locally
pip install -r requirements.txt
pytest tests/unit/                                    # contract unit tests
bash scripts/validate_bundle.sh                       # 6-check gate
databricks bundle validate                            # bundle config OK

# 4. Generate the AI Consumption Contract section
python scripts/generate_ai_contract.py \
    --contract data-contract.yml \
    --out docs/ai-consumption-contract.md

# 5. Deploy
databricks bundle deploy --target dev
databricks bundle run <pipeline_name> --target dev
```

## What lives where

```
templates/dabs-data-product-template/
├── data-contract.yml             ← The contract (single source of truth)
├── data-contract.schema.json     ← JSON Schema validating the contract
├── databricks.yml                ← Bundle config; references contract
├── databricks-template-schema.json   Bundle-init parameter schema
│
├── resources/
│   ├── pipeline.yml              ← DLT pipeline (parametrized)
│   ├── job.yml                   ← Orchestration job
│   ├── permissions.yml           ← UC ABAC grants
│   └── schema.yml                ← UC schema + tags
│
├── src/
│   ├── contract/                 ← Parses + validates + checks the contract
│   ├── pipelines/                ← Bronze · Silver · Gold · Platinum scaffolds
│   └── shared/                   ← Reusable helpers
│
├── tests/
│   ├── unit/                     ← Per-module unit tests
│   ├── integration/              ← Bundle-level integration smoke
│   └── fixtures/                 ← Valid + invalid contracts
│
├── scripts/
│   ├── validate_bundle.sh        ← 6-check CI/CD gate
│   ├── deploy.sh                 ← bundle validate + deploy
│   ├── generate_ai_contract.py   ← Produces AI Consumption Contract doc
│   └── lint_sanitization.sh      ← Inherits from parent repo
│
├── .github/workflows/
│   ├── ci.yml                    ← lint + test + bundle validate on PR
│   └── deploy.yml                ← bundle deploy on merge
│
├── docs/
│   ├── how-the-contract-flows.md
│   ├── extending-the-template.md
│   ├── from-contract-to-ai-consumption.md
│   └── golden-path-walkthrough.md
│
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md                     ← This file
```

## The 6-check gate

Run `bash scripts/validate_bundle.sh`. It fails fast if any of:

1. Bundle YAML syntax invalid.
2. `data-contract.yml` invalid against `data-contract.schema.json`.
3. Any column with `pii: true` lacks a `masking_function`.
4. `freshness.sla_minutes` not defined.
5. `quality_expectations[]` empty.
6. `metadata.owner_team` or `metadata.classification` null.

## How the contract flows

See `docs/how-the-contract-flows.md` for the full diagram. Short version:

```
data-contract.yml
   ↓ (parsed by src/contract/loader.py)
   ├─ schema.columns[]            → Bronze explicit schema + UC tags + masking
   ├─ bronze.ingestion_strategy   → Bronze pipeline (Auto Loader / JDBC / Streaming / CDC)
   ├─ quality_expectations[]      → Silver DLT @expect / @expect_or_drop / @expect_or_fail
   ├─ freshness.sla_minutes       → Silver freshness expectation
   ├─ metadata.classification     → UC permissions in resources/permissions.yml
   ├─ ai_consumption.scoped_views → Platinum question-oriented views
   ├─ ai_consumption.uc_functions → UC Functions registered for agents
   └─ ai_consumption.*            → docs/ai-consumption-contract.md (via scripts/)
```

## Customizing for your stack

| Stack signal | What changes |
|---|---|
| Snowflake instead of Databricks | Replace `resources/pipeline.yml` with dbt models; replace `databricks.yml` with `dbt_project.yml`. Contract YAML stays unchanged. |
| AWS instead of GCP | Update `databricks.yml` workspace hosts; UC works identically. |
| HIPAA / SOX / SOC 2 instead of OSFI-style | Update `metadata.classification` taxonomy and the `compliance-checker` skill in `.claude/skills/`. |
| Without Unity Catalog | Strip `resources/permissions.yml` and `src/shared/unity_catalog_helpers.py`; classification/masking become application-layer concerns. |

## Cross-references

- `../../ip/authored/dabs-data-contract-golden-path.md` — the IP doc explaining the pattern.
- `../../ip/authored/no-lac-principle.md` — the architectural commitment.
- `../../ip/authored/ai-ready-platinum-layer.md` — the Platinum layer rubric.
- `../../ip/curated/data-contracts-producer-consumer.md` — Baeyens's contract pattern (curated source).
- `../../ip/curated/metadata-driven-ingestion-framework.md` — Kocyigit's architectural inspiration.

## License

MIT (inherits from parent repo).
