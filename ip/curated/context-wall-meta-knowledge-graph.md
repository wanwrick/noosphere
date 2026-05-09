# The Context Wall + Meta Knowledge Graph

> **Source:** Firat Tekiner. *The Context Wall: Why AI Agents Fail Without Enterprise Context* — Medium series (Part 1 of 3). [Read it](https://medium.com/@firattekiner/the-context-wall-why-ai-agents-fail-without-enterprise-context-f28b1df7c43b).

## Core problem — the Context Wall

AI agents hit a wall: **enterprise architectures were built for humans, not machines.** Models are fluent but not grounded. Demos work; production stalls. Hard-coded instructions lack provenance.

| What agents experience | What human experts have |
|---|---|
| Fluent but not grounded | Years of accumulated context |
| Demos work, production stalls | Know that "SOW" = "Statement of Work" in this org |
| Confidently wrong | Remember last quarter's schema that worked |
| Starts fresh every session | Know who to ask when they don't know |

## The fix — Meta Knowledge Graph

A **meta knowledge graph** is *not* a copy of your data and *not* a catalog (catalogs are for humans). It organizes **metadata about knowledge**: how it's produced, governed, and used. Agents read from it, write to it, and learn through it.

| Concept | Domain Knowledge Graph | Meta Knowledge Graph |
|---|---|---|
| Captures | Facts about the world | Context *about* knowledge |
| Purpose | System of record for entities | System of record for institutional memory |
| Answers | "What are the facts?" | "Who owns it? How was it produced? Why this decision?" |
| Consumers | Humans + applications | AI agents + humans + applications |
| Data | Stores | Points to (no movement) |

## The 4 metadata categories

| Category | Captures | Status |
|---|---|---|
| **Technical** | Schemas, lineage, pipelines, formats | Traditional — well understood |
| **Business** | Definitions, glossaries, ownership, policies | Traditional — often incomplete |
| **Operational** | Freshness, quality scores, SLA status | Traditional — increasingly automated |
| **Agentic** ⭐ NEW | Decision traces, reasoning patterns, human corrections | No traditional framework captures this |

## Three types of agent memory

| Memory | Captures | Stored where |
|---|---|---|
| **Short-term** (session) | Current conversation, plan, intermediate results | Temporary; outcomes feed long-term |
| **Long-term** (enterprise) | Accumulated facts, entities, user preferences | Graph |
| **Reasoning** (decision traces) | Actions taken, tools called, outcomes, corrections | Graph — and **most often missing today** |

## The compounding effect

Every correction logged, every decision traced, every clarification captured makes the **next** agent smarter. Agents following rule-based approaches outperform humans at adhering to standards (humans drift under time pressure).

## When to use this in this practice

- **Designing AI-Ready Platinum Layer (Principle 1)** — the meta knowledge graph is the macro-pattern; AI Consumption Contracts are the micro-pattern.
- **Multi-domain agent rollouts** — when one agent reads across multiple data products, the graph is the cross-domain context surface.
- **Governance design** — agentic metadata is a new governance object class. UC tags + UC Functions are the entry point.

## How it applies in this practice

| This practice's component | What the Context Wall framework gives it |
|---|---|
| AI Consumption Contracts (`ai-ready-platinum-layer.md` §6.3) | The schema for the "agentic metadata" category at the data-product level |
| Decision logs (`Knowledge/Decisions/`) | A primitive form of reasoning memory — formalize as graph edges over time |
| `_Logs/feedback.md` | Captures human-correction edges that feed back into the graph |

## Cross-references

- `bain-3-layer-agentic.md` — the "Data + Knowledge" layer is what the meta knowledge graph becomes.
- `data-contracts-producer-consumer.md` (Baeyens) — formalizes one slice of the business metadata layer.
- `dataplex-six-data-product-principles.md` — Dataplex's "rich context" principle is operational meta-knowledge.
- `../authored/ai-ready-platinum-layer.md` — Principle 1 (Metadata becomes product) is the Platinum-layer rendering of this idea.
