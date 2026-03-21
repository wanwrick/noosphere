# DataWizards — Work Context

> Team context, QuestBank platform, Agile practices, stakeholder landscape, and operational frameworks for Paroz's day-to-day leadership role.

---

## 1. Team Overview

### DataWizards Team
- **Size:** 6 data engineers + Paroz (TPM)
- **Function:** Data Engineering & Business Intelligence
- **Company:** Questrade Financial Group (Canadian online brokerage)
- **Reporting:** Reports into Engineering organization under Adam Neus (Managing Director)
- **Mission:** Build and operate QuestBank — the enterprise data lakehouse
- **Geographic spread:** Armenia (Artur, Yelena, Hayk), Brazil (Gabriel), Eastern Europe (Ljupco), Argentina (Mariano)

### Team Roster — Domain Ownership Model

| Engineer | Domain | Focus | Notes |
|----------|--------|-------|-------|
| **Artur Gyulambaryan** | Temenos + Architecture | Lead architect; DLT pattern design; Event Hub; Temenos message gateway author | Senior; oversight role for sprint execution; key escalation path |
| **Gabriel Cortes** | LMS (Loan Management System) | Airflow DAG alerting, DLT expectations, quarantine pattern, dashboards, JSOC integration | Most critical path items in S5; proactive on incident tickets |
| **Yelena Hakhumyan** | LOS (Loan Origination System) | Airflow DAG alerting, LOS Pub/Sub, branch alignment, UAT investigation | On leave intermittently; point person on data platform upon return |
| **Hayk Danielyan** | Enablement | Airflow DAG alerting, Enablement Pub/Sub, branch alignment | Well-scoped repeatable work pattern; lower risk load |
| **Ljupco** | Temenos | Temenos alerting, tagging, scheduling | Domain-specific, independent workstream |
| **Mariano Barrionuevo** | Governance + Data Classification | Metadata pipeline, AI-generated descriptions, PII classification, UC masking functions, Terraform | Lead on QB-9079 governance epic; Claude AI integration for metadata |

### Team Culture
- Documentation-first (async-first communication)
- Agile with 2-week sprints
- Blameless retrospectives
- Code review as learning opportunity
- Domain ownership model (each engineer owns a data domain)

---

## 2. QuestBank Platform

### Architecture
```
Source Systems (Temenos, APIs, Kafka)
        │
        ▼
┌─────────────────────────────┐
│  Bronze Layer (Raw Ingestion) │  ← COPY INTO, Auto Loader, Kafka
│  - Raw data, no transforms   │
│  - Schema-on-read            │
│  - Full audit trail          │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│  Silver Layer (Cleansed)     │  ← Delta Live Tables, quality rules
│  - Deduplicated, validated   │
│  - Standardized schemas      │
│  - Business keys applied     │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│  Gold Layer (Business-Ready) │  ← Star schemas, aggregations
│  - Dimensional models        │
│  - KPI calculations          │
│  - Business logic applied    │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│  Platinum Layer (Curated)    │  ← Self-serve, governed
│  - Pre-built datasets        │
│  - Certified metrics         │
│  - ML feature stores         │
└─────────────────────────────┘
              │
              ▼
    Power BI / ML Models / Regulatory Reports
```

### Key Integration: Temenos Core Banking
- Temenos is the core banking system (accounts, transactions, customers)
- Integration via CDC (Change Data Capture) patterns
- Critical for regulatory reporting (OFSI, PIPEDA)
- High-priority delivery milestone

### Technology Stack
| Component | Technology |
|-----------|-----------|
| Platform | Databricks on Azure |
| Storage | Azure Data Lake Storage Gen2 (ADLS) |
| Governance | Unity Catalog |
| Orchestration | Delta Live Tables (DLT) |
| BI | Power BI (DirectQuery + Import) |
| Streaming | Kafka → Auto Loader / Structured Streaming |
| Security | ABAC (column masking) + RBAC (row filtering) |
| Version Control | Git (Azure DevOps) |
| CI/CD | Azure Pipelines |

---

## 3. Agile Practices

### Sprint Cadence
- **Sprint Length:** 2 weeks
- **Sprint Planning:** First Monday, 2 hours
- **Daily Standup:** 15 minutes, async-first option
- **Sprint Review:** Last Friday, demo to stakeholders
- **Retrospective:** Last Friday, after review

### User Story Format
```
As a [persona],
I want to [action],
So that [business value].

Acceptance Criteria:
- Given [context], when [action], then [expected result]
- Given [context], when [action], then [expected result]

Technical Notes:
- [Implementation guidance]
- [Dependencies]

Definition of Done:
- [ ] Code complete and peer reviewed
- [ ] Unit tests passing (>80% coverage)
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] Deployed to staging
- [ ] Product owner approval
```

### Story Sizing (Fibonacci)
| Points | Complexity | Duration | Example |
|--------|-----------|----------|---------|
| 1 | Trivial | < 1 day | Config change, minor fix |
| 2 | Simple | 1-2 days | New column, simple transform |
| 3 | Standard | 2-3 days | New pipeline component |
| 5 | Moderate | 3-5 days | New data source integration |
| 8 | Complex | 1-2 sprints | New domain model, major refactor |
| 13 | Epic-level | Break down further | Too big for one sprint |

### PI Planning (Program Increment)
- Quarterly planning horizon
- Align team goals with organizational objectives
- Dependencies mapped across teams
- Capacity-based commitment
- Risk identification and mitigation

---

## 4. Strategic Frameworks (Applied to Role)

### Mintzberg's 10 Managerial Roles
| Category | Role | DataWizards Application |
|----------|------|------------------------|
| **Interpersonal** | Figurehead | Represent team in steering committees |
| | Leader | Coach engineers, set vision |
| | Liaison | Connect with analytics, compliance, business teams |
| **Informational** | Monitor | Track platform health, industry trends |
| | Disseminator | Share context and priorities with team |
| | Spokesperson | Present platform value to leadership |
| **Decisional** | Entrepreneur | Drive innovation, propose new capabilities |
| | Disturbance Handler | Manage incidents, resolve blockers |
| | Resource Allocator | Sprint planning, capacity allocation |
| | Negotiator | Scope, timelines, priorities with stakeholders |

### Kotter: Management vs. Leadership
| Management | Leadership |
|------------|-----------|
| Planning & budgeting | Setting direction |
| Organizing & staffing | Aligning people |
| Controlling & problem solving | Motivating & inspiring |
| Produces consistency | Produces change |

Both are necessary. Overindexing on management → stagnation. Overindexing on leadership → chaos.

### Queen's Strategy Workbook (Applied)
1. **PEST Analysis** → Regulatory landscape (OFSI, PIPEDA), fintech competition, cloud trends
2. **Five Forces** → Data platform competitive dynamics within Questrade
3. **SWOT** → DataWizards team strengths/weaknesses/opportunities/threats
4. **Ansoff Matrix** → Growth: new data domains, new consumers, new capabilities
5. **Value Proposition** → What QuestBank uniquely delivers
6. **Vision/Mission** → Where DataWizards is heading
7. **SMAC Objectives** → Specific, Measurable, Achievable, Compatible goals
8. **Balanced Scorecard** → Financial, Customer, Internal Process, Learning & Growth metrics
9. **Action Plan** → Hierarchical: Strategic → Tactical → Operational

---

## 5. Stakeholder Landscape

### Key Stakeholders
| Stakeholder | Interest | Engagement Strategy |
|-------------|----------|-------------------|
| VP Engineering | Platform reliability, team efficiency | Monthly tech updates, capacity planning |
| VP Product | Feature delivery, business value | Roadmap alignment, demo days |
| CTO | Architecture, innovation, risk | Quarterly strategy reviews |
| Compliance/Legal | Regulatory adherence, data privacy | ABAC/RBAC demos, audit readiness |
| Analytics Teams | Self-serve data, quality, freshness | Gold/Platinum layer usability |
| Business Units | Insights, reports, decision support | Power BI dashboards, data catalog |

### Communication Cadence
| Audience | Format | Frequency | Content |
|----------|--------|-----------|---------|
| Team | Standup | Daily | Blockers, progress |
| Team | Retro | Bi-weekly | Process improvements |
| Stakeholders | Sprint Review | Bi-weekly | Demos, value delivered |
| Leadership | Status Update | Monthly | 3P format (Progress/Plans/Problems) |
| Executives | Roadmap Review | Quarterly | Strategy, investment, ROI |

---

## 6. HR & Team Development

### Performance Management
- Quarterly 1-on-1s with growth objectives
- Annual performance reviews tied to competency framework
- Skills matrix: each engineer rated on key technical and soft skills
- Individual Development Plans (IDPs) for each team member

### Compensation Analysis Framework
When making the case for promotions or adjustments:
1. Market data (Levels.fyi, Glassdoor, internal bands)
2. Performance evidence (deliverables, impact, peer feedback)
3. Retention risk assessment
4. Internal equity comparison
5. Total compensation modeling (base + bonus + equity + benefits)

### Team Development Areas
- Delta Live Tables and advanced Databricks features
- Streaming data architecture
- Data modeling best practices
- Stakeholder communication skills
- Technical writing and documentation

---

## Glossary

| Abbreviation | Meaning |
|-------------|---------|
| ABAC | Attribute-Based Access Control |
| ADLS | Azure Data Lake Storage |
| CDC | Change Data Capture |
| DLT | Delta Live Tables |
| ELT | Extract, Load, Transform |
| MVP | Minimum Viable Product |
| OFSI | Office of the Superintendent of Financial Institutions |
| PI | Program Increment |
| PIPEDA | Personal Information Protection and Electronic Documents Act |
| RBAC | Role-Based Access Control |
| SLA | Service Level Agreement |
| TPS | Toyota Production System (also: Transactions Per Second) |
| UC | Unity Catalog |
| WIP | Work in Progress |
