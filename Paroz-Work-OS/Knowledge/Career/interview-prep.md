# Interview Preparation System

> STAR/CARL story bank and behavioral question mapping, sourced from Paroz's 24-project archive. For deep prep workflows, see `_Career/_skills/INTERVIEW_PREP.SKILL.md`.

**Source Folder:** `C:\Users\paroz\OneDrive\Desktop\Smith Cornell EMBA Classes\_Career\`
**Project Bank:** `_Career/00-Career-Command-Center/PROJECT_BANK.md` (24 projects, 400 lines)

---

## Behavioral Interview Frameworks

### CARL (Primary, for leadership/growth questions)

| Element | What to Cover | Time |
|---------|-------------|------|
| **Context** | Situation and background (who, what, when, why it mattered) | 15 sec |
| **Action** | What YOU specifically did (not the team) | 30 sec |
| **Result** | Measurable outcome (quantify wherever possible) | 15 sec |
| **Learning** | What you learned and how it changed your approach | 15 sec |

**Total: 75-90 seconds.** Interviewers lose focus after 2 minutes.

### STAR (Backup, for straightforward "tell me about a time" questions)

| Element | Purpose |
|---------|---------|
| **Situation** | Set the scene |
| **Task** | Your responsibility |
| **Action** | What you did |
| **Result** | Measurable outcome |

### CAR (For resume bullets, not interviews)

**Context** + **Action** + **Result** in one concise sentence.

---

## STAR Story Bank (from 24-Project Archive)

### Leadership and People Stories

| Question Theme | Project | Key Metrics | EMBA Framework |
|---------------|---------|-------------|----------------|
| **Leading through ambiguity** | QuestBank data infrastructure (A2) | Banking-grade real-time pipelines, 4-unit KPI framework | IDEALS, Congruence Model |
| **Developing team members** | DataWizards cross-cultural team | 3 continents, M&A integration, certification programs | Transformational Leadership (4 I's) |
| **Resolving conflict** | Post-Flexiti M&A reporting integration (A3) | Single source of truth replacing fragmented definitions | DiSC, SPLIT framework |
| **Giving difficult feedback** | Performance management within DataWizards | Improved delivery velocity | SBI model |
| **Building team culture** | DataWizards async-first, documentation-first culture | Sprint predictability, knowledge sharing | Lencioni Five Dysfunctions |
| **Cross-cultural leadership** | Armenia + Toronto + Brazil coordination | Successful integration during M&A | SPLIT framework, Authenticity Paradox |

### Strategic Thinking Stories

| Question Theme | Project | Key Metrics | EMBA Framework |
|---------------|---------|-------------|----------------|
| **Major technical decision** | Databricks vs GCP Studio POC (A1) | $1.2-1.5M annual decision, 3-year TCO | Decision Analysis, VRIN |
| **Prioritizing competing demands** | 5 Q1 2026 initiatives with ~23 FTE | Resource allocation across 5 initiatives | 10-10-10, SPA framework |
| **Influencing without authority** | Databricks dashboards over Power BI | $2,500/user savings, Unity Catalog integration | Pyramid Principle, ROI |
| **Aligning technical to business** | Data mesh consumer-first strategy | Consumer adoption as pull mechanism | Consumer-first, CDO deliverables |
| **Simplifying complexity** | PII access model (4 levels to 2) | Reduced group proliferation, clearer governance | "Brainless first" principle |

### Execution and Delivery Stories

| Question Theme | Project | Key Metrics | EMBA Framework |
|---------------|---------|-------------|----------------|
| **Delivering under pressure** | QuestBank 1B launch (Mar 24 deadline) | Production-ready on deadline | Operations Mgmt, critical path |
| **Handling technical debt** | Gold layer skip (Bronze-to-Platinum) | Speed vs. quality trade-off, documented debt | Cost of delay analysis |
| **Project failure/struggle** | Temenos integration complexity | Adapted timeline, managed stakeholder expectations | After-Action Review |
| **Managing stakeholders** | 16 stakeholders across 5 initiatives | Cross-functional alignment | Stakeholder mapping, BLUF |
| **Scaling a system** | 1,300 tables ingested in 1 month | 95%+ data capture rate | 10Q framework, medallion arch |
| **ROI and business case** | RBAC Transformation (A5) | $1.27-1.47M investment, $1.2-1.5M annual value, 12-month payback | Managerial Accounting, NPV |
| **Change management** | RBAC governance rollout | CTO+CFO co-sponsorship, phased rollout | Kotter's 8-Step |

---

## Technical Interview Areas

### Architecture Design (whiteboard/system design)

**Answer structure (Pyramid Principle):**
1. **Clarify requirements** (2 min): users, data volume, latency, compliance, budget
2. **State your approach** (1 min): high-level architecture choice with rationale
3. **Draw the architecture** (5 min): components, data flow, key decisions
4. **Discuss trade-offs** (3 min): what you chose and why, alternatives considered
5. **Scale and evolve** (2 min): how this grows at 10x

### Technical Depth Areas

| Domain | Key Topics | Depth |
|--------|-----------|-------|
| **Databricks/Spark** | DLT, Unity Catalog, medallion architecture, Photon, SQL Warehouse, Auto Loader | Deep (daily use) |
| **Data Modeling** | Star schema, Data Vault, One Big Table, SCD Type 1/2, slowly changing dimensions | Deep |
| **Data Governance** | ABAC/RBAC, CDMC classification, lineage, catalog, Entra ID | Deep (built this) |
| **Cloud (Azure)** | ADLS, Key Vault, Entra ID, networking, cost management | Moderate |
| **Cloud (GCP)** | BigQuery, IAM, serverless, Pub/Sub | Moderate |
| **Python/SQL** | PySpark, pandas, advanced SQL, testing, CI/CD | Deep |
| **Data Mesh** | Domain ownership, data products, federated governance, publisher/subscriber | Conceptual + practical |
| **ML/AI** | Feature stores, model serving, MLflow, RAG, agents, MCP | Conceptual + demo (mcp-databricks-server) |

### System Design Patterns

| Pattern | When to Use | Paroz's Experience |
|---------|-------------|-------------------|
| **Medallion (Bronze/Silver/Gold/Platinum)** | General-purpose lakehouse | QuestBank, 22-week POC |
| **Data Mesh** | Multiple domains, decentralized ownership | Q1 2026 strategy with Adam |
| **ABAC + RBAC** | Fine-grained access control | Simplified PII model, Unity Catalog |
| **Data Exchange** | Internal data product marketplace | Designed but not yet built |

---

## Common Questions and Prepared Answers

### "Tell me about yourself" (60-90 seconds, Present-Past-Future)

> "I'm a Technical PM leading data platform engineering at Questrade, where my team of 5 built QuestBank, an enterprise data lakehouse on Databricks. We serve analytics, regulatory reporting, and ML across the organization, managing a portfolio worth $1.5M+ in annual value. Before this, I progressed from data engineering IC work to technical leadership, including managing a cross-cultural team spanning Armenia, Toronto, and Brazil through an M&A integration. I recently completed my Cornell-Queen's Executive MBA, which gave me frameworks for strategic thinking, financial analysis, and organizational leadership that I apply daily. I'm now looking for [specific next step] because [reason tied to this role/company]."

### "Why are you looking to leave?" (Pull, not push)

> "I'm not running from anything. I've built something I'm proud of at Questrade. But I'm at a point where I want [specific growth this role offers]. The work your team is doing on [specific project] is exactly the kind of [scale/challenge/impact] I want to tackle next."

### "What's your biggest weakness?" (Real + mitigation + evidence)

> "I tend to over-index on documentation and written communication, which can slow decision-making when a quick verbal alignment would suffice. I've been working on this by using the 10-10-10 framework to calibrate: is this a 10-minute decision (just decide in Slack) or a 10-month decision (write the memo)?"

### "Where do you see yourself in 5 years?" (Ambitious + realistic)

> "I want to be leading a data organization, not just a team. Building the platform at Questrade showed me that the real impact comes from connecting technical infrastructure to business outcomes. In 5 years, I want to own that connection at a larger scale, whether that's a VP of Data Engineering, Head of Data Platform, or a consulting partner helping multiple organizations transform."

---

## Panel Interview Strategy

| Interviewer | What They Care About | Adapt Your Answers |
|------------|---------------------|-------------------|
| **Hiring Manager** | Can you do the job? Reliable? | Specifics, execution, delivery track record |
| **Skip Level** | Strategic thinking, growth potential | Business impact, vision, executive presence |
| **Peer** | Collaboration, complementary skills | Humility, shared goals, "we" language |
| **Direct Report** | Leadership style, empowerment | Growth support, autonomy, clear communication |
| **Cross-functional** | Ease of collaboration | Shared goals, flexibility, stakeholder awareness |

---

## Case Interview Framework (for consulting roles)

1. **Clarify** (1 min): Restate problem, ask clarifying questions
2. **Structure** (2 min): MECE decomposition or issue tree (see Consulting.SKILL.md)
3. **Analyze** (5 min): Work through structure with data and logic
4. **Recommend** (2 min): Clear recommendation with evidence, risks, next steps

---

## Interview Day Logistics

### Pre-Interview Checklist
- [ ] Research company (annual report, news, Glassdoor, LinkedIn)
- [ ] Research each interviewer (LinkedIn, publications, talks)
- [ ] Map 5 CARL/STAR stories to likely question themes
- [ ] Prepare 3 questions per interviewer (specific to their role)
- [ ] Test tech setup (if virtual): camera, mic, lighting, background
- [ ] Have water, notepad, resume copy ready

### Post-Interview Protocol
- Same-day thank you emails (personalized per interviewer, reference something specific they said)
- Debrief notes: what went well, what to improve, signals about interest level
- Update pipeline tracker in Notion Hunt Hub
- Refine stories based on actual questions asked

---

## Personal Brand (Quick Reference)

### LinkedIn Strategy
- **Headline:** Role + differentiator (120 char max)
- **Summary:** Positioning statement adapted for LinkedIn tone
- **Experience:** XYZ/CAR formula (accomplishments, not job descriptions)
- **Content:** 1-2 posts/month on data engineering, platform leadership, EMBA insights
- **Engagement:** Comment on 3-5 industry posts/week

### Thought Leadership Topics (Paroz's sweet spot)
1. Data mesh in practice (not theory)
2. Databricks lakehouse patterns for regulated industries
3. Building data teams that think like product teams
4. The Technical PM role: bridging engineering and business
5. Applying MBA frameworks to data engineering decisions

**Full LinkedIn SKILL:** `_Career/_skills/LINKEDIN_OPTIMIZATION.SKILL.md`

---

## Source Material Reference

| Resource | Location |
|----------|----------|
| Full STAR stories (24 projects) | `_Career/00-Career-Command-Center/PROJECT_BANK.md` |
| Executive profile with metrics | `_Career/00-Career-Command-Center/Paroz_Mehta_Profile.md` |
| Interview prep methodology | `_Career/02-Interview-Prep/08_INTERVIEW_PREPARATION.md` |
| Salary negotiation | `_Career/02-Interview-Prep/09_SALARY_NEGOTIATION.md` |
| Case interview prep | `_Career/04-Consulting-Track/10_CONSULTING_TRACK.md` |
| Interview SKILL workflow | `_Career/_skills/INTERVIEW_PREP.SKILL.md` |
| Resume help guides (11 files) | `_Career/02-Interview-Prep/Resume-Help-Guides/` |

---

*Cross-references: [career-strategy.md](./career-strategy.md) for positioning and negotiation, [Knowledge/EMBA/Skills/Consulting.SKILL.md](../EMBA/Skills/Consulting.SKILL.md) for MECE/issue trees, [Knowledge/Work/communication.md](../Work/communication.md) for PREP framework*

*Last updated: 2026-03-15*
