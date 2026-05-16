# Skill: /onboard — Deep Career Intake Interview

## Purpose
Conduct a 25-question intake interview to build a complete career profile. This is the foundation for every other skill. Without a complete profile, every output is generic. Generic output does not get people hired.

## Instructions
Ask the questions in 5 groups of 5. After each group, briefly summarize what you heard before moving to the next group. This shows you're listening and catches misunderstandings early.

Do NOT ask all 25 at once. Conversation, not interrogation.

At the end, write all answers to `profile.yml`, set `onboarding_completed: true` and `onboarding_date: [today's date]`, and confirm with the user that the file is saved.

---

## Opening Script
"Great — let's build your Career Command Center profile. I'll ask you 25 questions across 5 topics. It takes about 15 minutes and everything I produce for you from now on will be grounded in what you tell me here. Ready? Let's start with the basics."

---

## Group A — Identity (Questions 1–5)
1. What is your name?
2. How would you describe your current situation in one sentence? (e.g., employed and exploring, actively searching, recently laid off, returning after a break)
3. How many years of total professional experience do you have?
4. What are the 1–3 specific job titles you are targeting? Be as precise as you can.
5. What seniority level are you targeting? (e.g., Senior IC, Team Lead, Manager, Director, VP, C-suite)

**After Group A:** "Got it — [Name], [X] years of experience, targeting [roles] at [seniority]. That's a clear target. Now let's talk about where and what kind of company."

---

## Group B — Target Profile (Questions 6–10)
6. Which industries are you most interested in? (Name up to 3. It's okay to say "open.")
7. What geographies are you targeting? Include remote if applicable.
8. What work arrangement do you prefer — fully remote, hybrid, or on-site?
9. What is your work authorization status? (e.g., citizen, permanent resident, requires sponsorship)
10. What is your ideal company size? (startup under 200, mid-market 200–2000, enterprise 2000+, or open)

**After Group B:** "Good — [geography], [arrangement], [authorization], [size]. That narrows the playing field meaningfully. Now let's talk strategy and what's actually going on."

---

## Group C — Strategy and Pain Points (Questions 11–15)
11. How urgently do you need to land? (e.g., I have 3 months of runway, I'm passively exploring, I'm leaving in 6 months regardless)
12. What is not working in your job search right now? Be honest — this is the most important question.
13. What is the biggest gap in your current materials? (resume, LinkedIn, cover letters, interview skills, network)
14. On a scale of 1–5, how comfortable are you with networking and cold outreach? (1 = I avoid it, 5 = I genuinely enjoy it)
15. What is your target total compensation range? Include base, bonus, equity if relevant. Include currency.

**After Group C:** "This is the real picture — [urgency], [what's broken], [biggest gap], networking at [score], targeting [comp]. This shapes everything we do together. Let's go deeper into your background."

---

## Group D — Skills and Stories (Questions 16–20)
16. What are your top 3 technical or domain-specific skills? (e.g., SQL, financial modelling, product roadmapping, data governance)
17. What are your top 3 soft skills or leadership qualities? (e.g., stakeholder alignment, cross-functional communication, driving ambiguity to clarity)
18. What is the one professional accomplishment you are most proud of? One sentence — keep it tight.
19. What is the biggest career challenge or pivot you have navigated? What did you learn from it?
20. What are your key credentials? (degrees, certifications, notable programs — include school if relevant)

**After Group D:** "Strong foundation — [skills], [credentials], and a clear story around [accomplishment]. One more group and we'll have everything we need."

---

## Group E — Deep Intake (Questions 21–25)
21. Do you have 1–3 dream or target companies you'd love to work for? (It's okay to say you don't know yet.)
22. What is the filename or version of the resume you are currently using? (e.g., resume-v2-pm.pdf, Jan 2025 version)
23. What is the furthest stage you have reached in a job search interview process? (e.g., applied and heard nothing, phone screen, final round, offer extended)
24. What has been your biggest stumble or failure point in interviews so far? Be specific.
25. What is one thing you wish a career coach had told you earlier in your career?

---

## Closing Script
"That's the full picture. Here's what I heard: [brief 3-sentence synthesis of the whole profile]. I'm writing this to your profile.yml now.

Once I've saved it, every resume I tailor, every cover letter I write, every interview I prep you for — it all starts here. Run `/tailor-resume`, `/linkedin-optimize`, or `/prep-interview` whenever you're ready."

---

## File Write Instructions
After collecting all answers, update `profile.yml` with every field. Use the exact YAML keys defined in the file. Set:
- `onboarding_completed: true`
- `onboarding_date: [today's date in YYYY-MM-DD format]`

Confirm to the user: "Profile saved to profile.yml. Your Career Command Center is live."
