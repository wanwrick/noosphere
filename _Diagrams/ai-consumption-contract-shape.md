# AI Consumption Contract — Shape

> What an AI Consumption Contract looks like in practice. ER-style: agent ↔ Platinum view ↔ governance.

```mermaid
erDiagram
    AGENT ||--o{ CONTRACT : signs
    PLATINUM_VIEW ||--o{ CONTRACT : grants
    GOVERNANCE ||--o{ CONTRACT : audits

    AGENT {
        string agent_id
        string consumption_pattern
        string use_case
        string owner
    }

    PLATINUM_VIEW {
        string view_name
        string grain
        string freshness_sla
        string masking_applied
    }

    CONTRACT {
        string contract_id
        date refresh_date
        string principle_1_semantic_clarity
        string principle_2_joinability
        string principle_3_consumption_shape
        string principle_4_masked_at_source
        string principle_5_observable
    }

    GOVERNANCE {
        string register_row_id
        bool dpia_completed
        string classification_tier
        string retention_obligation
    }
```

**Source IP:** `ip/authored/ai-ready-platinum-layer.md` · `data-products/ai-consumption-contract-template.md`. **Skill:** `ai-consumption-contract`.
