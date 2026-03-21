# Communication Protocols — Work Reference

> Paroz's communication system integrating EMBA frameworks with professional practices. Covers email, presentations, meetings, stakeholder management, and async communication.

---

## 1. Core Communication Frameworks

### PREP (Impromptu Responses)
- **P**oint: State your main point clearly
- **R**eason: Explain why (one key reason)
- **E**xample: Give a specific, concrete example
- **P**oint: Restate your main point

Use for: standup updates, hallway questions, Q&A responses, Slack threads.

### SBI (Feedback)
- **S**ituation: When and where (specific context)
- **B**ehavior: What you observed (factual, not interpretive)
- **I**mpact: The effect of that behavior (on you, team, project)

Use for: 1-on-1 feedback, performance conversations, peer coaching.

### BLUF (Bottom Line Up Front)
Lead every written communication with the conclusion or key ask. Supporting details follow.

```
BAD:  "After reviewing the Q3 data and considering various factors..."
GOOD: "We need to delay the Gold layer release by 2 weeks. Here's why..."
```

### SCQA (Memos & Proposals)
- **S**ituation: What's the current state? (familiar context)
- **C**omplication: What's changed or gone wrong? (the tension)
- **Q**uestion: What should we do? (implied or explicit)
- **A**nswer: Your recommendation (with evidence)

### SUCCESS Principles (Making Ideas Stick)
- **S**imple: Core message in one sentence
- **U**nexpected: Break a pattern, create curiosity
- **C**oncrete: Specific examples, not abstract concepts
- **C**redible: Data, testimonials, demonstrations
- **E**motional: Make them feel something
- **S**tories: Wrap ideas in narrative

---

## 2. Email Protocol

### Subject Line Format
```
[ACTION/FYI/DECISION BY DATE]: Topic — Impact
```
Examples:
- `[DECISION BY FRI]: Gold Layer Scope — Affects Q2 Roadmap`
- `[FYI]: Sprint 14 Review Summary — On Track`
- `[ACTION]: Need Your Input on ABAC Design by Wednesday`

### Email Structure
```
SUBJECT: [Action type]: Topic — Impact

[BLUF: One sentence — what you need and why]

Context: [2-3 sentences max]

Options (if decision needed):
1. [Recommended] Option A — [impact]
2. Option B — [trade-off]

Next Step: [Specific action] by [date]

— Paroz
```

### Email Rules
- Under 5 sentences for routine updates
- Under 150 words for decisions
- One email = one topic = one ask
- Use bullet points only for parallel items
- Reply within 24 hours (even if just to acknowledge)
- CC only people who need to act or be informed

---

## 3. Presentation Protocol

### Monroe's Motivated Sequence (Persuasive Talks)
1. **Attention:** Hook (story, statistic, question)
2. **Need:** Establish the problem (make audience feel it)
3. **Satisfaction:** Present your solution
4. **Visualization:** Paint the future with/without
5. **Action:** Clear call to action

### RAMP Openings
- **R**hetorical Question: "What would happen if our data platform went down for a day?"
- **A**nalogy: "Think of QuestBank like the nervous system of the organization..."
- **M**etaphor: "We're building highways for data, not dirt roads"
- **P**ersonal Story: Brief, relevant, 30 seconds max

### Slide Design Rules
- **One message per slide** — title states the conclusion
- **10 slides max** for most presentations
- **70% visual, 30% text** — graphs, diagrams, images
- **No bullet points** on slides (use speaker notes instead)
- **Consistent branding** — company template, clean fonts

### Executive Presence During Presentations
- **Power of Pause:** 2 seconds after key points
- **Speak Third:** Considered, not eager or cautious
- **Language Upgrades:**
  | Instead of | Say |
  |------------|-----|
  | "I think" | "The data suggests" |
  | "Maybe we could" | "I recommend" |
  | "We're trying" | "We're on track to" |
  | "The problem is" | "The opportunity is" |

### Q&A Handling
```
Pause → Rephrase the question → Answer concisely → Bridge back to key message
```
- Never say "That's a great question" (filler, wastes time)
- "I don't know, but I'll find out by [date]" is always acceptable
- Prepare for the 3 toughest questions in advance

---

## 4. Meeting Protocol

### Meeting Types & Cadence
| Type | Duration | Frequency | Format |
|------|----------|-----------|--------|
| Daily Standup | 15 min | Daily | Async-first (Slack) or sync |
| Sprint Planning | 2 hours | Bi-weekly | Sync (collaborative) |
| Sprint Review | 1 hour | Bi-weekly | Sync (demo) |
| Retrospective | 45 min | Bi-weekly | Sync (facilitated) |
| 1-on-1 | 30 min | Weekly | Sync (direct reports) |
| Stakeholder Update | 30 min | Monthly | Sync or async |
| Roadmap Review | 1 hour | Quarterly | Sync (leadership) |

### Meeting Prep Checklist
- [ ] Clear objective stated in invite
- [ ] Agenda shared 24 hours in advance
- [ ] Pre-read distributed (if needed)
- [ ] Right people invited (no spectators)
- [ ] Decision rights defined (who decides?)
- [ ] Time-boxed agenda items

### Meeting Facilitation
- Start on time, end 5 minutes early
- State the objective and desired outcome upfront
- Use "parking lot" for off-topic items
- Round-robin for input (don't let one person dominate)
- Summarize decisions and action items before ending
- Send written summary within 2 hours

---

## 5. Stakeholder Communication

### Stakeholder Matrix
| Stakeholder | Communication Style | Frequency | Key Metric They Care About |
|-------------|-------------------|-----------|---------------------------|
| VP Engineering | Technical + business | Monthly | Platform reliability, velocity |
| VP Product | Business outcomes | Monthly | Feature delivery, user adoption |
| CTO | Strategic + technical | Quarterly | Architecture, innovation, risk |
| Compliance | Regulatory precision | As needed | Audit readiness, data governance |
| Analytics Team | Practical, hands-on | Weekly | Data quality, freshness, access |
| Business Units | Business impact | Quarterly | Insights, report accuracy |

### Adapting to Audience
| Audience | Lead With | Depth | Format |
|----------|----------|-------|--------|
| Executive | Business impact, numbers | High-level | BLUF + Pyramid Principle |
| Technical | Architecture, trade-offs | Deep | Diagrams + code examples |
| Cross-functional | Value delivered, timeline | Moderate | SCQA + visual summary |
| External/vendor | Requirements, SLAs | Moderate | Formal, documented |

---

## 6. Async Communication (Slack & Written)

### Slack Threading Strategy
- **Channel per context:** #datawizards-team, #questbank-platform, #inc-YYYY-MM-DD
- **Thread everything:** Keep channels scannable
- **Use reactions:** ✅ acknowledged, 👀 reviewing, 🎯 action taken
- **Format updates:**
  ```
  📊 Status Update: [Topic]
  ✅ Done: [What completed]
  🔄 In Progress: [What's happening]
  ⚠️ Blocked: [What needs help]
  📅 Next: [What's coming]
  ```

### Async Decision Framework (DACI)
- **D**river: Person driving the decision to completion
- **A**pprover: Person with final say
- **C**ontributors: People with input
- **I**nformed: People who need to know

### 3P Status Update Format
```
PROGRESS (What we accomplished):
- [Achievement 1 with metric]
- [Achievement 2 with metric]

PLANS (What's coming next):
- [Next milestone + target date]
- [Key initiative + owner]

PROBLEMS (What needs attention):
- [Blocker + proposed solution + help needed]
- [Risk + mitigation plan]
```

---

## 7. Difficult Conversations

### Vendor Escalation Template
```
Subject: [ESCALATION]: Issue with [Service] — Impact on [Project/Timeline]

Current Status: [Brief description of the problem]

Impact: [Quantified business impact — revenue, timeline, compliance]

Actions Taken: [What you've already done to resolve]

Ask: [Specific resolution needed] by [date]

Escalation Path: If unresolved by [date], we will escalate to [next level].
```

### Pushback Response Framework
1. **Acknowledge:** "I understand the concern about..."
2. **Reframe:** "Let me share a different perspective..."
3. **Evidence:** "The data shows..."
4. **Trade-off:** "Here's what we'd gain vs. what we'd lose..."
5. **Propose:** "I recommend we..."

### Saying No Constructively
Never say: "We can't do that."
Always say: "We can do that if we trade off..." or "Here's what we can deliver within those constraints..."

---

## Quick Reference: When to Use What

| Situation | Framework |
|-----------|-----------|
| Quick verbal response | PREP |
| Giving feedback | SBI |
| Writing an email | BLUF + Email Protocol |
| Writing a proposal/memo | SCQA |
| Making ideas memorable | SUCCESS |
| Persuasive presentation | Monroe's Motivated Sequence |
| Status update | 3P (Progress/Plans/Problems) |
| Making a team decision | DACI |
| Escalating an issue | Escalation Template |
| Handling pushback | Pushback Response Framework |
