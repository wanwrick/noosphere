# [Platform Name] Playbooks: Critical Frameworks

> **Template note:** These playbooks are examples from a data engineering context. Replace with your own team's operational frameworks and SOPs.

> Snapshotted from Notion Work Hub for offline portability. For the latest version, fetch from Notion using the page IDs below.

---

## 1. Data Source Onboarding: 10Q Framework

**Notion Source:** `your-notion-page-id-here`

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
| 7 | **PII** | Personal data fields, sensitivity classification | ABAC masking, [Privacy Regulation] compliance |
| 8 | **Rate Limits** | API throttling, extraction windows | Scheduling, parallelism |
| 9 | **Replay** | Can we re-extract historical data? | Recovery strategy, backfill |
| 10 | **Gotchas** | Timezone issues, encoding, undocumented behavior | Risk mitigation |

### Usage Pattern
- **Before onboarding:** Run 10Q interview with the source team
- **Output:** Completed 10Q assessment feeds into pipeline design decisions
- **Maps to:** Bronze layer ingestion config + Silver layer DQ expectations

---

## 2. CDO Top 10 Deliverables

**Notion Source:** `your-notion-page-id-here`

Enterprise data strategy framework identifying the 10 deliverables every Chief Data Officer must own. Mapped to your platform's current state.

### The 10 Deliverables

| # | Deliverable | Current Status | Owner |
|---|-------------|---------------|-------|
| 1 | **Data Strategy & Roadmap** | [Status] | [Your Name] |
| 2 | **Data Governance Framework** | [Status] | [Your Name] + Platform |
| 3 | **Data Quality Management** | [Status] | [Team Name] |
| 4 | **Master Data Management** | [Status] | [Team Name] |
| 5 | **Metadata Management** | [Status] | [Team Name] |
| 6 | **Data Architecture** | [Status] | [Your Name] + [Partner 2] |
| 7 | **Data Literacy & Self-Serve** | [Status] | [Your Name] |
| 8 | **Data Monetization** | [Status] | TBD |
| 9 | **Privacy & Compliance** | [Status] | [Your Name] + [Team Member 2] |
| 10 | **Data Culture & Change Mgmt** | [Status] | [Your Name] |

### Strategic Insight
- Prioritize gaps by business impact
- Self-Serve and Culture are typically the highest-leverage gaps
- Use this framework to position your data platform as a strategic asset to leadership

---

## 3. Data Contracts: Producer-Consumer Interface

**Notion Source:** `your-notion-page-id-here`

Data Contracts define the interface between data producers and consumers. They formalize what data will look like, when it will arrive, and what quality guarantees it carries.

### Contract Components

| Component | What It Defines | Example |
|-----------|---------------|---------|
| **Schema** | Column names, types, nullability | `account_id: STRING NOT NULL` |
| **Freshness SLA** | Max acceptable latency | "Available within 2 hours of source update" |
| **Quality Rules** | Data quality expectations | `amount IS NOT NULL AND amount != 0` |
| **Completeness** | Expected row counts, coverage | "All active accounts, >=99.5% complete" |
| **Ownership** | Producer team, consumer team, steward | Producer: [Team Name], Consumer: BI Team |
| **Versioning** | How breaking changes are managed | Semantic versioning, deprecation notices |

### Contract Lifecycle
```
1. Define   -> Producer and consumer agree on contract terms
2. Validate -> Automated checks run on every pipeline execution
3. Monitor  -> Freshness and quality tracked against SLA
4. Alert    -> Breaches trigger notifications to both parties
5. Evolve   -> Version bumps for schema changes, migration window
```

### Implementation in [Platform Name]
- **Bronze to Silver boundary** is where contracts are enforced
- DLT expectations implement the quality rules
- Unity Catalog tags implement ownership and classification
- Freshness monitored via pipeline observability (Notion: `your-notion-page-id-here`)

### When to Use
- Onboarding a new data source (pair with 10Q)
- A consumer reports data quality issues
- Cross-team data sharing agreements
- Regulatory audit preparation (audit trail from contract to enforcement)

---

## Cross-Reference: How the 3 Frameworks Connect

```
New Source Request
    |
    v
10Q Assessment -------> Pipeline Design Decisions
    |                        |
    |                        v
    |              Data Contract Definition
    |                        |
    |                        v
    |              Bronze -> Silver Pipeline
    |              (DLT + Expectations)
    |                        |
    v                        v
CDO Deliverables    Gold Layer (Business-Ready)
(Strategy Alignment)        |
                            v
                  Consumer Self-Serve
```

---

*Snapshotted: [Date] | For live versions, fetch from Notion using page IDs above*
