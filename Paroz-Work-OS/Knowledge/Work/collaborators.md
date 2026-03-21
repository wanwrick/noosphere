# Key Collaborators

> Who Paroz works with, their domains, and how to interact with them effectively.

---

## DataWizards Team (Direct Reports)

| Name | Role Focus | Domain | Working Style |
|------|-----------|--------|---------------|
| **Artur Gyulambaryan** | Lead Architect | Temenos, Event Hub, DLT patterns, system architecture | Senior; oversight and pattern sign-off role; escalation path for infra issues |
| **Gabriel Cortes** | LMS Domain + DataOps | LMS ingestion, Terraform, CI/CD, Databricks admin, JSOC | Detail-oriented, proactive on tickets; opens issues without prompting |
| **Yelena Hakhumyan** | LOS Domain | LOS ingestion, branch alignment, UAT investigation, cross-team coordination | Key point person on data platform; intermittently on leave |
| **Hayk Danielyan** | Enablement Domain | Enablement pipelines, Pub/Sub, alerting | Well-scoped; follows patterns from Gabriel/Yelena implementations |
| **Ljupco** | Temenos Domain | Temenos alerting, tagging, scheduling | Independent workstream; focused on Temenos-specific deliverables |
| **Mariano Barrionuevo** | Governance + Classification | PII classification, UC masking, metadata pipeline, Terraform policies, Python wheel POC | Lead on QB-9079; uses Claude AI for metadata generation; high context-switching risk |

## Cross-Functional Partners

| Name | Role / Team | Domain | Interaction Pattern |
|------|------------|--------|-------------------|
| **Adam Neus** | Managing Director | Strategic direction, data strategy ownership, resourcing, executive alignment, Q1 SPA | Weekly 1:1, BLUF updates, decision escalations. Anchor for all strategy docs. Planning major org restructure (40-45 to ~25 people, producer/consumer model). |
| **Anna** | Data Exchange | Cross-system data flows, external partner integrations | Collaborative, async-first. No longer on QuestBank. |
| **Bart** | Platform Strategy | Architecture decisions, long-term platform direction, vendor strategy | Strategic discussions, needs data-backed proposals |
| **Martech Force** | Marketing Technology | Braze integration, marketing data modernization, campaign analytics | Project-based, new engagement for Q1 2026 |
| **Fran** | DataOps / Infrastructure | Managed tags, DLT clusters, Databricks deployment, GCP networking | Needed for managed tags implementation; cluster configuration |
| **Mauro** | DataOps / Infrastructure | Databricks cluster management, networking, GCP compute | Key for IP range changes, cluster troubleshooting, infrastructure escalations |
| **Divya** | Stakeholder Communications | Cross-team status updates, leadership communications, incident coordination | Takes ownership of stakeholder Slack/email communications during incidents |
| **Kriti Sood** | Platform Team | BigQuery/GCP side management, Entra ID groups provisioning (pii_full_access, pii_analytics) | Engaged for VPC issues and group provisioning; escalation path for GCP infrastructure |

## Extended Stakeholders (Bank + QTG)

| Name | Role / Team | Domain | Interaction Pattern |
|------|------------|--------|-------------------|
| **Amandeep (Aman)** | AML / FinCrime + Regulatory Reporting | Anti-money laundering pipelines, credit card AML, Keystone report delivery | Regulatory-driven timelines; non-negotiable deadlines; owns Keystone report validation internally |
| **Zoya** | Finance Liaison (Bank) | Keystone report requirements, metrics sign-off, Sohail liaison | Point of contact for finance-side metrics collection; manages metrics sheet |
| **Sohail** | Finance (Bank) | Finance authority and source of truth for Keystone reports; metrics sign-off | Named by Justin, David Furlong as finance authority; ~95% of Keystone requirements covered by 3 reports |
| **Nilanjana** | Data Governance | Data classification framework ownership, CDMC, Unity Catalog classification implementation | Joint owner of classification decisions AND implementation (not just policy). Works with Cam. Needs Databricks admin access. |
| **Daniel Dininio** | Data Governance | PI LDM authority, 39 PI attributes, classification standards, masking function definitions | Final sign-off authority before any terraform apply on masking. PI LDM spreadsheet is source of truth. |
| **Dan (Governance)** | Data Governance | Access control design, ABAC/RBAC policy | Architecture partner for access management; co-designed simplified PII model |
| **Cam** | Data Governance | Learning Unity Catalog classification; shadowing Nilanjana | In learning mode; will take on classification work to lighten Mariano/Gabriel load |
| **Mark Huang** | Platform Leadership | Executive sponsorship, cross-functional alignment, managed tags sign-off | Senior stakeholder; needs business-value framing; involved in Terraform/tags decisions |
| **Monty** | Databricks (Vendor) | Databricks Solutions Architect, Unity Catalog roadmap, technical enablement, incident escalation | Direct escalation path for Databricks issues; joined cluster incident call immediately when pinged. Critical backline contact. |
| **Daniel** | Databricks (Vendor Support) | Support engineer, workspace access, cluster diagnostics, backline escalation | Handles support tickets; joins calls for diagnostics; escalates to backline |
| **Geneviève** | Bank Analytics Team (Building) | Standing up new data science and analytics team for QuestBank. Owns bank business processes. | Reports to John Gallagher. French Canadian, direct communication style. Building team from scratch (reporting-first, expanding to predictive). Reach via Slack. |
| **John Gallagher** | Bank Leadership | SLAs, measurement, real-time and strategic monitoring. Operations oversight. | Very focused on measurement and accountability; outsourcing time-trial analytics because no internal capability |
| **Matt Farson / Barsam** | Bank Product/Engineering Leadership | Bank technology and product strategy; wants minimal QTG dependency | Key decision-maker on bank side; wants bank to own its own analytics capability |
| **Justin (Adler)** | Finance/Operations (Bank) | Regulatory reporting stakeholder; metrics authority | Named authority alongside Sohail for finance metric sign-offs |
| **David Furlong** | Leadership | Slack-first communication policy (no email) | Directive: all communications via Slack, not email |
| **Shreya** | Credit Risk Analytics | IntelliFi data consolidation in Databricks; credit risk model validation | Flagged IntelliFi data visibility issue on Mar 9; critical blocker for credit risk consolidation |
| **Subha** | Credit Risk Analytics | ECL, RAS, credit risk modeling; data consolidation oversight | Leads credit risk analytics team; needs consolidated Databricks dataset for regulatory models |
| **Jeremy** | Data Science (Bank) | Director of Data Science; data modeling; underutilized for cross-bank modeling | Could model data for entire bank, not just risk. Potential ally for Geneviève's analytics team. |
| **Lucas** | Production Support | Production access management, SFTP validation, Datadog monitoring, launch support | Technology team loses prod access post-go-live; Lucas's team owns production validation |
| **Scott** | Operations/Connectivity | SFTP validation, GL extract scheduling, API connectivity testing | Handles file-based integrations pre-launch |
| **Lian** | Temenos Integration Lead | Production validation planning, Temenos checklist, go-live coordination | Owns Temenos production validation document; coordinates with Temenos on stakeholder availability |
| **Carlos** | Temenos / TDA | TDA to Databricks connectivity validation; March 25 target | Owns TDA-Databricks connectivity proof |
| **Alejandro** | QuestBank Engineering | Core banking platform engineering, integration architecture | Technical partner for QuestBank data flows |
| **Tavneet** | Analytics (transitioning) | BA positioning; met with Geneviève; data definition curation work | Being considered for Geneviève's reporting team; strong BA skills |
| **Samandhi** | Analytics / Data Governance | Being trained for data definition curation and field inventory | Tavneet was originally doing this; now Samandhi is taking it over |
| **Ashwin** | Analytics | Pure BI capability; recommended for Geneviève's analytics team | Strong BI candidate for the new bank analytics team |

## Interaction Guidelines

**For DataWizards (direct team):**
- Use Agile ceremonies for task alignment (sprint planning, standup, retro)
- Provide clear acceptance criteria — they execute best with well-defined stories
- Apply SBI feedback model (Situation → Behavior → Impact)
- Document decisions in Notion for async visibility

**For cross-functional partners:**
- Lead with BLUF in all communications
- Frame requests in terms of business value, not technical details
- Use PREP framework for impromptu discussions (Point → Reason → Example → Point)
- Maintain stakeholder map awareness — know their priorities and pressures

**For leadership (Adam, Bart):**
- Present options with a recommendation (3 options + pick)
- Use data and evidence, not opinions
- Anticipate questions — prepare the "so what?" before presenting
- Frame platform work as business value, not infrastructure cost

---

*Last updated: 2026-03-14*
