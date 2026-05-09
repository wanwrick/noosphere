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
| Sprint Planning | Monday (Sprint Day 1) | 2 hours | [Team Name] team | Commit to sprint scope |
| Sprint Review | Friday (Sprint Day 10) | 1 hour | Team + stakeholders | Demo deliverables |
| Retrospective | Friday (Sprint Day 10) | 45 min | [Team Name] team | Process improvement |

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

### 1-on-1 Agenda Template
1. **Their items** (always first; it's their meeting)
2. **Progress on growth goals**
3. **Blockers I can help with**
4. **Context sharing** (company/team updates)
5. **Feedback** (SBI format if needed)

---

## Monthly

| Ritual | When | Duration | Audience | Purpose |
|--------|------|----------|----------|---------|
| Stakeholder Update | Last week | 30 min | VP Eng, VP Product | 3P status (Progress/Plans/Problems) |
| Team Health Check | First week | 30 min | [Team Name] team | Pulse check, morale, concerns |

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

## Practice OS Rituals (v1.2.0)

Practice-level rituals introduced with Noosphere v1.2.0. These run on top of the
team-level cadences above and are owned by the practice author, not by any one
client engagement.

| Ritual | Cadence | Trigger | Reference |
|--------|---------|---------|-----------|
| Sanitization Audit | Pre-commit + pre-push | Every commit touching tracked files | `Workflows/sanitization-pass.md`, `_Logs/sanitization-audit.md`, `scripts/lint_sanitization.sh` |
| Weekly Practice Synthesis | Weekly (Friday) | End-of-week reflection on engagements + IP | `weekly-practice-synthesis` skill (Phase 10) |
| Governance Audit Gate | Per archetype phase advance | `regulated: true` or `pii: true` in `initiatives.yaml` | `governance-audit` skill (Phase 10), `governance/compliance-register.yaml` |
| Attribution Lint | Pre-merge | Any change to `ip/curated/*.md` | `methodology/attribution-policy.md`, banned: blurring authored vs curated |
| IP Coverage Check | Per archetype change | `ip_applied` field added/changed in `initiatives.yaml` | `methodology/repository-conventions.md`, Invariant #1 |
| Diagram Refresh | Per architectural change | New IP file or routing change in `CLAUDE.md` | `methodology/diagram-generation.md`, `_Diagrams/` |

### Sanitization Audit Pre-Commit Hook
```
1. .pre-commit-config.yaml runs scripts/lint_sanitization.sh
2. gitleaks scan runs in parallel
3. Any banned-token match (employer / team / stakeholder / JIRA / vendor / workspace ID) blocks the commit
4. CI re-runs the same gate via .github/workflows/sanitization.yml
5. Findings logged to _Logs/sanitization-audit.md
```

### Weekly Practice Synthesis Format
```
This week's engagements: [archetype IDs touched]
IP applied: [authored + curated]
New corrections logged: [count from _Logs/feedback.md]
System fixes proposed: [count from _Logs/evolution.md]
Insight candidates: [POV ideas for insights/]
Open governance items: [DPIA, classification, masking gaps]
```

---

*Last updated: 2026-05-09 (v1.2.0 — Practice OS rituals added)*
