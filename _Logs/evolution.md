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
| 2026-04-05 | v1.2.0 LLM Knowledge Base pattern + self-linting + provenance | New framework (llm-knowledge-bases.md), workflow (knowledge-base-ops.md), auto-index (Index.md), provenance layer (_Sources/), knowledge article template, KB lint (self-improvement.md Part 5), lint cadence |

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

### v1.2.0 -- 2026-04-05 -- LLM Knowledge Base Pattern + Self-Linting + Provenance
**Author:** Paroz Mehta + Claude Opus 4.6

**What changed:**

| File | Change |
|------|--------|
| `Knowledge/Frameworks/llm-knowledge-bases.md` | New. LLM-as-author wiki pattern: ingest, compile, index, query, output, lint. Includes architecture, 5 pipeline stages, design principles, scaling considerations, comparison with RAG/vector/graph approaches, and "Applying This to Noosphere" section mapping the pattern to this system |
| `Workflows/knowledge-base-ops.md` | New. Operational playbook for building and maintaining LLM knowledge bases. General-purpose with Noosphere-specific annotations. Covers setup, ingest, query, output, lint, maintenance cadences, tool development |
| `_Registry/Index.md` | New. Auto-maintained content index with one-line summaries of every file, organized by directory. Replaces the need to scan CLAUDE.md routing for file descriptions |
| `_Sources/README.md` | New. Provenance conventions: inline source sections, raw material storage, front matter format, image sources |
| `Templates/knowledge-article.md` | New. Standard format for compiled wiki articles: definition, frameworks, application, cross-references, sources, pre-delivery verification |
| `Workflows/self-improvement.md` | Part 5 added: Knowledge Base Lint with 5 checks (index freshness, cross-reference integrity, gap detection, staleness, structure consistency) |
| `_Registry/Cadences.md` | Lint cadence added to ad-hoc triggers: monthly or after 3+ files added |
| `CLAUDE.md` | Session Protocol Step 1: Index.md added for ambiguous domain routing. Step 5: Index.md freshness check added. Routing rule 6: knowledge base ops added to workflow list. Routing rule 13: expanded to include lint operations |
| `README.md` | File count updated to 37. Directory tree: added Index.md, _Sources/, knowledge-article.md. Design Principles: added Provenance and Self-Linting. How to Extend: added source material, lint pass, knowledge article rows |
| `_Logs/evolution.md` | This entry |

**Design Decisions:**
- Index.md is the highest-value single addition: makes LLM file discovery faster than scanning routing rules
- KB Lint integrated into existing self-improvement.md (Part 5) rather than a separate workflow, to avoid parallel systems
- Provenance layer is deliberately lightweight (_Sources/ with conventions) rather than a full ingest pipeline, appropriate for a 37-file hand-curated system
- The LLM KB framework article grounds itself in Noosphere's own architecture via "Applying This to Noosphere" section, avoiding the trap of describing a separate system
- The workflow file uses inline Noosphere annotations (blockquotes) to show how each general step maps to this specific system
- Version incremented as minor (1.1.1 to 1.2.0) because 5 new files were added

**Gap that triggered this update:** No framework existed for the LLM-as-author knowledge base pattern. The system lacked a content index (forcing reliance on CLAUDE.md routing descriptions), had no provenance tracking, and had no structural lint checks beyond the autoresearch loop's gap detection
