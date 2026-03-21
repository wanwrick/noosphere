# Paroz Work OS v1.5

A portable, self-contained knowledge management system that turns Claude into an AI work partner with full access to 29 MBA courses, operational context, reusable templates, and step-by-step workflows.

**106 files. 29,428 lines. Zero external dependencies.**

---

## Why This Exists

Three problems this system solves:

1. **Knowledge silos.** 29 EMBA courses across finance, strategy, marketing, leadership, operations, economics, technology, and governance sit in notebooks and slide decks. They should be in every working session.

2. **Context switching.** Each new AI conversation starts from scratch. The system loads priorities, team context, past corrections, and communication preferences automatically.

3. **Framework amnesia.** Knowing Porter's Five Forces exists is different from applying it consistently when the situation calls for it. The system routes questions to the right framework every time.

---

## Design Principles

| Principle | How It Works |
|-----------|-------------|
| **Token Efficiency** | Notion Reference Map with 30+ page IDs for targeted lookups; local-first before MCP |
| **Frameworks First** | Every recommendation grounded in a named, referenced framework |
| **Portable** | Works as a zip file; no database, no server, no build step |
| **Learning Loop** | `feedback.md` captures corrections; the system never repeats mistakes |
| **Action-Oriented** | Every concept paired with a template or workflow that produces real output |

---

## Architecture Overview

### System Flow

```
User Request
     |
     v
+-----------+
| CLAUDE.md |  Reads GOALS.md (priorities) + feedback.md (past corrections)
+-----------+
     |
     v
  Route to domain(s)
     |
     +---> Knowledge/EMBA/     (frameworks, theory, analysis tools)
     +---> Knowledge/Work/     (team, tech stack, stakeholders, playbooks)
     +---> Templates/          (document formats: memo, status, RCA, story)
     +---> Workflows/          (step-by-step: incident, briefing, negotiation)
     +---> _Registry/          (skills, MCPs, cadences)
     +---> Notion MCP          (live data: sprint status, meeting notes)
     |
     v
  Execute + Verify
     |
     v
  Log learnings to _Logs/feedback.md
```

### Four Layers

```
+---------------------------------------------------------------+
|  SYSTEM LAYER          _Registry/ + _Logs/                    |
|  Skills, MCPs, cadences, feedback, version history            |
+---------------------------------------------------------------+
|  ACTION LAYER          Templates/ + Workflows/                |
|  Document formats + step-by-step operational playbooks        |
+---------------------------------------------------------------+
|  KNOWLEDGE LAYER       Knowledge/EMBA/ + Knowledge/Work/      |
|  29 courses (8 domains) + operational context (5 files)       |
+---------------------------------------------------------------+
|  CORE LAYER            CLAUDE.md + GOALS.md                   |
|  Routing brain + current priorities (P0-P3)                   |
+---------------------------------------------------------------+
```

---

## Component Reference

### System Core (2 files, 377 lines)

| File | Lines | Purpose |
|------|-------|---------|
| `CLAUDE.md` | 289 | System brain: identity, routing rules, session protocol, Notion reference map, behavioral instructions |
| `GOALS.md` | 88 | Current priorities (P0-P3), Q1 2026 initiatives, decision principles, key metrics |

### Knowledge Layer: EMBA (8 files, 1,745 lines)

29 Cornell-Queen's EMBA courses consolidated into 8 domain files.

| File | Lines | Courses | Key Frameworks |
|------|-------|---------|---------------|
| `finance.md` | 312 | 6 courses | DCF, WACC, CAPM, LBO, accounting, valuation |
| `strategy.md` | 278 | 6 courses | Porter's 5F, VRIN, blue ocean, game theory, CAGE |
| `leadership.md` | 275 | 5 courses | Congruence Model, transformational, teams, presentations, critical thinking |
| `operations.md` | 210 | 1 course | Little's Law, VUT, EOQ, lean/TPS, queueing |
| `governance.md` | 202 | 1 course | Agency theory, board composition, exec comp, shareholder activism |
| `economics.md` | 160 | 2 courses | Supply/demand, game theory, GDP, monetary/fiscal policy |
| `marketing.md` | 158 | 2 courses | STP, 4Ps, JTBD, CLV/CAC, brand equity |
| `technology.md` | 150 | 3 courses | Digital transformation, GenAI strategy, AI governance |

### Knowledge Layer: Work Context (5 files, 998 lines)

| File | Lines | Purpose |
|------|-------|---------|
| `datawizards.md` | 243 | Team structure (5 engineers), QuestBank architecture, Agile practices, strategic frameworks |
| `databricks.md` | 319 | Medallion architecture with code, Unity Catalog, DLT, ABAC security, Power BI patterns |
| `communication.md` | 263 | PREP, SBI, BLUF, SCQA, SUCCESS frameworks; email, meeting, presentation protocols |
| `questbank-playbooks.md` | 127 | Three critical frameworks: 10Q data onboarding, CDO Top 10 deliverables, Data Contracts |
| `collaborators.md` | 46 | Key team members, cross-functional partners, interaction guidelines |

### Knowledge Layer: Decisions (1 file, 35 lines)

| File | Lines | Purpose |
|------|-------|---------|
| `_template.md` | 35 | Decision log format: context, options, criteria, decision, outcome tracking |

### Action Layer: Templates (4 files, 303 lines)

| File | Lines | When to Use |
|------|-------|-------------|
| `decision-memo.md` | 74 | Executive 3-pager: The Ask (SCQA), Analysis (options table), Execution (plan + metrics) |
| `rca-template.md` | 97 | Blameless post-mortem: timeline, 5 Whys, after-action review, corrective actions |
| `user-story.md` | 79 | Agile story: As a / I want / So that, Gherkin acceptance criteria, subtask breakdown |
| `status-update.md` | 53 | Monthly 3P format: Progress (metrics), Plans (milestones), Problems (blockers + risks) |

### Action Layer: Workflows (4 files, 490 lines)

| File | Lines | Trigger |
|------|-------|---------|
| `incident-response.md` | 114 | Platform alert or production issue; SEV-1/2/3 classification |
| `data-storytelling.md` | 131 | Building dashboards, reports, or presenting data insights |
| `executive-briefing.md` | 114 | Preparing for board, C-suite, or senior leadership presentations |
| `negotiation-prep.md` | 131 | Budget discussions, vendor negotiations, scope negotiations |

### System Layer: Registry (3 files, 263 lines)

| File | Lines | What It Tracks |
|------|-------|---------------|
| `Skills.md` | 80 | 55 available skills: 4 document, 29 EMBA, 18 professional, 4 Notion |
| `MCPs.md` | 63 | 6 connected services: Notion, Gmail, Google Calendar, Drive, Canva, Figma |
| `Cadences.md` | 120 | Recurring rituals: daily standup, sprint ceremonies, 1-on-1s, quarterly reviews |

### System Layer: Learning Loop (2 files, 147 lines)

| File | Lines | Purpose |
|------|-------|---------|
| `feedback.md` | 45 | Corrections and preferences captured per session; prevents repeat mistakes |
| `evolution.md` | 102 | System changelog: v1.0 (initial), v1.1 (self-review), v1.2 (Notion integration) |

---

## How the Routing Works

CLAUDE.md uses a domain-based routing system. When a question arrives:

1. **Load context:** Read GOALS.md for priorities, feedback.md for past corrections
2. **Classify the domain:** EMBA theory? Work context? Document creation? Process? Live data?
3. **Route to files:**

| Question Type | Primary Route | Secondary Route |
|--------------|---------------|-----------------|
| Strategic analysis | Knowledge/EMBA/strategy.md | GOALS.md for priority context |
| Financial modeling | Knowledge/EMBA/finance.md | Knowledge/Work/databricks.md for data context |
| Team management | Knowledge/EMBA/leadership.md | Knowledge/Work/datawizards.md for team context |
| Incident response | Workflows/incident-response.md | Knowledge/Work/communication.md for messaging |
| Document creation | Templates/ (select format) | Knowledge/Work/communication.md for style |
| Data platform task | Knowledge/Work/questbank-playbooks.md | Notion MCP for live status |
| Meeting prep | _Registry/Cadences.md | Workflows/executive-briefing.md for deck prep |

4. **Execute with verification:** Cross-check against Knowledge files, apply BLUF + evidence standards
5. **Close loop:** Log corrections to feedback.md, summarize open items

---

## MCP Integrations

The system works fully offline with local files. When connected, these MCPs add live data:

| Service | What It Adds | Token Efficiency |
|---------|-------------|-----------------|
| **Notion** | Sprint data, meeting notes, initiative status | Reference Map with 30+ page IDs (no broad search) |
| **Gmail** | Email search and draft composition | Draft-only; send requires confirmation |
| **Google Calendar** | Schedule and availability | Meeting prep context |
| **Google Drive** | Shared docs and reports | Document retrieval |
| **Canva** | Presentations and visual assets | Design generation |
| **Figma** | UI/UX design context | Design system reference |

---

## How to Extend

| Goal | Action |
|------|--------|
| Add a knowledge domain | Create `Knowledge/EMBA/newdomain.md` or `Knowledge/Work/newtopic.md`, add routing rule to CLAUDE.md |
| Add a template | Create `Templates/newtemplate.md`, reference in CLAUDE.md routing section |
| Add a workflow | Create `Workflows/newworkflow.md`, add trigger to Cadences.md |
| Log a decision | Copy `Knowledge/Decisions/_template.md`, fill in context and outcome |
| Add an MCP | Update `_Registry/MCPs.md` and `_Registry/Skills.md` |
| Update priorities | Edit `GOALS.md` at the start of each quarter |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0.0 | 2026-03-06 | Initial release: 25 files, 8 EMBA domains, 3 work context files, full template and workflow suite |
| v1.1.0 | 2026-03-06 | Self-review: 24 issues fixed, 31 warnings addressed, 8 notes resolved. Stress test: 10/10 |
| v1.2.0 | 2026-03-07 | Notion integration: 30+ page IDs in Reference Map, 2 new work files (questbank-playbooks, collaborators), session protocol rewrite, token efficiency rules |

---

## Directory Structure

```
Paroz-Work-OS/
├── CLAUDE.md                       (289 lines) System brain + routing
├── GOALS.md                        (88 lines)  Priorities + OKRs
├── Knowledge/
│   ├── EMBA/                       (1,745 lines total)
│   │   ├── finance.md              (312)  6 courses
│   │   ├── strategy.md             (278)  6 courses
│   │   ├── leadership.md           (275)  5 courses
│   │   ├── operations.md           (210)  1 course
│   │   ├── governance.md           (202)  1 course
│   │   ├── economics.md            (160)  2 courses
│   │   ├── marketing.md            (158)  2 courses
│   │   └── technology.md           (150)  3 courses
│   ├── Work/                       (998 lines total)
│   │   ├── datawizards.md          (243)  Team + platform
│   │   ├── databricks.md           (319)  Tech reference
│   │   ├── communication.md        (263)  Frameworks
│   │   ├── questbank-playbooks.md  (127)  Critical SOPs
│   │   └── collaborators.md        (46)   Key people
│   └── Decisions/
│       └── _template.md            (35)   Decision log format
├── Templates/                      (303 lines total)
│   ├── decision-memo.md            (74)   Executive 3-pager
│   ├── rca-template.md             (97)   Post-mortem
│   ├── user-story.md               (79)   Agile story
│   └── status-update.md            (53)   3P format
├── Workflows/                      (490 lines total)
│   ├── incident-response.md        (114)  Crisis playbook
│   ├── data-storytelling.md        (131)  Insight pyramid
│   ├── executive-briefing.md       (114)  Board deck prep
│   └── negotiation-prep.md         (131)  BATNA + tactics
├── _Registry/                      (263 lines total)
│   ├── Skills.md                   (80)   55 skills
│   ├── MCPs.md                     (63)   6 connectors
│   └── Cadences.md                 (120)  Recurring rituals
├── _Logs/                          (147 lines total)
│   ├── feedback.md                 (45)   Corrections
│   └── evolution.md                (102)  Changelog
└── docs/                           (this folder)
    ├── README.md                   You are here
    ├── ARCHITECTURE.md             Technical deep-dive
    ├── QUICKSTART.md               Adaptation guide
    ├── linkedin-post.md            External communication
    └── internal-pitch.md           Leadership pitch
```

---

*Built by Paroz Mehta, Cornell-Queen's EMBA CA26.*
*System designed with Claude (Anthropic).*
