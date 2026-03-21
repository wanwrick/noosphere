# QuestBank Playbooks — Critical Frameworks

> Snapshotted from Notion Work Hub for offline portability. For the latest version, fetch from Notion using the page IDs below.

---

## 1. Data Source Onboarding — 10Q Framework

**Notion Source:** `8573e91d79a24e43a90aadcba0c06696`

The 10Q framework captures the 10 dimensions every new data source must be assessed against before onboarding into the lakehouse.

### The 10 Questions

| # | Dimension | What to Assess | Cost Lever |
|---|-----------|---------------|------------|
| 1 | **Volume** | Row counts, file sizes, growth rate | Compute sizing, storage |
| 2 | **Freshness** | How often does data change? SLA for availability | Batch vs. streaming decision |
| 3 | **Schema** | Stability, complexity, nested structures | Schema evolution strategy |
| 4 | **Quality** | Known issues, null rates, referential integrity | DQ rules in Silver layer |
| 5 | **Source Type** | API, file drop, CDC, database extract | Ingestion pattern selection |
| 6 | **Incremental** | Can we detect changes? Watermark column? | Full vs. incremental load |
| 7 | **PII** | Personal data fields, sensitivity classification | ABAC masking, PIPEDA compliance |
| 8 | **Rate Limits** | API throttling, extraction windows | Scheduling, parallelism |
| 9 | **Replay** | Can we re-extract historical data? | Recovery strategy, backfill |
| 10 | **Gotchas** | Timezone issues, encoding, undocumented behavior | Risk mitigation |

### Usage Pattern
- **Before onboarding:** Run 10Q interview with the source team
- **Output:** Completed 10Q assessment feeds into pipeline design decisions
- **Maps to:** Bronze layer ingestion config + Silver layer DQ expectations

---

## 2. CDO Top 10 Deliverables

**Notion Source:** `3017b88e336f810182dced261d72ad47`

Enterprise data strategy framework identifying the 10 deliverables every Chief Data Officer must own. Mapped to QuestBank's current state.

### The 10 Deliverables

| # | Deliverable | QuestBank Status | Owner |
|---|-------------|-----------------|-------|
| 1 | **Data Strategy & Roadmap** | ✅ Active — Q1 roadmap live | Paroz |
| 2 | **Data Governance Framework** | ✅ Active — Unity Catalog + ABAC | Paroz + Platform |
| 3 | **Data Quality Management** | ✅ Active — DLT expectations | DataWizards |
| 4 | **Master Data Management** | 🟡 In progress — shared dimensions | DataWizards |
| 5 | **Metadata Management** | 🟡 In progress — catalog descriptions | DataWizards |
| 6 | **Data Architecture** | 🟡 In progress — Medallion + Mesh | Paroz + Bart |
| 7 | **Data Literacy & Self-Serve** | 🔴 Gap — planned for Q2 | Paroz |
| 8 | **Data Monetization** | 🔴 Gap — future state | TBD |
| 9 | **Privacy & Compliance** | ✅ Active — PIPEDA/OFSI | Paroz + Shabi |
| 10 | **Data Culture & Change Mgmt** | 🔴 Gap — needs executive sponsorship | Paroz |

### Strategic Insight
- **3 active, 3 in-progress, 3 gaps** — prioritize gaps by business impact
- Deliverables 7 (Self-Serve) and 10 (Culture) are the highest-leverage gaps
- Use this framework to position QuestBank as a strategic asset to leadership

---

## 3. Data Contracts — Producer-Consumer Interface

**Notion Source:** `3057b88e336f819b8869ec95d5102e4e`

Data Contracts define the interface between data producers and consumers. They formalize what data will look like, when it will arrive, and what quality guarantees it carries.

### Contract Components

| Component | What It Defines | Example |
|-----------|---------------|---------|
| **Schema** | Column names, types, nullability | `account_id: STRING NOT NULL` |
| **Freshness SLA** | Max acceptable latency | "Available within 2 hours of source update" |
| **Quality Rules** | Data quality expectations | `amount IS NOT NULL AND amount != 0` |
| **Completeness** | Expected row counts, coverage | "All active accounts, ≥99.5% complete" |
| **Ownership** | Producer team, consumer team, steward | Producer: DataWizards, Consumer: BI Team |
| **Versioning** | How breaking changes are managed | Semantic versioning, deprecation notices |

### Contract Lifecycle
```
1. Define   → Producer and consumer agree on contract terms
2. Validate → Automated checks run on every pipeline execution
3. Monitor  → Freshness and quality tracked against SLA
4. Alert    → Breaches trigger notifications to both parties
5. Evolve   → Version bumps for schema changes, migration window
```

### Implementation in QuestBank
- **Bronze → Silver boundary** is where contracts are enforced
- DLT expectations implement the quality rules
- Unity Catalog tags implement ownership and classification
- Freshness monitored via pipeline observability (Notion: `6ea336980e6d49f4b4913dc0d56a832a`)

### When to Use
- Onboarding a new data source (pair with 10Q)
- A consumer reports data quality issues
- Cross-team data sharing agreements
- Regulatory audit preparation (audit trail from contract to enforcement)

---

## Cross-Reference: How the 3 Frameworks Connect

```
New Source Request
    │
    ▼
10Q Assessment ──────► Pipeline Design Decisions
    │                        │
    │                        ▼
    │              Data Contract Definition
    │                        │
    │                        ▼
    │              Bronze → Silver Pipeline
    │              (DLT + Expectations)
    │                        │
    ▼                        ▼
CDO Deliverables    Gold Layer (Business-Ready)
(Strategy Alignment)        │
                            ▼
                  Consumer Self-Serve
```

---

*Snapshotted: 2026-03-07 | For live versions, fetch from Notion using page IDs above*
