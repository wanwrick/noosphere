# Quickstart: Build Your Own Work OS

This guide walks you through adapting the Paroz Work OS for your own use. The system is designed to be forked and customized, not used as-is.

**Time estimate:** 2-3 hours for a working v1.0.

---

## Prerequisites

- **Claude Code** or **Cowork** (Claude desktop app with project support)
- A folder you can point Claude at as a project
- (Optional) MCP connectors: Notion, Gmail, Google Calendar, etc.

---

## Step 1: Copy the Structure (5 minutes)

Download or copy the `Paroz-Work-OS/` folder. This is your starting template.

Keep the directory structure intact. The naming conventions (Knowledge/, Templates/, Workflows/, etc.) are part of the routing system.

---

## Step 2: Personalize the Core (30 minutes)

### CLAUDE.md: Your System Brain

**What to change:**

| Section | What to Replace |
|---------|----------------|
| Identity | Your name, title, company, team |
| Profile: Role & Context | Your role, platform, key project |
| Communication Style | Your preferences (or keep these; they are solid) |
| Decision-Making Preferences | Your decision style |
| Working Patterns | Your work habits |
| Notion Reference Map | Your Notion page IDs (or remove if not using Notion) |

**What to keep:**
- Session Protocol structure (Load, Plan, Execute, Close Loop)
- Routing rules framework (customize destinations, keep the pattern)
- Error handling approach
- Behavioral Instructions patterns (adjust the specifics, keep the structure)

### GOALS.md: Your Priorities

Replace all content with:
- Your P0-P3 priority hierarchy
- Your current quarter's initiatives
- Your key metrics
- Your decision principles

**Update this file quarterly.** It is the filter for every request.

---

## Step 3: Replace Knowledge (1-2 hours)

### Knowledge/EMBA/ --> Your Domain Expertise

If you have an MBA or specialized training, create one file per domain:

```
Knowledge/YourDomain/
├── finance.md          Your financial frameworks
├── strategy.md         Your strategy frameworks
├── leadership.md       Your leadership models
└── [your-domain].md    Any specialized knowledge
```

If you don't have MBA content, replace this with whatever knowledge domains you want Claude to reference: industry expertise, technical specializations, research areas, etc.

**Format each file with:**
- Header explaining what it contains
- Tables for frameworks (concise, scannable)
- "When to Use" quick reference at the bottom of each section

### Knowledge/Work/ --> Your Work Context

| File to Replace | What to Put In |
|-----------------|---------------|
| `datawizards.md` | Your team: members, roles, tech stack, Agile practices |
| `databricks.md` | Your technical reference: architecture, code patterns, tooling |
| `communication.md` | Your communication frameworks (or keep Paroz's; they are general-purpose) |
| `questbank-playbooks.md` | Your critical SOPs and decision frameworks |
| `collaborators.md` | Your key stakeholders and interaction guidelines |

---

## Step 4: Customize Templates (30 minutes)

Review all four templates. Keep, modify, or replace based on your output needs:

| Template | Keep If... | Replace If... |
|----------|-----------|---------------|
| `decision-memo.md` | You write executive memos | Your org uses a different format |
| `status-update.md` | You send monthly updates | You use a different status format |
| `rca-template.md` | You run post-mortems | You have a company-standard RCA |
| `user-story.md` | You write Agile stories | You use a different story format |

Add new templates for any recurring document type: weekly reports, project charters, design docs, etc.

---

## Step 5: Customize Workflows (30 minutes)

Review all four workflows. These are step-by-step playbooks for high-stakes situations:

| Workflow | Keep If... | Replace If... |
|----------|-----------|---------------|
| `incident-response.md` | You handle production incidents | Your org has a standard IR process |
| `data-storytelling.md` | You present data insights | You don't do data work |
| `executive-briefing.md` | You present to leadership | You rarely present to executives |
| `negotiation-prep.md` | You negotiate budgets/scope | You don't negotiate often |

Add workflows for your most common complex processes.

---

## Step 6: Configure the Registry (15 minutes)

### _Registry/Skills.md
List the skills (Claude Code skills or custom) available in your environment. This helps Claude know what tools it can use.

### _Registry/MCPs.md
List your connected services and how Claude should use each one. If you don't use MCPs, you can simplify this file.

### _Registry/Cadences.md
Define your recurring rituals: standup frequency, sprint cadence, review cycles, 1-on-1 schedule.

---

## Step 7: Initialize the Learning Loop (5 minutes)

### _Logs/feedback.md
Clear the existing entries but keep the format:

```markdown
| Date | Category | Context | Correction | Rule |
|------|----------|---------|------------|------|
```

The system will populate this as Claude learns your preferences.

### _Logs/evolution.md
Clear existing entries. Add your v1.0 entry:

```markdown
### v1.0.0 -- [today's date] -- Initial Release
Created by: [Your name] + Claude
[Brief description of what you included]
```

---

## Step 8: Test It (15 minutes)

Run these tests to verify the system works:

1. **Cross-domain question:** Ask something that spans two knowledge domains. Verify Claude routes to both files and names the frameworks it applies.

2. **Document creation:** Ask Claude to create a document (memo, status update, etc.). Verify it uses the correct template and applies your communication style.

3. **Correction test:** Intentionally correct Claude on something. Verify it logs the correction to `_Logs/feedback.md`.

4. **Priority check:** Ask Claude to help with a task. Verify it references GOALS.md and maps the task to your priority hierarchy.

---

## Common Customizations

| "I want to..." | Do This |
|----------------|---------|
| Add a new knowledge domain | Create a file in `Knowledge/`, add a routing rule to CLAUDE.md |
| Change communication style | Edit `Knowledge/Work/communication.md` |
| Add a recurring ritual | Add it to `_Registry/Cadences.md` |
| Track a new MCP connector | Update `_Registry/MCPs.md` and `_Registry/Skills.md` |
| Add a new template | Create a file in `Templates/`, reference in CLAUDE.md |
| Add a new workflow | Create a file in `Workflows/`, add trigger to Cadences.md |
| Connect to Notion | Add page IDs to the Reference Map section in CLAUDE.md |
| Remove EMBA content | Delete `Knowledge/EMBA/` files, simplify routing in CLAUDE.md |

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

*For full system documentation, see [README.md](README.md). For technical architecture details, see [ARCHITECTURE.md](ARCHITECTURE.md).*
