# Q1 2026 Strategic Priority Alignment (SPA)

> Adam Neus's Q1 2026 strategic framework: 5 initiatives, ~23 FTE, anchored on QuestBank launch and governed data access. This is THE cross-reference document for all Q1 work.

**Notion Sources:**
- Adam Dec 29 Discussion: `2d87b88e336f80bfa79ffcee1d0b3bd3`
- Initiative Page (Executive): `684aa911db824338b94291fe4c6266d3`
- Work Hub: `0581c312a23d465eb1b9b15349c3d993`

---

## SPA Context

**Purpose:** Align the Executive team on Q1 priorities; ensure cross-functional visibility across Entities; prioritize Enterprise Function initiatives so shared resources go to the highest impact work.

**Session:** Wed Jan 14, 2026 | Audience: QFG Executive team
**Key Output:** Prioritized list of Q1 initiatives.

---

## Portfolio Overview (~23 FTE + Advisory)

| # | Initiative | FTE | Primary Theme |
|---|-----------|-----|---------------|
| 1 | QuestBank Data Platform & Compliance Reporting | 7 + advisory | Regulatory / Launch Critical (OFSI, FinCrime) |
| 2 | Marketing Modernization (Braze, Clean Rooms) | 3 | Growth & CX (1P to 3P data sharing) |
| 3 | Self-Serve Provisioning & Access Mgmt ("IKEA flatpack") | 7 | Data Mesh Platform (Tenants + Exchange) |
| 4 | Self-Serve Analytics, Semantic Layer & Agentic AI | 4 + 15% PT | Semantic Layer + Agentic Analytics |
| 5 | DW Modernization (CorpBI to GCP) | 2 + advisory | Legacy to Cloud Platform |

**Theme Map:**
- Regulatory & Launch Critical: Initiative 1 (QuestBank + OFSI + FinCrime)
- Growth & CX: Initiative 2 (Braze, Haus, RCA)
- Data Mesh & Self-Serve: Initiatives 3 & 4 (Tenants, Exchange, Semantic Layer)
- Legacy Risk Reduction: Initiative 5 (CorpBI to GCP)

---

## Initiative Deep Dives

### Initiative 1: QuestBank Data Platform & Compliance Reporting

**Goal:** Launch a secure, resilient lakehouse for QuestBank Q1 products with OFSI and FinCrime-ready reporting.

**Core Responsibilities:**
- Ingest data from key banking source systems (CBS, LOS, CRM) into GCP / Databricks
- Build governed data products for: QuestBank Ops, Risk/FinCrime, Compliance/OFSI
- Support Power BI regulatory and operational reporting with a delivery vendor

**Q1 Outcomes:**
- OFSI and FinCrime-ready data products live in GCP/DBX
- Critical regulatory and operational Power BI reports wired to governed data
- Risk, Ops, and Compliance able to self-serve core QuestBank views

**Why it matters:** Must-win for bank launch; hard dependency for Ops, FinCrime, and regulatory reporting.

### Initiative 2: Marketing Modernization (Braze + Clean Rooms)

**Goal:** Feed Braze and partners (Haus, RCA) with near-real-time, governed data products + secure exports / clean rooms.

**Workstreams:**
- Braze integration (ingestion + data products in GCP lakehouse)
- External Data Export Patterns for Haus & RCA (reusable for future vendors)
- Data Clean Room Patterns (BigQuery + Sensitive Data Protection + DLP)

**Q1 Outcomes:**
- First Braze data contract defined and implemented for QuestBank journeys
- Clean room pattern proven for at least one marketing use case
- Governance guardrails in place for outbound marketing data

### Initiative 3: Self-Serve Provisioning & Access Mgmt

**Goal:** Give Entity teams a pre-assembled toolkit ("IKEA flatpack") to ingest, process, and publish data products with minimal central bottlenecks.

**MVP Components:**
1. **Secure Data Tenant** (per Entity/domain): Terraform IaC, ingestion tools, DQ tooling, ML tooling, orchestration, AI agents
2. **Data Exchange:** AI-assisted publisher workflow, AI-assisted access request, steward approvals, subscriber management
3. **Enablement:** AI guidance, best-practice templates, documentation, training

**Q1 Outcomes:**
- First Entity onboarded to standard tenant + Exchange workflow
- End-to-end path proven from ingestion to published Data Product
- Documentation and templates in place for scale-out in Q2

### Initiative 4: Self-Serve Analytics, Semantic Layer & Agentic AI

**Goal:** Reduce dependency on report factories by combining semantic models + agentic AI analytics on top of the platform.

**Workstreams:**
- Power BI Semantic Layer for high-traffic subject areas
- Evaluate: Databricks Apps & Visualization, BigQuery Studio + agents, Looker Studio Pro

**Q1 Outcomes:**
- Initial PBI semantic layer wired to at least one QuestBank and one Brokerage use case
- Agentic analytics pilot running on curated, semantic Data Products
- Governance patterns defined for semantic layer changes

### Initiative 5: DW Modernization (CorpBI to GCP)

**Goal:** Plan and initiate migration of on-prem CorpBI Data Warehouse to the cloud platform.

**Workstreams (Q1 = kick-off, not full migration):**
- Define target state architecture and access management mapping
- Evaluate and select migration vendor
- Prioritize data assets and workloads for migration waves

**Q1 Outcomes:**
- Access mapping and classification model defined for first CorpBI domain
- First migration wave scoped with clear SPA linkage
- Runbook for future waves drafted

---

## Design Principles (from Adam)

1. **Data Products, not raw tables:** Data Products are the unit of access, discovery, and consumption. Raw data stays inside producer domains.
2. **Clear publisher / subscriber boundaries:** Producers own quality, classification, and publishing. Consumers request via workflow. Data Stewards are final approvers.
3. **Consumer-centric bias:** Optimize for low-friction consumption. Producers absorb automation and governance overhead.
4. **Read-left / Write-right:** Downstream never mutates upstream in the medallion model.
5. **Simple systems will scale:** Only brainless, simple systems will scale effectively.
6. **User-centric design first:** Focus on end users (business teams), not the 300 people in QTG.

---

## Q1 Roadmap Timeline

| Month | Deliverable | SPA Initiative |
|-------|------------|----------------|
| Jan | QuestBank Data Products w/ OFSI-compliant access controls | #1 |
| Jan | Data Clean Room pattern for Marketing (Haus/RCA) | #2 |
| Feb | Data Exchange MVP (discovery + basic workflows) | #3 |
| Feb | Power BI Semantic Layer access integration | #4 |
| Mar | AI-assisted approval workflow pilot | #3 |
| Mar | DW migration access mapping complete | #5 |

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Time to data access | < 2 days (standard requests) |
| Audit coverage | 100% of Data Product access |
| Self-serve adoption | 50%+ access via Exchange |
| Compliance findings | 0 access-related findings |

---

## Key Performance Data Points

- 1,300 tables ingested in one month (vs. 8 months for 300 tables with previous vendor)
- ~85% of QuestBank data contains PII
- Power BI premium costs $2,500/user annually
- 80% of PBI reports are tables exported to Excel
- Streaming data enabled for first time (replacing T-1 batch)

---

## Cross-References

- Access control framework details: [access-management.md](./access-management.md)
- Data Mesh vision and org strategy: [data-mesh-vision.md](./data-mesh-vision.md)
- Q1 strategic decisions: [../Decisions/2026-q1-strategic-decisions.md](../Decisions/2026-q1-strategic-decisions.md)
- Databricks technical patterns: [databricks.md](./databricks.md)
- 10Q onboarding, CDO deliverables, Data Contracts: [questbank-playbooks.md](./questbank-playbooks.md)

---

---

## Org Restructuring (ACTIVE — ~4 Weeks Out as of Mar 18)

> Source: Meeting with Athena, March 18, 2026. Highly sensitive context. Not publicly announced.

### What's Happening
Adam Neus is planning a significant restructuring of the data org based on a producer/consumer data mesh model:
- **Current state:** 40-45 people across QTG data functions
- **Target state:** ~25 people in QTG; 15-20 people moving to bank side
- **Timeline:** Expected within ~4 weeks of March 18 (by mid-April)

### Producer/Consumer Split
- **Producer team** (QTG, Paroz's likely home): Owns data from bronze through semantic model (gold layer). Manages ingestion, transformation, pipeline reliability.
- **Consumer team** (shifting to bank): Works downstream from semantic model (silver→platinum). Responsible for department-specific platinum layers, dashboards, reporting.

### Product Management Changes
- Current PM team structure being dismantled
- PMs moving under new product leads, not current structure
- Bank will have product squads per line of business (credit card, mortgage, deposits) plus platform teams
- New product managers will be hired by new product leads, not current team

### New Analytics Team (Geneviève)
- **Geneviève** is building a new data science and analytics team for the bank (bank side, not QTG)
- Reports to John Gallagher
- Structure notionally approved by John Gallagher; FTE approval pending
- Starting with reporting focus (immediate need), expanding to predictive modeling + full-spectrum analytics
- Specifically wants data scientists, not data engineers
- Key candidates being considered: Tavneet (BA positioning), Ashwin (pure BI), Jeremy (data modeling for all of bank)
- Paroz has been mentioned to Geneviève as a potential resource/candidate

### Paroz's Position
- Adam and others "clawing at" Paroz; high visibility (mostly positive)
- Most likely outcome: Paroz stays on producer side with Adam
- Paroz should reach out to Geneviève via Slack to explore analytics team role and understand scope
- Paroz to provide list of potential candidates from CDC if Geneviève's team is building
- If Adam "harvests" DataWizards team: Artur and Yelena (Hyakalena) recommended for bank roles (familiar with Intellify domain)

### Databricks Assessment (as of Mar 18)
"Databricks implementation on the engineering side is as good as it can be. Focus now needs to shift to the business consumption side."

### Center of Excellence (CoE) Risk
- Adam considering a CoE model; received significant pushback
- Risk: CoE members become disconnected from actual work (like EA), lose credibility
- Paroz pushing back: "These chaps need to touch stuff. Otherwise, how are you different than EA?"

---

## Critical Delivery Timeline (Updated Mar 2026)

| Date | Milestone | Status |
|------|-----------|--------|
| Mar 23 (end of week) | IntelliFi data stabilization in Databricks for credit risk team | Target |
| Mar 25 | Current sprint (S5) ends; Keystone reports internal validation complete | Hard deadline |
| Mar 25 | TDA to Databricks connectivity validation | Target |
| Apr 2 | Keystone reports external communication to Sohail/finance | External deadline |
| Apr 6 | **QuestBank bank product go-live** (Temenos production launch, Lian coordinating) | HARD DATE |
| May (early) | Mortgage product validation (funded loans hit LMS/Temenos) | Dependent on Apr 6 launch |
| Mid-April | Expected org restructuring announcement | Estimate |

### Keystone Reports Context
Three Keystone reports cover ~95% of finance (QuestBank) day-one requirements:
- Working with Sohail (Finance) as authority and sign-off
- 90+ calculated fields being documented in field inventory
- Color coding: green = finance-specific (stays in Platinum), orange = shared across departments (move left to gold semantic model)
- MTG report issues being resolved; two other reports validated internally
- Internal deadline: March 25 | External comms: April 2
- Pending: treasury and capital markets confirmation (Sohail claims reports cover them; unverified)

### Deloitte Engagement
- Deloitte engaged for Prospector/Portfolio Plus and IntelliFi migrations to Temenos
- Timeline: migrations begin within 3 months of March 2026
- Implication: BigQuery technical debt for credit risk is temporary; all consolidation should target Databricks now

---

## Sprint 5 (S5) — March 11 to March 25

> Sprint goal: Establish foundational pipeline reliability (alerting + quarantine pattern) across all 4 domains, launch governance metadata pipeline, and unblock UAT/production readiness.

### 4 Data Domains
- **LMS** (Loan Management System) — Gabriel Cortes
- **LOS** (Loan Origination System) — Yelena Hakhumyan
- **Enablement** — Hayk Danielyan
- **Temenos** — Ljupco (with Artur as architect/oversight)

### Work Streams
| Stream | What | Owner |
|--------|------|-------|
| A | Pipeline Alerting (Airflow DAG + Databricks Jobs) | Gabriel, Yelena, Hayk, Ljupco |
| B | Pub/Sub Message Ordering (LOS, Enablement) | Gabriel, Yelena, Hayk |
| C | Code Branch Alignment (SIT/UAT sync) | Yelena, Hayk |
| D | DLT Expectations + Quarantine Pattern | Gabriel, Yelena (Artur pattern oversight) |
| E | Silver Pipeline Monitoring Dashboards | Gabriel, Yelena |
| F | Governance: Metadata Pipeline + PII Classification | Mariano |
| G | Temenos Tagging + Scheduling | Ljupco |
| H | UAT BigQuery Foreign Catalog + Production Readiness | Artur, Yelena |
| Spike | Python Wheel Deployment Strategy POC | Mariano (2-day timebox) |

### Governance (QB-9079) — 5-Step Sequence (Mariano Lead)
1. QB-9115: Create governance.* schema + PI LDM as code (1.5 days)
2. QB-9113: Databricks AI classification scan + domain mapping sessions (1 day + 4x2hr sessions)
3. QB-9114: Define UC governed tag taxonomy + apply PII tags via Terraform (1.5 days)
4. QB-9098: Implement 8 masking functions + column policies via Terraform (3 days)
5. QB-9099: Build dual data products, Row-Level Security + domain sign-off (2 days + 0.5/engineer)

### PI LDM — 39 Attributes, 8 Masking Functions
Authority: Daniel Dininio's spreadsheet. All 39 attributes are Confidential + Highly Valuable.

| Masking Function | Behavior | Count |
|-----------------|----------|-------|
| mask_completely() | Returns `****` | 17 (Address, Email, Name, Phone, SIN-adjacent, etc.) |
| mask_unmasked() | Returns value as-is (explicit policy) | 9 (Citizenship, City, Credit Score, etc.) |
| mask_income() | CEIL(val/10000) * 10000 | 4 (Income, Liabilities, Liquid Assets, Net Worth) |
| mask_dob() | Year only: 1985-**-** | 1 (Date of Birth) |
| mask_sin() | First digit only: 9xx xxx xxx | 2 (SIN, TIN) |
| mask_ssn() | First 3: 999xxxxxx | 1 (SSN) |
| mask_postal() | First 3: M4M *** | 2 (Postal Code, Employment Postal Code) |
| mask_existence_indicator() | Yes/No | 3 (Driver's Licence, Passport, PR Card) |

### Access Group Model
| Group | Scope | Masking |
|-------|-------|---------|
| pii_full_access | Regulatory, audit, compliance | No masking |
| pii_analytics | All analysts, BI, reporting | All 8 masking functions |
| pii_superuser | Governance + platform engineers (PAM) | Deferred to S6 |
| questbank_rls | All QB users | Row filter: business_entity = 'questbank' |

---

*Snapshotted: 2026-03-11. Updated: 2026-03-20 with March meeting learnings. For live status, query Initiative Page (`684aa911db824338b94291fe4c6266d3`).*
