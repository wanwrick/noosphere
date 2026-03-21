# Paroz Work OS: Technical Architecture

## Design Philosophy

Four architectural principles shape every design decision:

1. **Markdown-native.** No database, no server, no build step. The file system is the schema.
2. **Convention over configuration.** Directory structure and naming patterns enable routing without a separate config file.
3. **Local-first, live-second.** Stable frameworks live locally; live status data comes from Notion MCP when available.
4. **Self-documenting.** Every file has a header block explaining its purpose, so the system describes itself.

---

## Architectural Layers

The system is organized into four layers, each with a distinct role:

```
Layer 4: SYSTEM       _Registry/ (3 files) + _Logs/ (2 files)
                      What capabilities exist, what has been learned

Layer 3: ACTION       Templates/ (4 files) + Workflows/ (4 files)
                      How to produce output, how to handle situations

Layer 2: KNOWLEDGE    Knowledge/EMBA/ (8) + Knowledge/Work/ (5) + Decisions/ (1)
                      What Paroz knows: theory, context, past decisions

Layer 1: CORE         CLAUDE.md + GOALS.md
                      How to route questions, what matters right now
```

**Key insight:** Layers 1-2 are *read* resources (reference material). Layers 3-4 are *action* resources (they produce deliverables or track state). This separation keeps knowledge stable while actions evolve.

---

## Request Processing Pipeline

Every question follows the same path through the system:

```
                    +-------------+
                    | User        |
                    | Question    |
                    +------+------+
                           |
                           v
                  +--------+--------+
                  |   CLAUDE.md     |
                  |   (Router)      |
                  +--------+--------+
                           |
              +------------+------------+
              |                         |
              v                         v
     +--------+--------+      +--------+--------+
     |   GOALS.md       |      |   feedback.md   |
     |   (Priorities)   |      |   (Corrections) |
     +--------+--------+      +--------+--------+
              |                         |
              +------------+------------+
                           |
                           v
                  +--------+--------+
                  |   Classify      |
                  |   Domain(s)     |
                  +--------+--------+
                           |
         +---------+-------+-------+---------+
         |         |       |       |         |
         v         v       v       v         v
      EMBA/     Work/   Templ/  Wkflw/   Notion
     (theory)  (context) (fmt)  (proc)    (live)
         |         |       |       |         |
         +---------+-------+-------+---------+
                           |
                           v
                  +--------+--------+
                  |   Execute +     |
                  |   Verify        |
                  +--------+--------+
                           |
                           v
                  +--------+--------+
                  |   Output to     |
                  |   User          |
                  +--------+--------+
                           |
                           v
                  +--------+--------+
                  |   Log to        |
                  |   feedback.md   |
                  +--------+--------+
```

---

## Session Lifecycle

Each session follows four mandatory phases. No shortcuts.

### Phase 1: Load Context
- Read `GOALS.md` to understand P0-P3 priorities and active Q1 initiatives
- Read `_Logs/feedback.md` to load accumulated corrections
- Identify which domain(s) the session will touch

### Phase 2: Plan Before Execute
- State which files will be read
- Name the frameworks to be applied
- Define the output format (memo, analysis, code, etc.)
- Get confirmation before producing deliverables

### Phase 3: Execute with Verification
- Produce the deliverable
- Cross-check framework application against Knowledge/ files
- Verify output meets BLUF, brevity, and evidence standards
- For data/technical work: validate logic and check for errors

### Phase 4: Close the Loop
- If corrected, log it to `_Logs/feedback.md` immediately
- If a new pattern emerges, propose adding it
- Summarize accomplishments and flag open items

---

## Integration Architecture

### Local vs. Live Data

```
+---------------------------------------+
|         LOCAL FILES (always)           |
|                                        |
|  Knowledge/EMBA/    Stable theory      |
|  Knowledge/Work/    Team, tech, SOPs   |
|  Templates/         Document formats   |
|  Workflows/         Step-by-step       |
|  _Registry/         Capabilities       |
|  _Logs/             Learning loop      |
+---------------------------------------+
              |
              | (optional, when connected)
              v
+---------------------------------------+
|         NOTION MCP (live)              |
|                                        |
|  Sprint status      Initiative data    |
|  Meeting notes       Calendar events   |
|  Advanced topics     Semantic modeling  |
|  Multi-agent arch    AI Dev Kit        |
+---------------------------------------+
```

**Rule:** Check local files first. Only fetch Notion when you need live status or advanced topics not snapshotted locally.

### Token Efficiency Strategy

The Notion Reference Map in CLAUDE.md contains 30+ specific page IDs organized by topic:

| Category | Pages | Example Use |
|----------|-------|-------------|
| Data Platform & Ingestion | 6 pages | Onboarding new data sources |
| Data Modeling & Semantic | 5 pages | Lakehouse modeling strategy |
| AI & Agentic Analytics | 7 pages | Multi-agent architecture |
| Strategy & Leadership | 4 pages | CDO-level planning |
| Team & Process | 3 pages | Meeting design, leadership systems |
| Live Databases | 2 databases | Sprint data, initiative status |

**Five rules for token-efficient Notion access:**
1. Never search broadly; always fetch by page ID
2. Check local files first
3. Batch related lookups in parallel
4. Don't re-fetch in the same session
5. For meeting/sprint data, query the database, not the hub page

### MCP Connector Topology

```
+-------------------+
|   Claude Session  |
+--------+----------+
         |
    +----+----+
    | MCP Hub |
    +----+----+
         |
    +----+----+----+----+----+----+
    |    |    |    |    |    |    |
    v    v    v    v    v    v    |
  Notion Gmail GCal Drive Canva Figma
  (wiki) (email)(sched)(docs)(design)(UI)
```

Each connector is optional. The system degrades gracefully: all core knowledge lives in local files.

---

## Example Scenarios

### Scenario 1: Incident Response (SEV-2 Alert)

```
Trigger: Production data pipeline failure
    |
    v
CLAUDE.md routes to --> Workflows/incident-response.md
    |
    v
Phase 1: Detection & Triage (0-15 min)
  - Classify severity (SEV-2: major impact, not total outage)
  - Read Knowledge/Work/collaborators.md for escalation contacts
  - Notify stakeholders per severity matrix
    |
    v
Phase 2: Investigation (15 min - 2 hours)
  - Read Knowledge/Work/databricks.md for technical patterns
  - Check Notion for recent pipeline changes (MCP fetch)
    |
    v
Phase 3: Resolution + Communication
  - Read Knowledge/Work/communication.md for crisis messaging frameworks
  - Apply BLUF for stakeholder updates
    |
    v
Phase 4: Post-Mortem
  - Use Templates/rca-template.md for blameless RCA
  - Apply After Action Review (Knowledge/EMBA/leadership.md)
  - Log learnings to _Logs/feedback.md
```

### Scenario 2: Strategic Decision (Platform Investment)

```
Trigger: "Should we invest in a semantic layer for QuestBank?"
    |
    v
CLAUDE.md checks GOALS.md --> Maps to Initiative 4 (P2: Self-Serve Analytics)
    |
    v
Read Knowledge/EMBA/strategy.md --> Apply VRIN framework
  - Valuable? Enables self-serve analytics (reduces BI bottleneck)
  - Rare? Few Canadian fintechs have semantic layers
  - Inimitable? Complex to replicate (requires Unity Catalog + domain expertise)
  - Organized? DataWizards team has the capability
    |
    v
Read Knowledge/EMBA/finance.md --> Build ROI case
  - DCF analysis on BI analyst time savings
  - Payback period calculation
    |
    v
Use Templates/decision-memo.md --> 3-page executive memo
  - Page 1: SCQA framing
  - Page 2: Options table (build vs. buy vs. defer) with evaluation
  - Page 3: Implementation plan + success metrics
    |
    v
Log decision to Knowledge/Decisions/
```

### Scenario 3: Data Platform Task (New Source Onboarding)

```
Trigger: "Onboard Braze marketing data into QuestBank"
    |
    v
CLAUDE.md checks GOALS.md --> Maps to Initiative 2 (P0: Marketing/Braze)
    |
    v
Read Knowledge/Work/questbank-playbooks.md --> Apply 10Q Framework
  - Volume, freshness, schema, quality, source type, incremental strategy,
    PII classification, rate limits, replay capability, gotchas
    |
    v
Read Knowledge/Work/databricks.md --> Select ingestion pattern
  - API source: use Auto Loader or Structured Streaming
  - Apply Medallion architecture (Bronze raw, Silver cleaned, Gold modeled)
    |
    v
Fetch Notion: Data Contracts page (3057b88e...) --> Define contract
  - Schema, freshness SLA, quality rules, ownership, versioning
    |
    v
Read Knowledge/Work/collaborators.md --> Identify partners
  - Martech Force team for Braze domain context
    |
    v
Use Templates/user-story.md --> Create sprint stories
  - Story points, acceptance criteria in Gherkin, subtask breakdown
```

---

## File Dependency Graph

Which files reference or depend on other files:

```
CLAUDE.md
  ├── reads --> GOALS.md (first thing every session)
  ├── reads --> _Logs/feedback.md (avoid past mistakes)
  ├── routes to --> Knowledge/EMBA/* (8 domain files)
  ├── routes to --> Knowledge/Work/* (5 context files)
  ├── routes to --> Templates/* (4 formats)
  ├── routes to --> Workflows/* (4 playbooks)
  ├── routes to --> _Registry/* (3 metadata files)
  └── references --> Notion page IDs (30+ pages)

Workflows/incident-response.md
  └── triggers --> Templates/rca-template.md (post-mortem)

Workflows/executive-briefing.md
  └── uses --> Knowledge/Work/communication.md (Pyramid Principle, SCQA)

Workflows/negotiation-prep.md
  └── uses --> Knowledge/Work/communication.md (pushback responses)

_Registry/Cadences.md
  ├── references --> Templates/status-update.md (monthly cadence)
  └── references --> Workflows/* (ad-hoc triggers)

GOALS.md
  └── references --> Notion database IDs (live initiative status)
```

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Full EMBA content, not distilled | Paroz prefers completeness; content is already table-formatted for efficiency |
| 8 domain files, not 29 course files | Token efficiency; most sessions touch 1-2 domains, not individual courses |
| 3 critical frameworks snapshotted locally | 10Q, CDO, Data Contracts are used frequently; portability over freshness |
| Advanced topics stay on Notion | Semantic modeling, multi-agent, AI Dev Kit are large and evolving; live reference is better |
| Routing rules in CLAUDE.md, not a separate router | Single entry point; no indirection; CLAUDE.md is always loaded first |
| feedback.md separate from evolution.md | Tactical corrections (feedback) vs. structural system changes (evolution) serve different purposes |
| Session protocol is mandatory | Prevents ad-hoc responses; ensures context loading and learning loop execution |
| Notion Reference Map uses page IDs | Broad search wastes tokens; targeted fetch by ID is 10x more efficient |

---

*For a guide on adapting this system for your own use, see [QUICKSTART.md](QUICKSTART.md).*
