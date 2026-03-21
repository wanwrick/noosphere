# Job Application Workflow

> End-to-end workflow triggered when Paroz pastes a job description or says "apply to [company] for [role]." Produces a complete application package with real document files, LinkedIn outreach, and Notion Hunt Hub tracking.

**Trigger phrases:** "Apply to [company]", "Here's a job posting...", "I want to apply to this role", "Help me apply", "Tailor everything for this job", or any pasted job description text.

**Output formats:** Resume (.docx + .pdf), Cover Letter (.docx + .pdf), LinkedIn outreach (text), Company Brief (.md), Interview Prep (.md)

---

## Step 1: Trigger Detection

Parse the pasted job description and extract:

| Field | Value |
|-------|-------|
| **Company** | |
| **Role Title** | |
| **Location** | City / Remote / Hybrid |
| **Compensation** | Range if stated |
| **Department** | Team or division |
| **Reports To** | If mentioned |
| **Source** | LinkedIn / Company site / Referral / Cornell portal |

---

## Step 2: Context Loading (Parallel Reads)

Load these files in parallel before generating any deliverables:

**Career Assets (from `_Career/` source folder):**
- `00-Career-Command-Center/Paroz_Mehta_Profile.md` (full experience inventory, 300 lines)
- `00-Career-Command-Center/PROJECT_BANK.md` (24 projects with STAR stories + resume bullets, 400 lines)
- `00-Career-Command-Center/Current_Initiatives_Deep_Dive.md` (fresh bullet points, 365 lines)
- `04-Consulting-Track/02_RESUME_GUIDE.md` (Cornell Career Services resume methodology)
- `00-Career-Command-Center/03_COVER_LETTER_FRAMEWORK.md` (Cornell 3-part cover letter structure)
- `_skills/RESUME_TAILORING.SKILL.md` (keyword matching algorithm)
- `_skills/NETWORKING.SKILL.md` (outreach templates)

**Work OS Knowledge (from `Knowledge/`):**
- `Career/career-strategy.md` (VRIN analysis, positioning, target roles)
- `Career/interview-prep.md` (STAR/CARL bank, behavioral + technical prep)

**EMBA Frameworks (apply during analysis):**
- `EMBA/strategy.md` (VRIN for competitive positioning of Paroz vs. other candidates)
- `EMBA/marketing.md` (STP for targeting: segment the company's need, position Paroz as the answer)
- `EMBA/Skills/Negotiation.SKILL.md` (BATNA for salary negotiation anchors)

---

## Step 3: JD Analysis

### 3a. Requirements Extraction

```
HARD REQUIREMENTS (must-have):
- [ ] [Skill/experience 1]
- [ ] [Skill/experience 2]
- [ ] ...

NICE-TO-HAVE:
- [ ] [Skill/experience 1]
- [ ] ...

KEY KEYWORDS (for ATS):
[List every technical term, tool, methodology, certification mentioned]

CULTURE SIGNALS:
[Values, work style, team dynamics from the posting]

ROLE TYPE:
[ ] MBB Consulting  [ ] Strategy  [ ] Product Management
[ ] Data Leadership  [ ] AI/ML    [ ] Other: ___
```

### 3b. Keyword Match Analysis

Compare JD keywords against Paroz's profile. Target: **70%+ match**.

| JD Keyword | Paroz Has? | Evidence Source |
|------------|------------|----------------|
| [keyword] | Yes/No/Partial | [Specific project/metric from Profile] |

### 3c. VRIN Positioning (Business Strategy framework)

Map Paroz's competitive advantage to this specific role:
- **Valuable:** Which of Paroz's skills directly address their stated needs?
- **Rare:** What combination does Paroz offer that other candidates likely don't?
- **Inimitable:** What experience is hard to replicate quickly?
- **Non-substitutable:** Why can't they get this value from a different type of candidate?

### 3d. Gap Analysis

Flag any keywords below 70% match as **gaps to address** in the cover letter. For each gap, identify the closest transferable experience.

---

## Step 4: Resume Generation

**MANDATORY: Use the `docx` skill to generate a Word file and `pdf` skill to generate a PDF.**

### Resume Structure (2 pages max, per Cornell Career Services)

**Header:**
```
PAROZ MEHTA
Toronto, ON | 647-500-5870 | pm662@cornell.edu | linkedin.com/in/parozmehta
```

**Executive Summary (3-4 lines):**
- Dynamically generated from JD keywords + Profile
- Format: "[Target identity] with [X years] experience in [JD-relevant domains]. [Key achievement with metric]. [EMBA credential + differentiator]."

**Professional Experience (reverse chronological):**
- Select 3-5 bullets per role, prioritized by JD keyword match
- Every bullet uses CAR format (Context-Action-Result) with quantified metrics
- Use the keyword matching table from Step 3b to select the highest-impact bullets

**Keyword Selection Table:**

| JD Emphasis | Paroz Achievement to Pull |
|-------------|--------------------------|
| Data Engineering | Databricks POC: 22-week, 25-35% efficiency, 3x performance |
| Leadership | DataWizards: 3 countries, M&A integration, team development |
| Strategy | RBAC: $1.27-1.47M business case, 12-month payback |
| AI/ML | MCP server, AI/BI Genie (80% success), Feature Store |
| Change Management | Kotter's 8-Step applied to RBAC, Flexiti integration |
| Financial Analysis | NPV/IRR modeling, $1.5M+ portfolio, TCO analysis |
| Governance/Compliance | Unity Catalog, RBAC, column-level lineage, audit trails |
| Cross-functional | CTO/CFO alignment, Credit Risk/Finance/Treasury stakeholders |

**Education:**
```
Cornell University, S.C. Johnson Graduate School of Management
Executive MBA, Class of 2026 | Ranked #6 in Cohort
```

**Certifications:** Select based on JD relevance (CSPO, A-CSPO, DASM, DASSM, DAVSC, Google Cloud)

**Skills Section:** Prioritize based on JD keywords

### Output Files
- `_Career/01-Personal-Brand/Resumes/Current/Paroz_Mehta_Resume_[Company]_[Role-Short].docx`
- `_Career/01-Personal-Brand/Resumes/Current/Paroz_Mehta_Resume_[Company]_[Role-Short].pdf`

---

## Step 5: Cover Letter Generation

**MANDATORY: Use the `docx` skill to generate a Word file and `pdf` skill to generate a PDF.**

### Cover Letter Structure (1 page max, per Cornell Career Services)

**Paragraph 1: Introduction (Why You're Writing)**
- Position applying for + how you found the opportunity
- Referral name if applicable
- One-sentence hook connecting background to their need

**Paragraph 2: Value Match (Why You're Qualified)**
- 2-3 specific achievements that directly match JD requirements
- Mirror their language/keywords
- Quantify impact ($, %, time saved)

**Paragraph 3: Company-Specific (Why This Company)**
- Reference specific company initiative, news, or value
- Connect experience to their strategic priorities
- Show genuine research (not generic)

**Paragraph 4: Close (Call to Action)**
- Express enthusiasm
- Mention availability for interview
- Professional sign-off

### Cover Letter Rules
- Max 4 paragraphs, 1 page
- SCR undertone: Situation (their need), Complication (the challenge), Resolution (you're the answer)
- Address to specific person when possible (check LinkedIn for hiring manager)
- Never generic; every letter must reference specific company details

### Output Files
- `_Career/01-Personal-Brand/Cover-Letters/Current/Paroz_Mehta_CoverLetter_[Company].docx`
- `_Career/01-Personal-Brand/Cover-Letters/Current/Paroz_Mehta_CoverLetter_[Company].pdf`

---

## Step 6: LinkedIn Outreach Messages

Generate 2-3 copy-paste-ready outreach variants using templates from `NETWORKING.SKILL.md`:

### Variant A: Cornell Alumni at the Company (< 100 words)
```
Subject: Fellow Johnson MBA - [Topic]

Hi [Name],

As a fellow Johnson MBA ([their year]), I'm reaching out about [specific topic].
I'm in the EMBA Class of 2026, currently in data platform leadership at Questrade.

Would love to hear your perspective on [1 specific question].
Could we connect for a brief call?

Go Big Red!
Paroz
```

### Variant B: Hiring Manager / Team Lead (< 150 words)
```
Subject: Cornell EMBA '26 - [Role Title] at [Company]

Hi [Name],

I'm Paroz Mehta, a Cornell Executive MBA candidate (Class of 2026)
currently leading data platform strategy at Questrade. I'm exploring
[specific role type] opportunities at [Company].

[1 sentence about why you admire their work/company - be specific]

I'd love to learn about your experience at [Company], particularly
around [specific topic]. Would you have 15 minutes for a brief call
in the next couple of weeks?

Thank you for considering,
Paroz Mehta
Cornell Johnson EMBA '26 | 647-500-5870
```

### Variant C: Mutual Connection Referral (< 120 words)
```
Subject: [Mutual connection] suggested I reach out

Hi [Name],

[Mutual connection] recommended I connect with you regarding
[specific topic] at [Company]. I'm a Cornell EMBA candidate
leading data platform strategy at Questrade.

[1 sentence linking your experience to their domain]

Would you be open to a 15-minute conversation? I'm happy to
work around your schedule.

Best,
Paroz Mehta
```

**Rules:** All outreach < 150 words. Be specific about what you want. Lead with value. Follow up within 48 hours of any meeting.

---

## Step 7: Company Research Brief

Use web search to gather current information. Follow `_Career/03-Networking/07_COMPANY_RESEARCH.md` methodology.

### Brief Template

```markdown
# [Company] - Research Brief for [Role Title]
## Prepared: [Date]

### Company Overview
- Industry, size, HQ, founded
- Revenue / funding stage / market cap
- Key products/services

### Strategic Priorities (Current)
- [Priority 1 from recent news/earnings]
- [Priority 2]
- [Priority 3]

### Recent News (Last 3 Months)
- [Headline + 1-sentence summary]
- [Headline + 1-sentence summary]

### Culture & Values
- From job posting: [culture signals extracted]
- From Glassdoor/LinkedIn: [notable patterns]

### Why This Company (Paroz's Talking Points)
1. [Authentic connection to experience]
2. [Strategic alignment with career goals]
3. [Specific value he can add]

### Key People to Know
- Hiring Manager: [Name, title]
- Team Lead: [Name, title]
- Cornell Alumni at Company: [Search LinkedIn]

### Potential Interview Questions (Company-Specific)
1. "Why [Company]?" -> [prepared answer]
2. "What do you know about our [initiative]?" -> [prepared answer]
3. "How would you approach [company challenge]?" -> [prepared answer]
```

### Output File
- `_Career/03-Networking/Company-Briefs/[Company]_Research_Brief.md`

---

## Step 8: Interview Prep Cheat Sheet

### Cheat Sheet Template

```markdown
# [Company] - [Role] Interview Prep
## Quick Reference Cheat Sheet

### Role Fit Summary
- Match Score: [X]% keyword alignment
- Strongest Matches: [top 3 areas]
- Gaps to Address: [areas to reframe]

### 60-Second Pitch (customized for this role)
[Tailored version of the pitch]

### Top 10 Behavioral Questions + STAR Answers
1. "Tell me about yourself" -> [Customized 60-sec pitch]
2. "Why are you leaving your current role?" -> [Growth frame]
3. "Describe a time you led organizational change" -> STAR: Flexiti M&A / RBAC
4. "Tell me about a complex technical decision" -> STAR: Databricks vs GCP
5. "How do you manage cross-functional stakeholders?" -> STAR: CTO/CFO alignment
6. "Describe a failure and what you learned" -> STAR: [Select appropriate]
7. "How do you prioritize competing initiatives?" -> STAR: QuestBank + RBAC + Reporting
8. "Why [Company]?" -> [From Research Brief]
9. "Where do you see yourself in 5 years?" -> [Aligned with company trajectory]
10. "What questions do you have for us?" -> [5 questions below]

### Questions to Ask Them
1. What does success look like in this role in the first 90 days?
2. What's the biggest challenge the team/org is facing right now?
3. How does this role contribute to [specific company strategy]?
4. What's the team structure and who would I be working with?
5. What's the interview process from here?

### Salary Negotiation Anchors (BATNA Framework)
- Market range for [role] in [location]: [research]
- Paroz's target: [based on experience + EMBA]
- BATNA: Current role at Questrade + other applications in pipeline
- Anchor high, justify with: Cornell EMBA, $1.5M+ portfolio, cross-cultural leadership
- Never give a number first
- Negotiate the package, not just salary
```

### Output File
- `_Career/02-Interview-Prep/Cheat-Sheets/[Company]_[Role]_Interview_Prep.md`

---

## Step 9: Notion Hunt Hub Logging

**Database:** Target Companies (`2c4d6eae-fc07-49dd-879a-b78c6a97da8e`)
**Data Source:** `collection://89c2e54c-d592-45c5-a866-03b47392535f`

### Create or Update Entry

| Field | Value |
|-------|-------|
| **Name** | [Company Name] |
| **Company Type** | Auto-classify: MBB / Tier 2 Consulting / Big 4 / Tech Company / Finance/PE/VC / Corporate Strategy / Startup |
| **Industry** | Auto-classify: Management Consulting / Technology / Financial Services / Healthcare / Consumer/Retail / Energy / Other |
| **Priority** | Auto-assess based on role fit + career strategy alignment (P0-P3) |
| **Application Status** | "Applied" |
| **Next Step** | "Follow up on application; send networking outreach" |
| **Next Date** | [Application date + 7 days] |
| **Contacts** | [Names from research brief, if found] |
| **Notes** | "[Role Title] | Match: [X]% | Resume: Paroz_Mehta_Resume_[Company]_[Role-Short] | Applied [date]" |
| **Website** | [Company career page URL if available] |

**If company already exists in the database:** Update Application Status, Next Step, Next Date, and Notes rather than creating a duplicate.

---

## Step 10: Delivery

Present all deliverables to Paroz in a structured summary:

```
## Application Package for [Company] - [Role]

### Match Analysis
- Overall keyword match: [X]%
- Strongest fit areas: [list]
- Gaps addressed in cover letter: [list]
- VRIN positioning: [1-sentence unique value for this role]

### Deliverables Created
1. Resume (.docx + .pdf): [file paths]
2. Cover Letter (.docx + .pdf): [file paths]
3. LinkedIn Outreach: [3 variants presented above]
4. Company Brief: [file path]
5. Interview Prep: [file path]
6. Notion Hunt Hub: [entry created/updated]

### Recommended Next Steps
1. Review and personalize all documents (15 min)
2. Submit application via [LinkedIn / company site]
3. Send networking outreach to [specific contacts]
4. Set follow-up reminder for [date + 7 days]
5. Begin interview prep using cheat sheet
```

---

## Post-Application Feedback Loop

After submitting, Claude should ask:
1. Did you get a response? -> Update Notion tracker status
2. Did you get an interview? -> Trigger deep interview prep from `interview-prep.md`
3. What feedback did you receive? -> Log patterns for system improvement
4. Any new contacts made? -> Add to networking tracker

---

## Cross-References

| Resource | Location | Used For |
|----------|----------|----------|
| JOB_APPLICATION.SKILL.md | `_Career/_skills/` | Detailed skill execution reference |
| RESUME_TAILORING.SKILL.md | `_Career/_skills/` | Keyword matching algorithm |
| INTERVIEW_PREP.SKILL.md | `_Career/_skills/` | STAR story bank |
| NETWORKING.SKILL.md | `_Career/_skills/` | Outreach templates |
| LINKEDIN_OPTIMIZATION.SKILL.md | `_Career/_skills/` | Profile keywords |
| CAREER_HUB.SKILL.md | `_Career/_skills/` | Master flywheel |
| career-strategy.md | `Knowledge/Career/` | VRIN, positioning, targets |
| interview-prep.md | `Knowledge/Career/` | CARL/STAR bank, 24 projects |
| strategy.md | `Knowledge/EMBA/` | VRIN framework |
| marketing.md | `Knowledge/EMBA/` | STP framework |
| Negotiation.SKILL.md | `Knowledge/EMBA/Skills/` | BATNA for salary |
| `docx` skill | Claude Code skill | Word document generation |
| `pdf` skill | Claude Code skill | PDF generation |

---

## Notion Hunt Hub Quick Reference

| Resource | Page ID |
|----------|---------|
| Hunt Hub (root) | `28b7b88e-336f-819f-95d3-f401c882015b` |
| Target Companies DB | `2c4d6eae-fc07-49dd-879a-b78c6a97da8e` |
| Personal Brand & Applications | `c1e9708f-0a3a-404b-bfdb-e3dd9d5e0339` |
| Interview Preparation | `9ed01144-f99e-4cc5-9de6-8c11c042ff59` |
| Networking & Outreach | `4a8d9227-bd5d-4889-97c8-c75905fb7df8` |
| Consulting Industry & Firms | `3980b891-7174-4a68-9e84-8aaccf08a1da` |
| Frameworks & Case Prep | `b4fd31d0-b280-4c40-96af-67fd8adf9731` |

---

*This workflow is the primary entry point for all job applications. Paste a job description to activate.*
*Last Updated: 2026-03-15*
