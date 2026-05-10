# From Contract to AI Consumption

> How the `ai_consumption` block in `data-contract.yml` becomes a runnable, agent-ready interface — including the auto-generated AI Consumption Contract markdown that the AI-Ready Platinum Layer (Principle 5) mandates.

## The flow

```
data-contract.yml
   ai_consumption:
     enabled: true
     answerable_questions: [...]
     scoped_views: [...]
     uc_functions: [...]
              |
              v
+--------------------------------------+
| src/pipelines/platinum.py            |
|   Reads ai_consumption.scoped_views  |
|   Registers DLT views in Platinum    |
+--------------------------------------+
              |
              v
+--------------------------------------+
| src/shared/unity_catalog_helpers.py  |
|   emit_uc_function_statements()      |
|   Generates CREATE FUNCTION skeletons|
+--------------------------------------+
              |
              v
+--------------------------------------+
| scripts/generate_ai_contract.py      |
|   Reads ai_consumption + metadata    |
|   Writes docs/ai-consumption-contract.md |
+--------------------------------------+
              |
              v
   AI Consumption Contract.md
   (Goes into the data product PRD)
```

## What an agent actually sees

When a Claude session (or AI/BI Genie) connects via MCP and discovers this data product:

1. **MCP Catalog** lists the scoped views by name + description.
2. The agent reads the **AI Consumption Contract markdown** to learn:
   - Which questions this product answers.
   - Which scoped views to query.
   - Which UC Functions to call for business-logic operations.
   - Freshness commitment.
   - Owner team for escalations.
3. The agent issues queries against the scoped views (5–8 columns each) instead of raw Gold tables.
4. UC ABAC enforces masking + row filters at query time — even if the agent constructs a query that *would* return PII, the masking function obscures it.

## Why scoped views matter

Wide BI tables are great for humans browsing in Power BI. Agents that try to read them:

- Get overwhelmed by columns and produce wrong SQL.
- Trip over PII unnecessarily.
- Generate queries that scan more data than needed.

Scoped views named for the questions they answer (`vw_account_activity_for_agents`) solve all three. The agent finds the view by name; the view excludes PII by construction; the query is small.

## Why UC Functions matter

Without UC Functions, business logic ("classify_amount_band" or "calculate_book_value") lives in the agent's prompt. That is fragile:

- Different agents drift.
- Updates require prompt changes everywhere.
- Audit asks "where did this number come from?" → no clean answer.

With UC Functions:

- One canonical implementation.
- Audit-traceable: every call logged at UC.
- Updates propagate automatically.
- Producer team owns the logic, not the agent.

## Editing the contract → regenerating

Whenever you update `ai_consumption` in `data-contract.yml`:

```bash
python scripts/generate_ai_contract.py \
    --contract data-contract.yml \
    --out docs/ai-consumption-contract.md
```

Commit the regenerated doc. CI re-runs the 6-check gate.

## Cross-references

- `../../ip/authored/ai-ready-platinum-layer.md` — the design principle this implements.
- `../../ip/curated/context-wall-meta-knowledge-graph.md` — Tekiner's argument for why metadata is the semantic layer.
- `../../ip/curated/bain-3-layer-agentic.md` — Bain's "Data + Knowledge" layer is what this fulfills.
