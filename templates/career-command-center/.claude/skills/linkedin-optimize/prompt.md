# Skill: /linkedin-optimize — LinkedIn Profile Audit and Rewrite

## Purpose
Audit the user's current LinkedIn profile and produce specific rewrites for every major section. Generic LinkedIn advice is worthless — every output must be grounded in `profile.yml` and the user's specific target roles.

## Instructions

### Step 1 — Load context
Read `profile.yml`. Note target roles, target industries, years of experience, top skills, key accomplishments, credentials.

### Step 2 — Get current profile content
Ask the user to paste the text from each section they want audited. At minimum: Headline, About/Summary, and the most recent 2–3 Experience entries.

If they cannot paste it, ask them to describe each section briefly and work from that.

### Step 3 — Audit (score each section 1–5)
Score and comment on:
| Section | Score | Biggest issue |
|---|---|---|
| Headline | | |
| About | | |
| Experience (most recent) | | |
| Skills section (presence + order) | | |
| Profile completeness overall | | |

**Scoring criteria:**
- 5: Recruiter stops scrolling. Target role is obvious. Compelling outcome in first 10 words.
- 3: Readable but generic. Could be anyone.
- 1: Job description copy-paste. No outcomes. Will not rank in recruiter search.

### Step 4 — Headline rewrite
Write 3 headline variants. Formula: `[Target title] | [Top differentiator] | [Industry or credential]`

Max 220 characters. Lead with what the user wants to be found for, not their current title.

### Step 5 — About section rewrite
Write a full About section (1,200–1,500 characters):
- **Hook** (first 2 lines must work as the preview before "see more"): What you do and for whom. Make it specific.
- **Core value prop** (2–3 sentences): What you uniquely bring, grounded in profile.yml skills and accomplishments.
- **Recent wins** (2–3 bullets): Specific, quantified outcomes.
- **What you are looking for** (1 sentence): Clear signal for recruiters.
- **Call to action** (1 sentence): How to reach you.

### Step 6 — Experience bullet rewrites
For each Experience entry provided, rewrite the bullets using:
`[Strong action verb] + [what you did] + [quantified outcome]`

Add ATS-friendly keywords that match the user's target roles from `profile.yml`.

### Step 7 — Skills section recommendations
Based on target roles and profile.yml skills, recommend:
- Top 5 skills to pin (most searchable by recruiters for these roles)
- 5–10 additional skills to add if not present

### Step 8 — Quick wins checklist
List 5 actions the user can take in the next 30 minutes:
- [ ] Update headline to Version [X] above
- [ ] Replace About section
- [ ] Add [specific missing skill] to skills
- [ ] Request [N] endorsements for [top skill]
- [ ] Turn on "Open to Work" (recruiters only, not public) if actively searching

### Closing
"Save the rewritten sections to `job-search/target-companies.md` or directly update your LinkedIn. Run `/tailor-resume` to make your resume consistent with the new positioning."
