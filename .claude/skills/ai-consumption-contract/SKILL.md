---
name: ai-consumption-contract
description: Author or refresh an AI Consumption Contract for a Platinum-layer data product. Translates the AI-Ready Platinum 5 Principles + 6-question metadata rubric into a per-agent contract that an LLM agent or Genie space can consume safely. Use when an AI agent is being granted Platinum access, when a new agentic use case is launching, or when defending the data team's AI-readiness posture.
---

# ai-consumption-contract

You are authoring an **AI Consumption Contract**: the agreement between a
Platinum-layer data product and an AI agent that consumes it. *1× publish
→ 1× govern → 5+ consume.*

## Source IP
- Authored: `ip/authored/ai-ready-platinum-layer.md` (canonical).
- Authored: `ip/authored/no-lac-principle.md` (Bronze-to-Platinum logic).
- Curated: `ip/curated/context-wall-meta-knowledge-graph.md` (Tekiner).
- Curated: `ip/curated/bain-3-layer-agentic.md`.
- Template: `data-products/ai-consumption-contract-template.md`.

## When to invoke
- A Genie space, agentic analytics agent, or RAG pipeline is requesting
  Platinum read access.
- The data team is defending AI spend and needs proof of governed
  consumption.
- Periodic contract refresh (quarterly) on active AI consumers.

## Required inputs
1. Name + role of the consuming agent (Genie / RAG / fine-tune / feature).
2. Platinum view(s) being granted.
3. Use case (one sentence).
4. Producer's data contract (path to `data-contract.yml`).
5. Current archetype + governance status (from `initiatives.yaml`).

## The AI-Ready Platinum 5 Principles (every contract must address each)
1. **Semantic clarity** — column names match the metric definitions in
   the UC business glossary; no abbreviations the agent will hallucinate.
2. **Joinability declared** — every join key the agent will follow is
   documented in the metadata; no implicit relationships.
3. **Consumption-shaped** — the view is shaped for the agent's question
   pattern (one row per question, not per source row).
4. **Masked at source** — tier-1/2 columns are pre-masked in the view;
   the agent never sees raw PII.
5. **Observable** — every read by the agent is logged with prompt +
   row count + latency for cost + drift defense.

## The 6-question metadata rubric
1. What does each column mean (business definition)?
2. What does each column NOT mean (anti-definition)?
3. What is the freshness contract (max staleness)?
4. What is the volume contract (rows-per-day expectation)?
5. What is the quality contract (DLT expectations the agent inherits)?
6. What is the access contract (ABAC tags + masking applied)?

## Output shape
The completed `data-products/ai-consumption-contract-template.md` filled
out for the specific agent, with:
1. **BLUF**: agent X consumes Platinum view Y for use case Z.
2. 5 Principles each with concrete evidence (column lists, mask rules).
3. 6-question rubric each with cited source (glossary entry, DLT rule).
4. Observability hookup (UC system tables + agent prompt log path).
5. Quarterly refresh date stamped.

## Verification
- Every Principle and every rubric question answered or marked FAIL with
  remediation.
- Tier-1/2 columns demonstrably masked (cite the mask rule, not "yes").
- If any agent is reading raw PII → contract verdict is FAIL.
- Sanitization: no agent, vendor, or workspace name leaks.

## Handoff
- Save the contract to
  `data-products/<product>/ai-contracts/<agent>-contract.md`.
- Append the contract row to `data-products/data-products.yaml` under
  the product's `ai_consumers` list.
- If FAIL → invoke `governance-audit` skill before granting access.
