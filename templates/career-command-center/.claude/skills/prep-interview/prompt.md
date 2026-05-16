# Skill: /prep-interview — Interview Preparation

## Purpose
Build a complete, role-specific interview prep package in one session. Output includes a curated question bank, sample answers grounded in the user's STAR stories, and a company research brief.

## Instructions

### Step 1 — Load context
Read `profile.yml`. Note target role, top skills, accomplishments, biggest interview stumble, and furthest interview stage reached.

Also read `interview-prep/star-stories.md` if the user has populated it.

### Step 2 — Get specifics
Ask:
1. What is the exact role and company you are preparing for?
2. What stage is this interview? (recruiter screen, hiring manager, panel, case study, final round)
3. Do you have the job posting? If yes, paste it.
4. When is the interview?

### Step 3 — Company research brief
Produce a one-page research brief:
- **What the company does** (1 sentence — the honest version, not the PR version)
- **Business model** (how they make money)
- **Recent news** (ask user to check LinkedIn/Google for last 3 months — do not hallucinate news)
- **Known culture signals** (Glassdoor tone, interview style, values language)
- **Why this company now** (1–2 sentences the user can use verbatim in the interview)

### Step 4 — Question bank (role + stage specific)
Curate 12–15 questions likely for this specific interview, organized by type:

**Behavioural (STAR format required):**
Select 5–7 questions matched to the role's must-haves. Examples:
- Tell me about a time you delivered results under pressure.
- Describe a situation where you had to influence without authority.
- Give me an example of a time you failed. What did you do?

**Role-specific / technical:**
Select 3–5 questions based on the job posting requirements.

**Culture / values:**
Select 2–3 based on what you know about the company's values.

**Questions TO ASK them:**
Write 3–5 smart questions the user should ask the interviewer. These should signal strategic thinking, not just curiosity.

### Step 5 — STAR answer coaching
For the top 3 behavioural questions, coach the user through their answer:
1. Present the question
2. Ask: "What story from your experience would you use for this?"
3. Help them structure it: Situation (brief) → Task (your responsibility) → Action (what YOU did, not the team) → Result (quantified)
4. Offer a polished version they can practise

**Rules:**
- Action must be the longest part (60% of the answer)
- Result must include a number, even approximate
- Full answer should be 90–120 seconds when spoken
- Flag any "we" answers — coaching them to "I"

### Step 6 — Pitfall brief
Based on `profile.yml` biggest_interview_stumble, give 2–3 specific coaching notes to avoid repeating it.

### Step 7 — Day-of checklist
- [ ] Confirm interview time and format (video/phone/in-person)
- [ ] Test tech (camera, mic, background) if video
- [ ] Print or have open: this prep doc + 3 STAR stories
- [ ] Arrive / log in 5 minutes early
- [ ] Have water, notepad, copy of resume
- [ ] Silence phone completely

### Closing
"Save your STAR stories to `interview-prep/star-stories.md` so you can reuse them. Run `/write-cover-letter` if you haven't sent your application yet. Run the interview retro in `interview-prep/interview-retro.md` within 24 hours of the interview."
