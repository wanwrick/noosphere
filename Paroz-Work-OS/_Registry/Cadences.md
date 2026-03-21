# Cadences & Rituals Registry

> Recurring work rituals, review cycles, and communication cadences. Reference for scheduling and preparation.

---

## Daily

| Ritual | Time | Duration | Format | Purpose |
|--------|------|----------|--------|---------|
| Standup | Morning | 15 min | Async (Slack) or sync | Blockers, progress, plans |

### Standup Format
```
📊 Yesterday: [What I completed]
🎯 Today: [What I'm working on]
⚠️ Blockers: [What needs help]
```

---

## Bi-Weekly (Sprint Cadence)

| Ritual | Day | Duration | Attendees | Purpose |
|--------|-----|----------|-----------|---------|
| Sprint Planning | Monday (Sprint Day 1) | 2 hours | DataWizards team | Commit to sprint scope |
| Sprint Review | Friday (Sprint Day 10) | 1 hour | Team + stakeholders | Demo deliverables |
| Retrospective | Friday (Sprint Day 10) | 45 min | DataWizards team | Process improvement |

### Sprint Planning Checklist
- [ ] Backlog groomed and prioritized
- [ ] Stories estimated (Fibonacci)
- [ ] Capacity calculated (account for PTO, meetings)
- [ ] Dependencies identified
- [ ] Sprint goal defined in one sentence

### Retrospective Format
```
🟢 What went well?
🔴 What didn't go well?
🔄 What will we change?
⭐ Action items (max 3, with owners)
```

---

## Weekly

| Ritual | Day | Duration | Attendees | Purpose |
|--------|-----|----------|-----------|---------|
| 1-on-1s | Varies | 30 min each | Direct reports | Coaching, growth, blockers |
| Notion Meeting Sync | Sunday 8 PM | Automated | Claude (scheduled task) | Sync week's Notion meeting notes into Work OS local files |

### 1-on-1 Agenda Template
1. **Their items** (always first — it's their meeting)
2. **Progress on growth goals**
3. **Blockers I can help with**
4. **Context sharing** (company/team updates)
5. **Feedback** (SBI format if needed)

---

## Monthly

| Ritual | When | Duration | Audience | Purpose |
|--------|------|----------|----------|---------|
| Stakeholder Update | Last week | 30 min | VP Eng, VP Product | 3P status (Progress/Plans/Problems) |
| Team Health Check | First week | 30 min | DataWizards team | Pulse check, morale, concerns |

### Monthly Update Prep
- [ ] Gather sprint metrics (velocity, quality, delivery)
- [ ] Update key metrics dashboard
- [ ] Draft 3P update using `Templates/status-update.md`
- [ ] Identify decisions needed from leadership
- [ ] Prepare one "win story" to highlight

---

## Quarterly

| Ritual | When | Duration | Audience | Purpose |
|--------|------|----------|----------|---------|
| PI Planning | Start of quarter | Half day | Extended team | Quarterly goals, dependencies |
| Roadmap Review | Mid-quarter | 1 hour | Leadership | Strategy alignment, reprioritization |
| Performance Check-ins | End of quarter | 1 hour each | Direct reports | IDP review, growth objectives |

### Quarterly Prep Checklist
- [ ] Review and update GOALS.md priorities
- [ ] Refresh stakeholder map and engagement strategy
- [ ] Conduct team skills assessment
- [ ] Prepare roadmap update for leadership
- [ ] Draft individual development plans
- [ ] Review decision log for patterns

---

## Annual

| Ritual | When | Purpose |
|--------|------|---------|
| Performance Reviews | Q4 / Q1 | Formal performance assessment |
| Compensation Review | Q1 | Market analysis, promotion cases |
| Team Strategy Day | January | Annual vision, mission, objectives |
| Personal Growth Review | December | Reflect on year, set next year goals |

---

## Ad-Hoc (Trigger-Based)

| Trigger | Ritual | Reference |
|---------|--------|-----------|
| Production incident | Incident response | `Workflows/incident-response.md` |
| Major decision needed | Decision memo | `Templates/decision-memo.md` |
| Post-incident | Root cause analysis | `Templates/rca-template.md` |
| Negotiation coming up | Negotiation prep | `Workflows/negotiation-prep.md` |
| Executive presentation | Briefing prep | `Workflows/executive-briefing.md` |
| Data insight to share | Data storytelling | `Workflows/data-storytelling.md` |

---

### Weekly Notion Meeting Sync
**Scheduled task:** `weekly-notion-sync` (Sunday 8 PM, automated)
**What it does:** Queries Notion for the past week's meeting notes, compares against 5 local Work OS files (GOALS.md, collaborators.md, q1-strategy.md, datawizards.md, access-management.md), and imports all new learnings.
**To run manually:** Ask Claude "run the weekly Notion sync" or re-create the scheduled task if it has expired.
**First created:** v1.4.1 (2026-03-20)

---

*Last updated: 2026-03-20*
