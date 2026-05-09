# System Evolution Log

> Changelog for the Noosphere system. Track additions, modifications, and structural changes.

---

## Version History

### v1.0.0 -- 2026-03-20 -- Initial Release
**Created by:** Paroz Mehta + Claude

**Structure:** See `README.md` for the full directory tree.

**Sources:**
- Business frameworks across 8 domains
- Professional skills distilled into templates, workflows, and work context
- MCP connectors registered in MCPs.md
- Your work context, team info, and communication preferences

**Design Decisions:**
- Full framework content preserved (not distilled) for depth
- Notion kept as live reference via MCP (not snapshotted)
- Portable as zip; works in both Cowork and Claude Code
- Self-reinforcing via feedback.md and decision logs

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-03-20 | v1.0 Initial creation | Build portable Noosphere from frameworks + work knowledge |
| 2026-03-21 | v1.1.0 Self-improvement loop + verification system | Add auto-optimization so the system improves each session, not just accumulates corrections |
| 2026-03-22 | v1.1.1 Diagram guidelines, README cleanup, gitignore hardening | Excalidraw design constraints added to CLAUDE.md; CONTRIBUTING.md and LICENSE added to directory tree; .excalidraw files excluded from repo |
| 2026-05-02 | v1.1.2 Placeholder convention fix in playbooks.md | CDO Deliverables row 8 ("Data Monetization") used `TBD` for owner while every other row used `[Your Name]` / `[Team Name]`. Aligned with the bracket-placeholder convention defined in CONTRIBUTING.md |

---

### v1.1.0 -- 2026-03-21 -- Self-Improvement Loop
**Author:** Paroz Mehta + Claude Sonnet 4.6

**What changed:**

| File | Change |
|------|--------|
| `Workflows/self-improvement.md` | New. Auto-Loader, Auto-Improver (3-pass verification), Autoresearch loop, Version Discipline |
| `CLAUDE.md` | Session Protocol expanded to 5 steps. Step 3 now includes three verification passes (framework, BLUF, action). Step 5 added: Self-Improvement Check. Routing rule 12 added for self-improvement workflow. |
| `Templates/decision-memo.md` | Pre-Delivery Verification section added (BLUF, options completeness, action ownership) |
| `Templates/status-update.md` | Pre-Delivery Verification section added (metrics on every bullet, solution with every problem) |
| `Templates/rca-template.md` | Pre-Delivery Verification section added (blameless check, 5 Whys independence, action ownership) |
| `Templates/user-story.md` | Pre-Delivery Verification section added (testable AC, edge cases, dependency confirmation) |
| `Workflows/data-storytelling.md` | Verification Loop section added (insight pyramid integrity, visualization BLUF) |
| `Workflows/executive-briefing.md` | Verification Loop section added (BLUF, Pyramid Principle, audience check, action specificity) |
| `Workflows/incident-response.md` | Verification Loop section added (resolution proof, post-mortem blameless check) |
| `Workflows/negotiation-prep.md` | Verification Loop section added (BATNA reality check, anchor preparation, post-deal documentation) |
| `README.md` | "What's New in v1.1" section added. Directory updated to 32 files. How to Extend updated. |

**Design Decisions:**
- Verification loops placed at end of each file (not inline) to keep the workflow readable on first pass
- Three-pass verification (framework, BLUF, action) mirrors a consulting peer review: content, communication, execution
- Autoresearch loop adapts Karpathy's pattern for knowledge work: score → mutate → re-score
- Boris Jeltsky (AI PM build-in-public) credited in self-improvement.md and README
- Version incremented as minor (1.0 → 1.1) because a new workflow file was added

**Gap that triggered this update:** No structured mechanism existed to improve the system based on session learnings. Corrections went into feedback.md but no loop closed back to system-level fixes.

---

### v1.1.1 -- 2026-03-22 -- Diagram Guidelines and Repo Hygiene
**Author:** Paroz Mehta + Claude Opus 4.6

**What changed:**

| File | Change |
|------|--------|
| `CLAUDE.md` | Diagram Generation section added: pastel palette, L-to-R layout, spacing rules, overlap guard, sketch aesthetic |
| `.gitignore` | `*.excalidraw` added to prevent local diagram files from being committed |
| `README.md` | Directory tree updated to include CONTRIBUTING.md and LICENSE at root |
| `_Logs/evolution.md` | v1.0.0 placeholders (`[Date]`, `[Your Name]`) replaced with actual values |

**Design Decisions:**
- Excalidraw files are local review artifacts; the generator script produces them on demand
- Design constraints documented in CLAUDE.md so every future session enforces the same visual standards
- Version incremented as patch (1.1.0 to 1.1.1) because only existing files were edited

---

### v1.1.2 -- 2026-05-02 -- Placeholder Convention Fix
**Author:** Paroz Mehta + Claude Opus 4.7

**What changed:**

| File | Change |
|------|--------|
| `Knowledge/Work/playbooks.md` | CDO Top 10 Deliverables table, row 8 (Data Monetization): owner cell changed from `TBD` to `[Your Name]` to match the bracket-placeholder convention used by every other row in the same table |

**Gap that triggered this update:** `CONTRIBUTING.md` mandates that all personalizable content uses bracket syntax (`[Your Name]`, `[Team Name]`, etc.). The `TBD` value was the only deviation from this convention in the repo and would surface as an inconsistent placeholder during fork-and-customize workflows.

**Design Decisions:**
- Kept `[Your Name]` for parity with rows 1, 7, and 10 (other owner-only rows)
- Version incremented as patch (1.1.1 to 1.1.2) because only an existing file was edited and no new file or routing rule was added

---

### v1.2.0-phase9 -- 2026-05-09 -- Practice OS Registries Refresh
**Author:** Paroz Mehta + Claude Opus 4.7

**What changed:**

| File | Change |
|------|--------|
| `_Registry/Cadences.md` | Added Practice OS Rituals section: sanitization audit (pre-commit), weekly practice synthesis, governance audit gate, attribution lint, IP coverage check, diagram refresh. Sanitization hook flow + weekly synthesis format documented. |
| `_Registry/MCPs.md` | Added GitHub + Diagram (mermaid/svg) MCPs. Reframed Notion as the live reference (always fetch by page ID). GitHub MCP scope and diagram-MCP usage rules added under Important Notes. |
| `_Registry/Archetypes.md` | New registry: 5-archetype index (codename, sector, type, phase, tier, regulated, DPIA) + IP coverage matrix + governance gate reminder + file map. Pointer back to `initiatives/initiatives.yaml`. |

**Closes:** Phase 9 of the v1.2.0 Practice OS extension (PR #3). Archetype dossiers and `initiatives.yaml` were already complete; this commit refreshes the three `_Registry/` files to reflect v1.2.0 (Skills.md is intentionally deferred to Phase 10 when the 7 new skills + 3 atomic subagents land).

**Design Decisions:**
- Phase tag in version (`v1.2.0-phase9`) keeps the evolution log honest about WIP. Final `v1.2.0` stamp lands in Phase 14 per PR description.
- Did not refresh `_Registry/Skills.md` here. Phase 10 will add the v1.2.0 skills as a single coherent change, not a partial preview.
- `_Registry/Archetypes.md` is a derived index, not a source of truth. `initiatives.yaml` remains canonical.

---

### v1.2.0-phase10 -- 2026-05-09 -- Practice OS Skills + Atomic Subagents
**Author:** Paroz Mehta + Claude Opus 4.7

**What changed:**

| File / dir | Change |
|------|--------|
| `.claude/skills/claude-md-bootstrap/SKILL.md` | New: generate the CLAUDE.md routing brain for forks / new repos. |
| `.claude/skills/data-source-10q-intake/SKILL.md` | New: runs the 10-question intake; produces `data-contract.yml` + 2-page brief. |
| `.claude/skills/dabs-template-init/SKILL.md` | New: bootstraps a DABs project from `templates/dabs-data-product-template/`. |
| `.claude/skills/governance-audit/SKILL.md` | New: 7-check pre-phase-advance audit (DPIA, classification, masking, retention, erasure, access, jurisdiction). |
| `.claude/skills/ai-consumption-contract/SKILL.md` | New: authors per-agent AI Consumption Contract (5 Principles + 6-question rubric). |
| `.claude/skills/defending-ai-spend-memo/SKILL.md` | New: 12-question (Hewing) memo with No LAC + Platinum architectural defence. |
| `.claude/skills/weekly-practice-synthesis/SKILL.md` | New: Friday weekly retro ritual with punch list. |
| `.claude/agents/dq-validator.md` | New atomic subagent: DQ section verdict only. |
| `.claude/agents/schema-reviewer.md` | New atomic subagent: schema modeling review against authored + curated IP. |
| `.claude/agents/compliance-checker.md` | New atomic subagent: cross-reference contract against `compliance-register.yaml`. |
| `.gitignore` | Whitelisted `.claude/agents/` alongside `.claude/skills/`. |
| `_Registry/Skills.md` | Added Practice OS Skills + Atomic Subagents tables; bumped Last updated stamp. |

**Closes:** Phase 10 of the v1.2.0 Practice OS extension (PR #3).

**Design Decisions:**
- Skills live at `.claude/skills/<name>/SKILL.md` per Claude Code convention so they auto-register and become invocable as `/<name>`.
- Subagents at `.claude/agents/<name>.md` for the same auto-registration. Each subagent is single-purpose with explicit boundary statements (no scope creep).
- The seven skills mirror the practice's actual end-to-end engagement loop: bootstrap repo → intake source → init DABs → audit governance → contract AI consumption → defend spend → synthesize weekly.
- The three subagents are intentionally narrow so the parent skill can compose them without re-implementing focused checks.
- Attribution preserved (Invariant #3): `defending-ai-spend-memo` cites Hewing as the curated 12-question source; authored IP (No LAC, Platinum) is the answer pattern, not blurred together.
