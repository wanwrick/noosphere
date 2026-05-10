# Golden Path Walkthrough — Fork to Running in 30 Minutes

> Step-by-step walkthrough for a data team adopting this template. Assumes you have a Databricks workspace, the Databricks CLI installed, and a Python ≥3.10 environment.

## Step 0 — Prereqs

- Databricks CLI installed: `curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh`
- Auth configured: `databricks auth login --host https://<your-workspace>`
- Python 3.10+
- `git`

## Step 1 — Copy the template into your platform repo (3 min)

```bash
git clone https://github.com/wanwrick/noosphere.git
cp -r noosphere/templates/dabs-data-product-template/ \
      <your-platform-repo>/data-products/<product-name>/
cd <your-platform-repo>/data-products/<product-name>/
git add . && git commit -m "feat(data-product): scaffold from DABs Data-Contract Golden Path"
```

## Step 2 — Fill in the contract (10 min)

Open `data-contract.yml`. Replace the example values with your own data product's:

- `metadata.id` — slug for table-name prefix.
- `metadata.name` + `description` — human-readable summary.
- `metadata.owner_team` — codename of the team owning this product.
- `metadata.classification` — public · internal · confidential · restricted.
- `grain.description` — one row per *what*?
- `bronze.source_type` + `ingestion_strategy` — files / database / api / kafka / saas; snapshot / incremental / cdc.
- `schema.columns[]` — every column. Mark PII columns with `pii: true` and a `masking_function`.
- `freshness.sla_minutes` — your committed SLA.
- `quality_expectations[]` — at least three: pk-not-null, business-rule, completeness.
- `ai_consumption.*` — fill if agents will read this product (recommended).

## Step 3 — Validate locally (5 min)

```bash
pip install -r requirements.txt
pytest tests/unit/ -v
bash scripts/validate_bundle.sh
databricks bundle validate
```

All four must succeed before proceeding.

## Step 4 — Generate the AI Consumption Contract (1 min)

```bash
python scripts/generate_ai_contract.py \
    --contract data-contract.yml \
    --out docs/ai-consumption-contract.md
```

Review the generated doc. If `ai_consumption.enabled: true`, this becomes the contract for any agent reading the product.

## Step 5 — Deploy to dev (5 min)

```bash
bash scripts/deploy.sh dev
databricks bundle run data_product_pipeline --target dev
```

Watch the DLT run in the Databricks UI. Confirm Bronze/Silver/Gold/Platinum tables populate.

## Step 6 — Verify governance applied (3 min)

In a Databricks SQL editor:

```sql
-- Confirm column tags
DESCRIBE TABLE EXTENDED dev.<your-id>.<your-id>_silver;

-- Confirm masking on PII columns
SELECT * FROM dev.<your-id>.<your-id>_silver LIMIT 10;
-- PII columns should show masked output unless you're in the cleared group
```

## Step 7 — Wire the GitHub Actions (3 min)

Set repository secrets:
- `DATABRICKS_HOST_DEV`, `DATABRICKS_HOST_STAGING`, `DATABRICKS_HOST_PROD`
- `DATABRICKS_TOKEN`

Push to your branch. Open a PR. The CI workflow runs `pytest` + `validate_bundle.sh` + `bundle validate`. Merge to main triggers `deploy.yml` to dev.

## Done.

You now have:
- A contract-enforcing data product pipeline running in dev.
- An AI Consumption Contract documenting how agents should consume it.
- CI/CD that fails fast on contract violations.

To promote: re-run `bash scripts/deploy.sh staging` after staging signoff, then `prod`.

## Next steps

- Adapt `src/pipelines/gold.py` to your domain logic (the only place custom code is allowed).
- Add domain-specific UC Functions if the contract declares them.
- Add `docs/extending-the-template.md` content for your team's idiomatic patterns.
- Reference the Authored IP files in this repo when explaining the *why* in design reviews.
