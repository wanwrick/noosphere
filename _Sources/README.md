# Sources & Provenance

> Raw inputs, references, and source material that informed the knowledge base.

---

## Purpose

Every piece of knowledge in Noosphere should be traceable to its origin. This directory and the conventions below establish provenance tracking so that claims can be verified, sources can be refreshed, and gaps can be identified.

---

## Conventions

### 1. Inline Source Sections

Each knowledge file in `Knowledge/Frameworks/` or `Knowledge/Work/` can include a `## Sources` section at the bottom listing the materials that informed it:

```markdown
## Sources

- [Source title](URL or file path) -- Brief note on what was drawn from it
- [Book or paper title] -- Author, year. Relevant chapters/sections.
- _Sources/strategy/porter-2008-five-forces.md -- Web clip of original HBR article
```

### 2. Raw Source Material

For substantial external sources (web clips, papers, dataset descriptions), place the raw material in a subdirectory matching the knowledge domain:

```
_Sources/
  strategy/          # Sources for Knowledge/Frameworks/strategy.md
  finance/           # Sources for Knowledge/Frameworks/finance.md
  llm-knowledge-bases/  # Sources for the LLM KB framework
  platform/          # Sources for Knowledge/Work/platform.md
```

### 3. Source File Format

Raw source files should include front matter for traceability:

```markdown
---
title: [Article or paper title]
url: [Original URL, if web-sourced]
date_accessed: [YYYY-MM-DD]
tags: [domain, subtopic]
---

[Content: full text, clipped markdown, or summary]
```

### 4. Image Sources

Images referenced by knowledge files should be stored alongside their source document in `_Sources/[domain]/images/` with descriptive filenames.

---

## When to Add Sources

- When creating a new knowledge file from external material
- When updating a knowledge file based on new research
- When a claim in the wiki needs verification or citation
- During lint passes that flag unsourced content

## When Not to Add Sources

- For general business frameworks widely known (Porter's Five Forces does not need a citation for its existence, but a specific interpretation does)
- For internal team context that originates from the user directly
