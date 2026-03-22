# Self-Improvement Workflow

## Purpose

This workflow describes the auto-optimization loop built into Noosphere. It ensures the system improves with each session rather than remaining static. Two mechanisms drive this: the **Auto-Loader** (context bootstrap at session start) and the **Auto-Improver** (verification and correction loop at session end).

Inspired by:
- **Boris Jeltsky**, build-in-public AI PM patterns (iterative public improvement, transparent versioning)
- **Andrej Karpathy**, autoresearch loop pattern (score → mutate → re-score → keep best)

---

## Part 1: Auto-Loader (Session Bootstrap)

Run at the start of every session. Takes under 60 seconds.

### Step 1: Load Priority Stack

```
Read in this order:
1. GOALS.md         → What matters right now (P0-P3)
2. _Logs/feedback.md → What not to repeat
3. _Registry/Cadences.md → Is a ritual due today?
```

**Check:** Do current priorities align with what the user is asking? If not, flag the mismatch before proceeding.

### Step 2: Identify Domain(s)

Map the session request to one or more Knowledge/ files:

| Request type | Primary file | Secondary file |
|---|---|---|
| Strategy or competitive analysis | Knowledge/Frameworks/strategy.md | Knowledge/Frameworks/economics.md |
| Financial analysis or modeling | Knowledge/Frameworks/finance.md | - |
| People, teams, org design | Knowledge/Frameworks/leadership.md | Knowledge/Work/collaborators.md |
| Data platform or technical work | Knowledge/Work/platform.md | Knowledge/Work/playbooks.md |
| Communication or stakeholder update | Knowledge/Work/communication.md | Templates/status-update.md |
| Decision under uncertainty | Knowledge/Frameworks/strategy.md | Templates/decision-memo.md |
| Presentation or deck | Workflows/executive-briefing.md | Knowledge/Work/communication.md |
| Incident or crisis | Workflows/incident-response.md | Templates/rca-template.md |
| Negotiation | Workflows/negotiation-prep.md | - |
| Data narrative or dashboard | Workflows/data-storytelling.md | - |

### Step 3: State the Plan

Before executing anything, output:

```
Domain: [X]
Framework(s): [Y]
Output format: [Z]
Files I will read: [list]
```

Get confirmation or adjustment before producing deliverables.

---

## Part 2: Auto-Improver (Verification Loop)

Run after producing any output. The loop has three passes.

### Pass 1: Framework Check

For each framework applied, verify:

- [ ] Is the framework named explicitly?
- [ ] Are all components addressed (e.g., all 5 forces for Porter's, all 4 Is for transformational leadership)?
- [ ] Is the conclusion derived from the framework, not stated first and then justified?
- [ ] Are assumptions clearly separated from facts?

**Threshold:** If any check fails, revise before delivery. Do not deliver partial framework applications.

### Pass 2: Communication Check (BLUF Enforcement)

For any written output:

- [ ] Can the reader understand the recommendation from the first sentence alone?
- [ ] Is the "so what" stated before the evidence?
- [ ] Are sentences under 25 words?
- [ ] Is every hedge removed ("I think," "probably," "it seems")?
- [ ] Are banned words absent (leverage, utilize, synergies, deep dive, circle back)?

**Threshold:** If the output fails 2+ checks, rewrite the opening. Patch individual sentences for 1 failure.

### Pass 3: Action Check

For any recommendation or plan:

- [ ] Does every action item have an owner?
- [ ] Does every action item have a due date or trigger?
- [ ] Is the next step specific enough to execute without follow-up questions?
- [ ] Are risks identified with mitigations (not just listed)?

**Threshold:** If any action item lacks owner or date, add them before delivery.

---

## Part 3: Autoresearch Loop (System-Level Optimization)

Run when a session reveals a repeating gap. Triggered by:
- 3+ corrections in the same category within one session
- A question the system cannot answer from existing Knowledge/ files
- A template that required significant modification to fit the actual use case

### The Loop

```
1. IDENTIFY the gap
   What question could not be answered?
   What framework was missing or incomplete?
   What template did not fit?

2. SCORE the current state
   Rate the gap: Critical (system fails) / Important (degraded output) / Minor (extra effort)
   Rate frequency: Always / Sometimes / Rarely

3. PROPOSE the fix
   New file in Knowledge/, Templates/, or Workflows/?
   Edit to existing file (add missing component, fix wrong formula)?
   New routing rule in CLAUDE.md?

4. VALIDATE the fix
   Does the proposed addition answer the gap question directly?
   Does it create any duplication with existing files?
   Is it general enough to reuse across sessions?

5. IMPLEMENT and LOG
   Make the change.
   Log it in _Logs/evolution.md with: date, gap identified, fix applied, reason.

6. RE-SCORE
   In the next session that hits this domain, does the gap still appear?
   If yes: the fix was insufficient. Return to step 3.
   If no: loop closed.
```

### Gap Taxonomy

| Gap type | Typical fix |
|---|---|
| Missing framework | Add to Knowledge/Frameworks/ |
| Missing SOP | Add to Knowledge/Work/playbooks.md |
| Missing template format | Add to Templates/ |
| Missing workflow step | Edit existing Workflows/ file |
| Wrong routing | Edit CLAUDE.md routing rules |
| Repeated communication error | Add to _Logs/feedback.md |
| Missing tool or MCP | Add to _Registry/MCPs.md or Skills.md |

---

## Part 4: Version Discipline

Every improvement cycle produces a version increment. Use semantic versioning:

| Change type | Increment | Example |
|---|---|---|
| New file added (workflow, template, knowledge domain) | Minor | v1.0 → v1.1 |
| Edit to existing file (fix, enhancement, verification loop) | Patch | v1.1 → v1.1.1 |
| Full restructure of system architecture | Major | v1.1 → v2.0 |

**Log every increment** in `_Logs/evolution.md`. The log is the public record of how the system learned.

---

## Quick Reference

```
Session start:
  Load GOALS.md → feedback.md → Cadences.md
  Map domain → State plan → Confirm

After every output:
  Pass 1: Framework complete?
  Pass 2: BLUF enforced?
  Pass 3: Actions have owners + dates?

After every session:
  Any gap triggered 3+ times? → Run autoresearch loop
  Any new learning? → Log to feedback.md
  Any system fix applied? → Log to evolution.md + bump version
```
