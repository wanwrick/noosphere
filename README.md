# Work OS Template

A portable, self-contained knowledge management system that turns Claude into an AI work partner with full access to business frameworks, operational context, reusable templates, and step-by-step workflows.

**29 files. Zero external dependencies. Fork it, customize it, make it yours.**

---

## Why This Exists

Three problems this system solves:

1. **Knowledge silos.** Frameworks across finance, strategy, marketing, leadership, operations, economics, technology, and governance sit in notebooks and slide decks. They should be in every working session.

2. **Context switching.** Each new AI conversation starts from scratch. The system loads priorities, team context, past corrections, and communication preferences automatically.

3. **Framework amnesia.** Knowing Porter's Five Forces exists is different from applying it consistently when the situation calls for it. The system routes questions to the right framework every time.

---

## Architecture

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
     +---> Knowledge/Frameworks/  (business frameworks, theory, analysis tools)
     +---> Knowledge/Work/        (team, tech stack, stakeholders, playbooks)
     +---> Templates/             (document formats: memo, status, RCA, story)
     +---> Workflows/             (step-by-step: incident, briefing, negotiation)
     +---> _Registry/             (skills, MCPs, cadences)
     +---> Notion MCP             (live data: sprint status, meeting notes)
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
|  KNOWLEDGE LAYER       Knowledge/Frameworks/ + Knowledge/Work/|
|  8 business domains + operational context files               |
+---------------------------------------------------------------+
|  CORE LAYER            CLAUDE.md + GOALS.md                   |
|  Routing brain + current priorities (P0-P3)                   |
+---------------------------------------------------------------+
```

---

## Directory Structure

```
work-os-template/
+-- CLAUDE.md                       System brain + routing
+-- GOALS.md                        Priorities + OKRs
+-- Knowledge/
|   +-- Frameworks/                 8 business domain files
|   |   +-- finance.md              DCF, WACC, CAPM, LBO, accounting, valuation
|   |   +-- strategy.md             Porter's 5F, VRIN, blue ocean, game theory, CAGE
|   |   +-- leadership.md           Transformational, teams, org behavior, presentations
|   |   +-- operations.md           Little's Law, VUT, EOQ, lean/TPS, queueing
|   |   +-- governance.md           Agency theory, board composition, exec comp
|   |   +-- economics.md            Supply/demand, game theory, GDP, policy
|   |   +-- marketing.md            STP, 4Ps, JTBD, CLV/CAC, brand equity
|   |   +-- technology.md           Digital transformation, GenAI strategy, AI governance
|   +-- Work/                       Operational context files
|   |   +-- team.md                 Team structure, platform, Agile practices
|   |   +-- platform.md             Technical reference with code patterns
|   |   +-- communication.md        PREP, SBI, SUCCESS, email/meeting protocols
|   |   +-- playbooks.md            Critical SOPs and decision frameworks
|   |   +-- collaborators.md        Key people and interaction guidelines
|   +-- Decisions/
|       +-- _template.md            Decision log format
+-- Templates/                      4 reusable document formats
|   +-- decision-memo.md            Executive 3-pager
|   +-- status-update.md            3P format (Progress/Plans/Problems)
|   +-- rca-template.md             Root cause analysis (blameless)
|   +-- user-story.md               Agile story format
+-- Workflows/                      4 step-by-step playbooks
|   +-- incident-response.md        SEV-based crisis playbook
|   +-- negotiation-prep.md         BATNA + power dynamics + tactics
|   +-- executive-briefing.md       Board deck / C-suite prep
|   +-- data-storytelling.md        Insight pyramid + visualization guide
+-- _Registry/                      System metadata
|   +-- Skills.md                   All available skills inventory
|   +-- MCPs.md                     Connected services reference
|   +-- Cadences.md                 Recurring rituals and schedules
+-- _Logs/                          Learning system
    +-- feedback.md                 Corrections and preferences
    +-- evolution.md                System changelog
```

---

## Getting Started

### Step 1: Fork and Clone
Fork this repository and clone it locally. This becomes your project folder for Claude Code or Cowork.

### Step 2: Personalize the Core (30 min)
- **CLAUDE.md**: Replace `[Your Name]`, `[Company Name]`, `[Team Name]`, and `[Platform Name]` placeholders with your info. Keep the session protocol and routing rules structure.
- **GOALS.md**: Replace with your P0-P3 priorities, current initiatives, key metrics, and decision principles.

### Step 3: Replace Knowledge (1-2 hours)
- **Knowledge/Frameworks/**: Keep the 8 domain files and add your own frameworks, or replace with your specialized knowledge areas.
- **Knowledge/Work/**: Replace team context, platform details, communication preferences, playbooks, and collaborator info with your own.

### Step 4: Customize Templates & Workflows (30 min)
Review the 4 templates and 4 workflows. Keep what applies, swap what doesn't, add new ones for your recurring needs.

### Step 5: Configure the Registry (15 min)
- **Skills.md**: List your available Claude Code skills
- **MCPs.md**: List your connected services
- **Cadences.md**: Define your recurring rituals

### Step 6: Initialize the Learning Loop (5 min)
- **feedback.md**: Start empty; the system populates it as Claude learns your preferences
- **evolution.md**: Add your v1.0 entry

### Step 7: Test It (15 min)
1. Ask a cross-domain question. Verify Claude routes to the right knowledge files.
2. Ask Claude to create a document. Verify it uses the correct template.
3. Correct Claude on something. Verify it logs the correction to feedback.md.
4. Ask for help with a task. Verify it references GOALS.md.

---

## Design Principles

| Principle | How It Works |
|-----------|-------------|
| **Token Efficiency** | Notion Reference Map with page IDs for targeted lookups; local-first before MCP |
| **Frameworks First** | Every recommendation grounded in a named, referenced framework |
| **Portable** | Works as a zip file; no database, no server, no build step |
| **Learning Loop** | `feedback.md` captures corrections; the system never repeats mistakes |
| **Action-Oriented** | Every concept paired with a template or workflow that produces real output |

---

## MCP Integrations (Optional)

The system works fully offline with local files. When connected, these services add live data:

| Service | What It Adds |
|---------|-------------|
| **Notion** | Sprint data, meeting notes, initiative status |
| **Gmail** | Email search and draft composition |
| **Google Calendar** | Schedule and availability |
| **Google Drive** | Shared docs and reports |
| **Canva** | Presentations and visual assets |
| **Figma** | UI/UX design context |

---

## How to Extend

| Goal | Action |
|------|--------|
| Add a knowledge domain | Create a file in `Knowledge/Frameworks/` or `Knowledge/Work/`, add routing rule to CLAUDE.md |
| Add a template | Create a file in `Templates/`, reference in CLAUDE.md |
| Add a workflow | Create a file in `Workflows/`, add trigger to Cadences.md |
| Log a decision | Copy `Knowledge/Decisions/_template.md`, fill in context and outcome |
| Add an MCP | Update `_Registry/MCPs.md` and `_Registry/Skills.md` |
| Update priorities | Edit `GOALS.md` at the start of each quarter |

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Claude ignores Knowledge files | CLAUDE.md routing rules don't match | Update routing rules to reference new file names |
| Responses are too generic | GOALS.md not loaded | Verify GOALS.md exists and Session Protocol references it |
| Same mistake repeated | feedback.md not being read | Check Session Protocol step 1 includes feedback.md |
| Notion fetches fail | Page IDs incorrect or MCP not connected | Verify page IDs; check MCP connection status |
| Claude doesn't use templates | Templates not referenced in routing | Add template routing rules to CLAUDE.md |

---

## License

MIT. See [LICENSE](LICENSE) for details.

---

*Originally designed by Paroz Mehta.*
