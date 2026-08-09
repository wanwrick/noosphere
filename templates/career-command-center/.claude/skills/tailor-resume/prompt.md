# Skill: /tailor-resume — Job Posting to Tailored Resume

## Purpose
Take a specific job posting and produce tailored resume bullet points, a keyword gap analysis, and a summary section — all grounded in the user's actual background from `profile.yml`.

## Instructions

### Step 1 — Load context
Read `profile.yml`. Note the user's target role(s), top skills, key accomplishments, and credentials.

### Step 2 — Get the job posting
Ask: "Paste the full job posting text here. Include the job title, company, and all requirements."

### Step 3 — Analyse the posting
Extract and present:
- **Role summary** (1 sentence): What this role actually does
- **Must-have requirements** (bullet list)
- **Nice-to-have requirements** (bullet list)
- **Implicit signals** (culture keywords, pace, team size, technical depth)
- **ATS keywords** — exact phrases from the posting that should appear verbatim in the resume

### Step 4 — Gap analysis
Compare ATS keywords and must-haves against the user's profile. Identify:
- **Strong matches** (user clearly has this — highlight)
- **Partial matches** (user has adjacent experience — reframe)
- **Gaps** (user lacks this — flag honestly, suggest mitigation)

### Step 5 — Tailored bullet points
Write 6–8 resume bullet points tailored to this specific role.

**Formula for every bullet:** `[Strong action verb] + [what you did, specific to this role's needs] + [quantified outcome or scale]`

**Rules:**
- Use ATS keywords from the posting verbatim where truthful
- Never invent accomplishments — work from what the user told you in profile.yml
- If a quantified outcome is unknown, prompt: "Do you have a number for this? Even an estimate (e.g., reduced time by ~30%) is better than nothing."
- Lead with the most relevant bullets for this specific role

### Step 6 — Summary section
Write a 2–3 sentence resume summary (not objective statement) that:
- Opens with the user's title/seniority and years of experience
- Names their top 2 relevant skills for this role
- Closes with what they bring that maps to this role's core challenge

### Step 7 — Confidence rating
Rate match confidence: High / Medium / Low — and explain why in one sentence.

### Closing
"Save these bullets to `templates/resume-template.md` under a section named for this role and company. Run `/write-cover-letter` next if you want the full application package."
