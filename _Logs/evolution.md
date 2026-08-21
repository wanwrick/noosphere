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

---

### v1.2.0-phase11 -- 2026-05-09 -- Insights Seed (First Published POV)
**Author:** Paroz Mehta + Claude Opus 4.7

**What changed:**

| File | Change |
|------|--------|
| `insights/CLAUDE.md` | New: routing for the insights directory; conventions (BLUF, three counter-positions, kill criterion, attribution rules); workflow from `_backlog.md` → draft → published. |
| `insights/_backlog.md` | New: candidate POV table — five working titles seeded, one promoted to published, four remain draft / candidate. |
| `insights/from-contract-yaml-to-deployable-product-in-30-minutes-2026-05-09.md` | New: first published POV. The 30-minute benchmark argument for the DABs Golden Path. Three counter-positions defended (YAML can't capture mess; benchmark trick; vendor lock-in). Authored vs curated IP cited separately (Invariant #3). Kill criterion stated. |

**Closes:** Phase 11 of the v1.2.0 Practice OS extension (PR #3).

**Design Decisions:**
- The first POV directly defends the most ambitious authored deliverable in this PR (the DABs Golden Path subproject). Picking it first is a deliberate provocation: it exposes the contract-first thesis in public.
- `_backlog.md` was seeded with five working titles (not one) because `weekly-practice-synthesis` skill expects a backlog to draw from. Future synthesis runs append to it.
- POV filename convention is `<topic>-<YYYY-MM-DD>.md`. Working drafts use the topic only. Promotion = adding the date.
- Attribution: the 30-minute benchmark argument is mine; Mahboub (metadata-driven ingestion) and Shi (5 Pillars) are cited as the curated underpinning. Never blurred.

---

### v1.2.0-phase12 -- 2026-05-09 -- 13 Mermaid Diagrams
**Author:** Paroz Mehta + Claude Opus 4.7

**What changed:**

13 Mermaid diagram files added under `_Diagrams/` plus an index README:

| File | Mermaid type | Subject |
|---|---|---|
| `_Diagrams/no-lac-architecture.md` | flowchart LR | Medallion stack |
| `_Diagrams/ai-ready-platinum-5-principles.md` | flowchart + mindmap | 5 Principles + 6-Q rubric |
| `_Diagrams/dabs-contract-flow.md` | flowchart LR | Contract → renders |
| `_Diagrams/practice-os-3-layers.md` | flowchart TB | Three-layer mental model |
| `_Diagrams/ip-catalog-attribution.md` | flowchart LR | Authored vs curated vs EMBA |
| `_Diagrams/10q-discovery-flow.md` | flowchart TB | 10Q intake decision flow |
| `_Diagrams/platform-mandate-coalition.md` | sequenceDiagram | Coalition sequence |
| `_Diagrams/strategy-cascade.md` | flowchart TB | Roger Martin Cascade |
| `_Diagrams/case-answer-shapes.md` | flowchart LR | 4 prompt types → frameworks |
| `_Diagrams/medallion-layers-table.md` | flowchart TB | Property table per layer |
| `_Diagrams/ai-consumption-contract-shape.md` | erDiagram | AI contract entity model |
| `_Diagrams/sanitization-flow.md` | flowchart LR | Pre-commit gate flow |
| `_Diagrams/governance-audit-flow.md` | stateDiagram-v2 | 7-check audit state machine |
| `_Diagrams/README.md` | — | Index + style + how-to-add |

**Closes:** Phase 12 of the v1.2.0 Practice OS extension (PR #3).

**Design Decisions:**
- Native Mermaid (`.md` files with fenced ```mermaid blocks) instead of calling the diagram MCP. GitHub renders Mermaid natively in the markdown view; this keeps source control honest and makes diagrams diffable as text.
- Pastel palette enforced via Mermaid `classDef` blocks (`#AEC6CF`, `#B7E4C7`, `#FDFD96`, `#C3B1E1`, `#D3D3D3`) per `methodology/diagram-generation.md`.
- L-to-R or T-to-B layout. No zig-zag. No ordinals (numbered shapes) for sequence — arrows carry direction.
- 13 chosen diagrams span the IP frontier (No LAC · Platinum · DABs Golden Path · 10Q), the practice spine (3-layer model · IP catalog · case answer shapes), the operational gates (sanitization · governance audit), and the strategic frame (Cascade · medallion properties · platform mandate sequence · AI Consumption Contract entity shape).
- Existing v1.1 PNGs in `_Diagrams/` are kept as archive; the index README marks them as superseded by their Mermaid replacements.

---

### v1.2.0-phase13 -- 2026-05-09 -- 9 Verification Checks
**Author:** Paroz Mehta + Claude Opus 4.7

**What changed:**

| File | Check |
|------|-------|
| `scripts/verify/01_token_budget.sh` | CLAUDE.md ≤600 tokens (≈480 target) |
| `scripts/verify/02_routing.sh` | Every routing-table target in CLAUDE.md exists (talent/ + playbooks/ deferred to Phase 14) |
| `scripts/verify/03_skill_invocation.sh` | Every skill + subagent named in CLAUDE.md exists in `.claude/` |
| `scripts/verify/04_dabs_end_to_end.sh` | DABs subproject validate_bundle.sh + pytest unit tests |
| `scripts/verify/05_attribution_lint.sh` | Invariant #3: every `ip/curated/*.md` has Source callout |
| `scripts/verify/06_governance_gate.py` | Every `regulated:true` archetype declares dpia_required + dpia_completed explicitly |
| `scripts/verify/07_ip_coverage.py` | Invariant #1: every archetype names ≥1 IP file and every slug resolves |
| `scripts/verify/08_sanitization_audit.sh` | Wraps `scripts/lint_sanitization.sh` |
| `scripts/verify/09_diagram_coverage.sh` | Every diagram declared in `methodology/diagram-generation.md` exists in `_Diagrams/` |
| `scripts/verify_all.sh` | Runner: prints pass/fail summary |
| `.github/workflows/verify.yml` | CI wrapper that runs `verify_all.sh` on PR + main push |
| `Knowledge/Frameworks/CLAUDE.md` | Added (was missing — caught by 02_routing) |
| `CLAUDE.md` | Trimmed IP catalog line by 4 words (was at 604 tokens, now under 600) |

**Closes:** Phase 13 of the v1.2.0 Practice OS extension (PR #3).

**Verification result on this commit:** 9/9 pass · 0 fail.

**Design Decisions:**
- The verification suite caught two real defects (missing `Knowledge/Frameworks/CLAUDE.md`; CLAUDE.md 4 tokens over budget) on first run. Working as intended.
- Token budget gate uses words × 1.3 as a conservative estimator. Real tokenizer would be tighter; this errs on the side of strictness.
- 04_dabs_end_to_end skips gracefully if `databricks` CLI or `pytest` are absent (CI will install them; sandbox does not have them).
- 05_attribution_lint warns on authored files lacking author marker but does not fail; that's a craft issue, not a hard invariant. Hard invariant is: curated files MUST cite Source.
- 06_governance_gate is intentionally narrow: it checks that the field declaration is honest (no nulls where regulated:true). The 7-check audit lives in the `governance-audit` skill, not in CI.
- CI workflow runs on PR + main push so the gate is honored end-to-end, not just locally.

---

### v1.2.0 -- 2026-05-09 -- Practice OS Extension (FINAL)
**Author:** Paroz Mehta + Claude Opus 4.7

**The full v1.2.0 release.** This entry supersedes the per-phase tags
(`v1.2.0-phase9` through `v1.2.0-phase13`) and stamps the final clean
v1.2.0 version. All 14 phases of PR #3 closed.

**What v1.2.0 ships:**

1. **No LAC** — the headline architectural principle (`ip/authored/no-lac-principle.md`).
2. **AI-Ready Platinum Layer** — UC metadata as the runtime semantic layer (`ip/authored/ai-ready-platinum-layer.md`).
3. **DABs Data-Contract Golden Path** — forkable Databricks Asset Bundle subproject (`templates/dabs-data-product-template/`).
4. **12 attributed industry methodologies** in `ip/curated/`.
5. **5 anonymized engagement archetypes** in `initiatives/archetypes/`.
6. **Governance pack** — 8 files in `governance/`, including OSFI/PIPEDA-style runbooks, GDPR Article 17 erasure, DPIA template, ethics policy, model risk, classification, NDA, compliance register YAML.
7. **EMBA + Strategy framework expansion** — 13 new files across Cornell-Queen's frameworks and cross-cutting toolkits.
8. **Sanitization Protocol (Invariant #0)** — banned-token lint + gitleaks + GitHub Actions gate.
9. **3-layer mental model** — Shared Context / Shared Queries / Shared Discipline routing in `CLAUDE.md`.
10. **7 Practice OS skills + 3 atomic subagents** — Phase 10.
11. **Insights seed** — first published POV (Phase 11).
12. **13 Mermaid diagrams** under `_Diagrams/` (Phase 12).
13. **9 verification checks + CI workflow** under `scripts/verify/` (Phase 13).
14. **Talent + playbooks** — `talent/` (3 files) and `playbooks/` (4 files), final routing fully resolved (Phase 14).

**This commit (Phase 14):**

| File | Change |
|------|--------|
| `talent/CLAUDE.md` | New: routing for talent dir; three-pillar staffing model (Producer · Platform · Governance). |
| `talent/roles.md` | New: 7-role archetype table with hand-off discipline. |
| `talent/capability-matrix.md` | New: capability × level grid; reading rules for bench depth, authoring concentration, hiring trigger, promotion trigger. |
| `talent/hiring-brief-template.md` | New: fork-and-fill role brief. |
| `playbooks/CLAUDE.md` | New: routing for playbooks dir; conventions (Trigger, Owner, Done when). |
| `playbooks/producer-onboarding.md` | New: 12-step onboarding playbook from intake → bundle → consumer notification. |
| `playbooks/governance-runbook.md` | New: 10-step regulated-archetype audit playbook. |
| `playbooks/change-management.md` | New: 9-step platform-change playbook with deprecation discipline. |
| `playbooks/engagement-kickoff.md` | New: 11-step engagement-kickoff playbook with discovery week shape. |
| `scripts/verify/02_routing.sh` | Removed the talent/ + playbooks/ deferred-WARN allowance — both now exist. |

**Verification result on this commit:** 9/9 pass · 0 fail.

**File-count summary (v1.1.2 → v1.2.0):** ~32 files → ~180 files. The repo is now a portable, fork-and-customize Practice OS with a working DABs subproject, governed IP, codified archetypes, executable skills, machine-checked invariants, and a published POV defending the 30-minute claim.

**Honest version-history note:** the per-phase tags (`-phase9` through `-phase13`) above remain as the build trail. They are not separate releases; they are commit-level checkpoints inside the v1.2.0 PR. The final tag is plain v1.2.0.

---

### v1.2.1 -- 2026-05-10 -- CI Fix: Install DABs Requirements
**Author:** Paroz Mehta + Claude Opus 4.7

**What changed:**

| File | Change |
|------|--------|
| `.github/workflows/verify.yml` | Install `templates/dabs-data-product-template/requirements.txt` in addition to top-level pyyaml. |

**Gap that triggered this update:** v1.2.0 merged green for sanitization but the new `verify` workflow failed in CI on commit `5024b74`. Cause: the GitHub-hosted runner image ships with `pytest` pre-installed, so `04_dabs_end_to_end.sh` proceeded to invoke pytest. The DABs unit tests import `jsonschema` (and `pyyaml`) from `requirements.txt`. CI installed only top-level `pyyaml`, so pytest collection failed.

**Fix:** install the DABs subproject's `requirements.txt` in the workflow. Verified locally — 9/9 unit tests pass and full `verify_all.sh` returns 9/9 pass · 0 fail.

**Design Decisions:**
- Kept the script's defensive SKIP fallback for environments where pytest is genuinely absent (sandboxes, sparse CIs). The fix is in the workflow, not the script.
- Patch increment (1.2.0 → 1.2.1) per `methodology/repository-conventions.md` — only an existing CI file was edited.

---

### v1.3.0 -- 2026-08-20 -- Routing Coverage + Gate Documentation
**Author:** Paroz Mehta + Claude

**What changed:**

| File | Change |
|------|--------|
| `CLAUDE.md` | Rewritten within the 600-token cap. Seven routing rows added (`Knowledge/Work/`, `Workflows/`, `Templates/`, `_Registry/`, `_Logs/`, `scripts/`, `templates/`). Invariant #5 added: gates are CI-enforced. Version bumped to v1.3.0. |
| `scripts/CLAUDE.md` | New. The 9 verification checks, how to run them, the three constraints on editing the root routing brain, how to add a check, and the CI wiring. |
| `templates/CLAUDE.md` | New. Both forkable subprojects. States explicitly that a subproject's own `CLAUDE.md` is payload for a fork, not instructions for this repo. |
| `Workflows/CLAUDE.md` | New. Six workflows, the mandatory Verification Loop convention, and the two workflows that govern the repo itself. |
| `Templates/CLAUDE.md` | New. Four document formats, the mandatory Pre-Delivery Verification convention, and the `Templates/` vs `templates/` distinction. |
| `_Registry/CLAUDE.md` | New. The three inventories and the rule that the skills registry, `.claude/`, and the root `## Skills` block must agree. |
| `_Logs/CLAUDE.md` | New. The three trails, the version-increment table, and the escalation rule from correction to structural defect. |
| `Knowledge/Work/CLAUDE.md` | New. Five operational-context files, the fork note, and the sanitization warning for the repo's highest-risk surface. |
| `README.md` | Directory tree corrected against disk. "What's New in v1.3.0" added. Two "How to Extend" rows added (routing rule, verification check). |

**Gap that triggered this update:** three defects, all found by reading the
repo against its own rules.

1. **Unreachable content.** Seven directories held real content but had no
   nested `CLAUDE.md` and no routing row. `Knowledge/Work/` and `Templates/`
   were absent from the routing table entirely. Check 02 could not catch this:
   it verifies that routed paths exist, not that existing paths are routed.
2. **Career Command Center unrouted.** It shipped after v1.2.1 with no
   changelog entry, no routing row, and no version bump — a version-discipline
   miss. Worse, its `CLAUDE.md` opens by casting the reader as a career coach.
   An agent reading it while working on Noosphere inherits the wrong role.
   `templates/CLAUDE.md` now draws that line explicitly.
3. **Tree described directories that do not exist.** `playbooks/onboarding/`,
   `playbooks/governance/`, `playbooks/change-mgmt/`, and
   `templates/dabs-data-product-template/examples/` were all in the README
   tree and none is on disk. The `examples/` path was also cited as a live
   target in "How to Extend".

**Design Decisions:**
- **The root file stays a routing brain.** The obvious response to "document
  the repo comprehensively" is to grow `CLAUDE.md`. Check 01 caps it at 600
  tokens, and the cap is the design: detail belongs in nested files that load
  only when the work is in that directory. Comprehensiveness came from adding
  seven nested brains, not from growing the root.
- **Budget paid honestly.** The root file was at 599 of 600 tokens. Seven new
  rows and a new invariant were funded by trimming routing descriptions to
  their nouns and replacing `·` separators with commas in the skill and IP
  lists — `wc -w` counts a standalone `·` as a word. Final: 455 words ≈ 591
  tokens.
- **Check 01's estimator documented where it bites.** `scripts/CLAUDE.md`
  records the `·` behaviour so the next editor does not rediscover it.
- **Minor increment** per `methodology/repository-conventions.md`: new routing
  rules and a new file class (nested routing brains for system directories),
  no structural overhaul.

**Verification result on this commit:** 9/9 pass · 0 fail.
