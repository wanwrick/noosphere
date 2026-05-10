# AI Consumption Contract — Template

> Section to include in every data-product PRD where AI agents are consumers. **Auto-generated** by `templates/dabs-data-product-template/scripts/generate_ai_contract.py` from the `data-contract.yml`'s `ai_consumption` block. Do not hand-edit; update the contract YAML and regenerate.

---

## AI Consumption Contract — [Data Product Name]

**Owner team:** `[owner_team]` · **Steward:** `[steward]` · **Classification:** `[classification]` · **Version:** `[version.current]`

### Answerable questions

The following questions are contractually answerable from this data product:

- "[question 1]"
- "[question 2]"
- "[question 3]"

Questions not in this list are **out of scope** for AI agents until the contract is updated.

### Scoped views

| Name | Grain | Columns | Purpose |
|---|---|---|---|
| `vw_[name]_for_agents` | one row per [grain] | [columns] | [description] |

Agents must query the scoped views, not the underlying Gold tables.

### UC Functions

| Name | Logic | Governance |
|---|---|---|
| `[function_name]` | [logic_summary] | [governance_owner] |

Business logic operations (classifications, calculations) must call the UC Functions, not embed in agent prompts.

### Freshness commitment

- **SLA:** [N] minutes ([measurement basis])

If freshness exceeds SLA, agents must surface the lag in their answer ("data as of [timestamp]") rather than answer authoritatively.

### Metadata coverage

- **Grain:** [grain.description]
- **Time coverage:** [populate from registry]
- **Currency / units:** [populate from column descriptions]
- **Out of scope:** [populate before agent consumption begins]

The 6-question rubric (per `ip/authored/ai-ready-platinum-layer.md`) must be 100% filled before an agent can consume this product in production.

### Consumed by

- AI agents: [list]
- BI tools: [list]

### Change management

- Contract version bumps follow `data-contract.yml metadata.version` — semantic versioning.
- Breaking changes require approval per `metadata.version.breaking_changes_require`.
- Deprecation window: `metadata.version.deprecation_window_days` days before removal.

---

*Auto-generated from `data-contract.yml`. Do not hand-edit; update the contract and regenerate via `scripts/generate_ai_contract.py`.*
