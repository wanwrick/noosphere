# Paroz's Work Goals & Priorities

## Current Role Context

**Technical Product Manager — Data Engineering & BI**
Questrade Financial Group | DataWizards Team

Leading the build-out of QuestBank, an enterprise data lakehouse on Databricks that serves analytics, regulatory reporting, and machine learning across the organization. Producer team lead in a Data Mesh strategy — owns ingestion and transformation.

## Strategic Priorities

### P0 — QuestBank Platform Delivery
- Complete Medallion Architecture build (Bronze → Silver → Gold → Platinum)
- Deliver Temenos core banking integration on schedule
- Achieve Unity Catalog governance across all data domains
- Enable self-serve analytics via Power BI DirectQuery
- Meet OFSI/PIPEDA regulatory compliance requirements

### P1 — Team Growth & Excellence
- Develop 5 data engineers into autonomous domain experts
- Establish DataWizards as the go-to data platform team at Questrade
- Build Agile maturity — clean sprints, reliable velocity, quality stories
- Create a culture of documentation-first, async-first collaboration

### P2 — Stakeholder Influence & Executive Visibility
- Strengthen relationships with VP Engineering, VP Product, CTO
- Translate technical platform work into business value narratives
- Build a coalition of internal champions for the data platform
- Position QuestBank as a strategic asset, not a cost center

### P3 — Post-MBA Application
- Apply EMBA frameworks systematically to real work challenges
- Use financial analysis skills for business cases and ROI modeling
- Leverage strategy frameworks for competitive positioning of the platform
- Apply leadership models to team development and organizational influence

## Key Metrics I Track

| Metric | Target | Cadence |
|--------|--------|---------|
| Sprint velocity | Stable ±10% | Bi-weekly |
| Platform uptime | 99.9% | Daily |
| Data quality score | >95% | Weekly |
| Stakeholder satisfaction | >4/5 | Quarterly |
| Team engagement | High | Monthly pulse |
| Pipeline delivery vs plan | >85% on-time | Monthly |

## Decision Principles

1. **Customer value first** — Does this serve the end user (analyst, regulator, data scientist)?
2. **Build for scale** — Will this work at 10x the current load?
3. **Reduce technical debt** — Every sprint should leave the codebase better than we found it
4. **Document everything** — Future Paroz (and the team) will thank present Paroz
5. **Speed over perfection** — Ship the 80% solution, iterate from feedback

## Q1 2026 Initiatives (Live from Work Hub)

These are the active initiatives from the Notion Work Hub. For live status, query the Q1 Initiatives database (`684aa911db824338b94291fe4c6266d3`).

| # | Initiative | Status | Key Focus |
|---|-----------|--------|-----------|
| 1 | **Data Platform & Access Management** | 🟡 In progress | Platform hardening, ABAC rollout, access provisioning |
| 2 | **Marketing Modernization — Braze** | 🔴 Not started | Martech data integration, campaign analytics pipeline |
| 3 | **Self-Serve Provisioning** | 🔴 Not started | Automated workspace/table provisioning for consumers |
| 4 | **Self-Serve Analytics & Semantic Layer** | 🔴 Not started | Semantic modeling, metric views, Power BI optimization |
| 5 | **DW Modernization: CorpBI → GCP** | 🔴 Not started | Legacy warehouse migration planning |

### Initiative-to-Priority Mapping
- Initiative 1 → P0 (Platform Delivery)
- Initiative 2 → P0 (New data domain onboarding — use 10Q framework)
- Initiative 3 → P1 (Self-serve infrastructure for Data Mesh)
- Initiative 4 → P2 (Stakeholder value — self-serve analytics)
- Initiative 5 → P0 (Platform modernization)

### Active Workstreams (as of Mar 20, 2026)

| Workstream | Owner | Status | Key Blocker |
|-----------|-------|--------|-------------|
| PII Classification + Masking (QB-9079) | Mariano + Nilanjana | In progress — 5-step sequence; Phase 1 (immediate protection) running now | Nilanjana needs Databricks admin access; Fran/Mauro needed for managed tags |
| Keystone Reports (Finance) | Aman + Zoya + Sohail | 3 reports built; MTG issue resolving; validation by Mar 25 | MTG mapping bug being fixed; Sohail sign-off pending |
| IntelliFi Credit Risk Data (Databricks) | Paroz + Yelena (return) | VPC + shared cluster blocker; data not visible to credit risk team | VPC service controls + cluster issues; target fix Mar 23 |
| Temenos Production Validation | Lian + Lucas | Validation checklist in progress; KT sessions to Lucas's team | RBC account mappings missing from Treasury; many validations require live data |
| Sprint 5 Pipeline Reliability (QB-6553) | Gabriel + Yelena + Hayk + Ljupco | DLT alerting, quarantine pattern, Pub/Sub ordering | Yelena recovering from leave; Gabriel overloaded with critical path items |
| Data Governance Framework (Phase 2) | Mariano + Nilanjana + Cam | Repeatable automated classification/masking framework | Focus sessions with Databricks (Monty) being arranged; dependent on Phase 1 completion |
| Databricks Cluster Incident Post-Mortem | Paroz + Gabriel + Fran | Post-mortem scheduled; fix verified; communication to business sent | Cost impact: ~$4,000-5,000; cluster tagging deferred until post-bank-launch |
| Braze / Martech Integration | Martech Force | Not started | Dependency on platform hardening |

### Key Dates

- **Mar 23** — IntelliFi data stabilization in Databricks for credit risk team (Paroz target)
- **Mar 25** — Sprint S5 ends; Keystone reports internal validation complete; TDA-Databricks connectivity validated
- **Mar 26** — Engineering workshop (Databricks dashboards, access model)
- **Apr 2** — Keystone reports external communication to finance stakeholders
- **Apr 6** — **QuestBank bank product go-live** (Temenos production launch — HARD DATE)
- **Mid-April** — Expected org restructuring announcement (Adam's producer/consumer split)
- **Early May** — Mortgage product validation (funded loans hit Temenos)

### Active Blockers

1. **VPC service controls:** IntelliFi data not visible to credit risk team in Databricks; networking issue with 2 vendors involved
2. **GCP serverless private endpoint:** Not available; forces shared cluster dependency (shared clusters on PCI endpoint by end of March/mid-April)
3. **RBC account mappings:** Treasury hasn't provided mappings needed for Temenos production validation
4. **Org restructuring uncertainty:** Adam planning 40-45 to ~25 person reorganization; DataWizards team structure uncertain; Paroz's role in flux
5. **Gabriel + Yelena overloaded:** Both own the most critical-path S5 items; risk of sprint slip

### Critical Context: Org Restructuring
- Adam Neus planning producer/consumer data mesh split
- QTG shrinking from 40-45 to ~25 people; 15-20 moving to bank
- Geneviève building new bank-side data science and analytics team (reports to John Gallagher)
- Timeline: ~4 weeks from March 18 (mid-April)
- Paroz most likely stays on producer side; should reach out to Geneviève via Slack to explore options
- DataWizards team may be partially "harvested" to bank side

### Upcoming Work Preparation
Paroz is preparing to improve the ingestion system at work. Key Notion resources for this:
- Metadata-Driven Ingestion Framework (`3127b88e336f8161ac87f6e2499659ae`)
- Data Contracts (`3057b88e336f819b8869ec95d5102e4e`)
- Data Source Onboarding 10Q (`8573e91d79a24e43a90aadcba0c06696`)
- Data Modeling for Modern Lakehouse (`2d27b88e336f81cdb19cdd784a1f0efe`)
- Semantic Modeling in Databricks (`3027b88e336f810fa9fdc963c26213d6`)

### Cross-References (v1.3.0 Strategy Files)
- [Q1 Strategy & SPA](Knowledge/Work/q1-strategy.md) — Adam's 5-initiative portfolio with ~23 FTE
- [Access Management Framework](Knowledge/Work/access-management.md) — Three-pillar access model (WHO/WHAT/ASSIGNMENT)
- [Data Mesh Vision](Knowledge/Work/data-mesh-vision.md) — Decentralized ownership, consumer-first, quality economics
- [Q1 Strategic Decisions](Knowledge/Decisions/2026-q1-strategic-decisions.md) — 6 ratified decisions shaping execution

## How to Use This File

- **Claude:** Read this file first on every interaction to understand current priorities
- **Paroz:** Update quarterly focus areas at the start of each quarter
- **Decision filter:** When prioritizing, check if work aligns with P0-P3 hierarchy
- **Initiative context:** For live status, query Notion rather than relying on this snapshot
