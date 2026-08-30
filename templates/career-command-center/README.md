# Career Command Center

A personal job search operating system powered by Claude Code. Open this folder in Claude Code and your AI career coach is ready.

---

## What this is

The Career Command Center is a structured folder you mount in Claude Code. It gives Claude everything it needs to act as a genuine career coach — not a generic chatbot. Every session is grounded in your real profile, your real pipeline, and your real goals.

Designed for: active job seekers, people making a career pivot, and anyone who wants to run a smarter, faster, less stressful search.

---

## Setup (5 minutes)

### 1. Install Claude Code
Download from [claude.ai/code](https://claude.ai/code) or install the VS Code extension.

### 2. Open this folder
```
code career-command-center/
```
Or open the folder directly in Claude Code via File → Open Folder.

### 3. Start your first session
Claude Code will automatically detect you are a new user and begin the onboarding interview. Answer the 25 questions honestly — everything Claude produces from that point on is grounded in your answers.

**That's it.** No API keys, no configuration, no plugins.

---

## First session

When you open Claude Code in this folder for the first time, you will see:

> "NEW USER — profile.yml is empty. Begin onboarding."

Claude will immediately start the intake interview (~15 minutes). At the end, your `profile.yml` is populated and your Career Command Center is live.

---

## Commands (slash commands)

| Command | What it does |
|---|---|
| `/onboard` | Run the full intake interview (or re-run to refresh your profile) |
| `/tailor-resume` | Paste a job posting → get tailored bullet points + keyword analysis |
| `/linkedin-optimize` | Audit and rewrite your LinkedIn profile |
| `/prep-interview` | Full interview prep package for a specific role |
| `/write-cover-letter` | Generate a tailored cover letter for a specific posting |
| `/weekly-review` | Friday pipeline check + next week plan |

---

## Folder map

```
career-command-center/
├── profile.yml          ← your profile (gitignored — never committed)
├── GOALS.md             ← your career targets and metrics (gitignored)
├── job-search/          ← applications, target companies, ATS keywords
├── interview-prep/      ← STAR stories, question bank, interview retros
├── career-strategy/     ← positioning narrative, compensation, 90-day plan
├── templates/           ← master resume, cover letters, STAR template
├── Workflows/           ← weekly ritual, application retro
├── bootstrap.sh         ← creates your working files from the .example set
└── _Logs/               ← session log (gitignored)
```

Every file that holds personal data ships as a tracked `.example` template.
`bootstrap.sh` copies each to its live filename on first session start, and
`.gitignore` keeps the live copy out of git. You get a working folder; git
never sees your data.

---

## Important: privacy

**Your personal data is gitignored by default.** You do not have to configure
anything, and there is no first-commit window in which it is exposed.

Ten files are protected this way: `profile.yml`, `GOALS.md`,
`_Logs/session-log.md`, both files under `job-search/` that name real
companies, both `interview-prep/` files, and all three `career-strategy/`
files. Generated résumés and cover letters (`*.pdf`, `*.docx`,
`resume-*.md`, `cover-letter-*.md`) are ignored too — those carry your name,
address, phone, and email in a single document.

This matters beyond your own privacy. `target-companies.md` and
`interview-retro.md` ask you to record recruiter and interviewer names.
**That is other people's personal data, and it is not yours to publish.**

Two things the tooling cannot do for you:

- **Check `git status` before your first push.** If you added files of your
  own, confirm none of them carries personal data.
- **Set your commit identity.** `git log` publishes your email on every
  commit forever. To use GitHub's privacy address instead:
  ```
  git config user.email "<your-id>+<username>@users.noreply.github.com"
  ```
  Find yours under GitHub → Settings → Emails → *Keep my email address
  private*. Set this **before** your first commit; it does not apply
  retroactively.

---

## How to get the most from this

1. **Complete onboarding properly.** Vague answers produce generic outputs. Be specific.
2. **Use `/tailor-resume` for every application.** Mass-applying with one resume does not work.
3. **Build your STAR bank early.** 8–10 stories covers almost any interview.
4. **Run `/weekly-review` every Friday.** It takes 15 minutes and prevents stale pipelines.
5. **Ask follow-up questions.** Claude remembers your profile within the session — use it.

---

## Feedback and improvement

This is your folder — modify it to fit your style. Add new sections, new templates, new questions. If a skill prompt is not producing what you need, edit the `prompt.md` file inside `.claude/skills/[skill-name]/`.
