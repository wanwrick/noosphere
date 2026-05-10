---
name: defending-ai-spend-memo
description: Generate a Defending AI Spend memo using the curated 12-question framework. Used when leadership questions AI investment, when an executive wants ROI evidence, or when an architecture decision needs an outcome-framed business case. Output is a one-page memo plus a dense appendix.
---

# defending-ai-spend-memo

You are authoring a **Defending AI Spend** memo: a structured business
case that survives a CFO interrogation. The framework is curated (Hewing,
12 questions) and is applied here against the Noosphere IP base.

## Source IP
- Curated: `ip/curated/defending-ai-spend-12q.md` (Hewing, 12 questions).
- Curated: `ip/curated/data-product-architecture-5-pillars.md` (Shi).
- Authored: `ip/authored/no-lac-principle.md` (architectural defence).
- Authored: `ip/authored/ai-ready-platinum-layer.md` (consumption defence).

Attribution rule (Invariant #3): the 12 questions are Hewing's. The
authored IP is the answer pattern. Never blur.

## When to invoke
- "CFO is asking about AI spend", "defend the AI roadmap", "build the
  business case", "ROI memo for the agentic pilot".
- A budget review touching AI infra, agent licenses, or platform compute.

## Required inputs
1. The investment under defence (e.g. "Q3 agentic pilot", "Platinum
   layer build-out", "Genie rollout").
2. Audience (CFO / CEO / Board / Architecture Council).
3. Time horizon (current year / 18-month / 3-year).
4. Linked archetype + data products (so we cite real consumption).

## The 12 questions (Hewing)
1. What problem is this solving?
2. Who is the consumer of the AI output?
3. What is the consumption pattern (read / agentic / fine-tune)?
4. What is the alternative (do nothing / current tool / human)?
5. What is the marginal cost per inference?
6. What is the marginal value per inference?
7. What is the failure mode + cost?
8. What is the governance posture?
9. What is the moat (data, model, distribution, governance)?
10. What is the timeline to first measurable outcome?
11. What is the kill criterion (when do we stop)?
12. What does the second-year case look like?

## Output shape
**One-page memo (BLUF first paragraph):**
- Recommendation + dollar ask + outcome metric in three sentences.
- Section: Why now (problem + alternative).
- Section: How (architectural defence — No LAC + Platinum).
- Section: Risk + governance posture.
- Section: Decision needed + by when.

**Appendix (dense):**
- 12-question table: question → one-paragraph answer → evidence pointer.
- Per-archetype consumption forecast.
- Cost model: marginal cost × volume × time horizon.
- Kill criteria + measurement plan.

## Verification
- BLUF: first paragraph readable in 30 seconds, recommendation explicit.
- Every question answered. "Unknown" answers are FAIL — research first.
- Citation: Hewing 12-question framework cited; authored IP cited
  separately.
- Sanitization: no employer / vendor / cost figure that leaks the client.
- Banned style: no "leverage", "synergies", "deep dive".

## Handoff
- Save memo to `insights/defending-ai-spend-<topic>-<date>.md` once
  `insights/` exists (Phase 11).
- Until then: `_Logs/<date>-defending-ai-spend-<topic>.md`.
- Log the decision to `Knowledge/Decisions/`.
