# [Team Name]: Work Context

> Team context, platform architecture, Agile practices, stakeholder landscape, and operational frameworks for day-to-day leadership.

---

## 1. Team Overview

### Team Profile
- **Size:** 5 data engineers
- **Function:** Data Engineering & Business Intelligence
- **Company:** [Company Name]
- **Reporting:** Reports into Engineering organization
- **Mission:** Build and operate [Platform Name]: the enterprise data lakehouse

### Team Culture
- Documentation-first (async-first communication)
- Agile with 2-week sprints
- Blameless retrospectives
- Code review as learning opportunity
- Domain ownership model (each engineer owns a data domain)

---

## 2. Platform Architecture

### Medallion Architecture
```
Source Systems (Core Banking, APIs, Streaming)
        |
        v
+-------------------------------+
|  Bronze Layer (Raw Ingestion)  |  <- COPY INTO, Auto Loader, Streaming
|  - Raw data, no transforms    |
|  - Schema-on-read             |
|  - Full audit trail           |
+--------------+----------------+
               |
               v
+-------------------------------+
|  Silver Layer (Cleansed)       |  <- Delta Live Tables, quality rules
|  - Deduplicated, validated    |
|  - Standardized schemas       |
|  - Business keys applied      |
+--------------+----------------+
               |
               v
+-------------------------------+
|  Gold Layer (Business-Ready)   |  <- Star schemas, aggregations
|  - Dimensional models         |
|  - KPI calculations           |
|  - Business logic applied     |
+--------------+----------------+
               |
               v
+-------------------------------+
|  Platinum Layer (Curated)      |  <- Self-serve, governed
|  - Pre-built datasets         |
|  - Certified metrics          |
|  - ML feature stores          |
+-------------------------------+
               |
               v
    BI / ML Models / Regulatory Reports
```

### Key Integration: Core System
- Core system manages accounts, transactions, customers
- Integration via CDC (Change Data Capture) patterns
- Critical for regulatory reporting
- High-priority delivery milestone

### Technology Stack
| Component | Technology |
|-----------|-----------|
| Platform | Databricks on Azure |
| Storage | Cloud Data Lake Storage |
| Governance | Unity Catalog |
| Orchestration | Delta Live Tables (DLT) |
| BI | Power BI (DirectQuery + Import) |
| Streaming | Kafka -> Auto Loader / Structured Streaming |
| Security | ABAC (column masking) + RBAC (row filtering) |
| Version Control | Git |
| CI/CD | Cloud Pipelines |

---

## 3. Agile Practices

### Sprint Cadence
- **Sprint Length:** 2 weeks
- **Sprint Planning:** First Monday, 2 hours
- **Daily Standup:** 15 minutes, async-first option
- **Sprint Review:** Last Friday, demo to stakeholders
- **Retrospective:** Last Friday, after review

### User Story Format

For the full user story template with subtasks and Gherkin acceptance criteria, see `Templates/user-story.md`.

Quick format: **As a** [persona], **I want to** [action], **So that** [business value]. Include acceptance criteria, technical notes, and definition of done.

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

> For full framework definitions, see `Knowledge/Frameworks/leadership.md` (Mintzberg, Kotter) and `Knowledge/Frameworks/strategy.md` (Strategic Planning). Below shows how they apply to this role.

### Mintzberg's 10 Managerial Roles
| Category | Role | Application |
|----------|------|------------|
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

### Management vs. Leadership (Kotter)
| Management | Leadership |
|------------|-----------|
| Planning & budgeting | Setting direction |
| Organizing & staffing | Aligning people |
| Controlling & problem solving | Motivating & inspiring |
| Produces consistency | Produces change |

Both are necessary. Overindexing on management leads to stagnation. Overindexing on leadership leads to chaos.

### Strategic Planning Framework
1. **PEST Analysis** -> Regulatory landscape, industry competition, cloud trends
2. **Five Forces** -> Data platform competitive dynamics within the organization
3. **SWOT** -> Team strengths/weaknesses/opportunities/threats
4. **Ansoff Matrix** -> Growth: new data domains, new consumers, new capabilities
5. **Value Proposition** -> What the platform uniquely delivers
6. **Vision/Mission** -> Where the team is heading
7. **SMAC Objectives** -> Specific, Measurable, Achievable, Compatible goals
8. **Balanced Scorecard** -> Financial, Customer, Internal Process, Learning & Growth metrics
9. **Action Plan** -> Hierarchical: Strategic -> Tactical -> Operational

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
| Business Units | Insights, reports, decision support | BI dashboards, data catalog |

### Communication Cadence

For the full communication cadence (meeting types, durations, frequencies), see `_Registry/Cadences.md`.

---

## 6. HR & Team Development

### Performance Management
- Quarterly 1-on-1s with growth objectives
- Annual performance reviews tied to competency framework
- Skills matrix: each engineer rated on key technical and soft skills
- Individual Development Plans (IDPs) for each team member

### Compensation Analysis Framework
When making the case for promotions or adjustments:
1. Market data (industry benchmarks, internal bands)
2. Performance evidence (deliverables, impact, peer feedback)
3. Retention risk assessment
4. Internal equity comparison
5. Total compensation modeling (base + bonus + equity + benefits)

### Team Development Areas
- Delta Live Tables and advanced platform features
- Streaming data architecture
- Data modeling best practices
- Stakeholder communication skills
- Technical writing and documentation

---

## Glossary

| Abbreviation | Meaning |
|-------------|---------|
| ABAC | Attribute-Based Access Control |
| CDC | Change Data Capture |
| DLT | Delta Live Tables |
| ELT | Extract, Load, Transform |
| MVP | Minimum Viable Product |
| PI | Program Increment |
| RBAC | Role-Based Access Control |
| SLA | Service Level Agreement |
| TPS | Toyota Production System (also: Transactions Per Second) |
| UC | Unity Catalog |
| WIP | Work in Progress |
