# Skill: /write-cover-letter — Cover Letter Generator

## Purpose
Write a specific, compelling cover letter for a specific job posting. Generic cover letters are ignored. This skill produces a letter that sounds like the user wrote it, not like a template.

## Instructions

### Step 1 — Load context
Read `profile.yml`. Note name, target roles, top skills, proudest accomplishment, and key credentials.

### Step 2 — Get the posting
Ask: "Paste the full job posting here, including the job title and company name."

### Step 3 — Extract the hook
From the posting, identify:
- The core problem this role solves for the company
- The 1–2 must-have qualifications that matter most
- Any specific language the company uses to describe themselves

### Step 4 — Write the cover letter

**Format:** 4 paragraphs. No filler. No "I am writing to apply for." Maximum 350 words.

**Paragraph 1 — Why this role:**
Open with a sentence that shows you understand what this role is really for. Not "I am excited to apply." Something like: "The [Title] role at [Company] is fundamentally about [the real challenge] — and that's the problem I've spent [X] years solving."

**Paragraph 2 — Why this company:**
1–2 specific, researched reasons. Not "I admire your culture." Use something real — a product decision, a recent move, a stated value. Ask the user: "What specifically drew you to this company? Give me one real thing." Build from that.

**Paragraph 3 — Why me:**
Lead with the user's strongest accomplishment relevant to this role (from profile.yml or user-provided). Follow with 1–2 additional qualifications that directly address the must-haves from the posting. Use numbers.

**Paragraph 4 — Call to action:**
One sentence: express genuine interest and invite next steps. Do not beg. Do not use "I look forward to hearing from you."

### Step 5 — Tone check
After writing, flag:
- Any generic phrases → rewrite with specific detail
- Any "I" starts to 3+ consecutive sentences → restructure
- Any word over 3 syllables that has a simpler substitute → swap

### Step 6 — Personalisation prompt
Ask: "Is there anything specific about why you want THIS company that I should weave in? A conversation you had, a product you use, a news item that got your attention?"

Incorporate the answer into Paragraph 2.

### Closing
"Save this to `templates/cover-letter-template.md` with the company and role noted at the top. Run `/tailor-resume` if you haven't tailored your resume for this posting yet."
