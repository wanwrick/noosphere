# LLM Knowledge Bases

A pattern for building personal knowledge systems where an LLM ingests raw sources, compiles a structured wiki, and then operates on that wiki to answer questions, generate artifacts, and incrementally improve the knowledge base itself.

## Core Insight

The LLM is not just a query engine over your data. It is the **author, editor, and librarian** of a living wiki. You rarely touch the wiki directly. The LLM writes it, maintains it, cross-links it, and enhances it over time. Your role is to feed it raw sources, ask questions, and review outputs.

---

## Architecture

```
Raw Sources (articles, papers, repos, datasets, images)
     |
     v
+-------------+
|   raw/      |  Indexed source documents (web clips, PDFs, screenshots)
+------+------+
       |
       v  [LLM Compile Pass]
+------+------+
|   wiki/     |  Structured .md files: concepts, articles, summaries, backlinks
+------+------+
       |
       +---> Q&A (complex questions answered via wiki research)
       +---> Outputs (markdown reports, Marp slides, matplotlib charts)
       +---> Linting (health checks, consistency, gap detection)
       +---> Filing (outputs fed back into wiki to enhance it)
       |
       v
+------+------+
|   tools/    |  CLI search engine, web scrapers, format converters
+-------------+
```

### Data Flow

1. **Ingest**: Raw data enters `raw/` from web clippers, manual downloads, API pulls
2. **Compile**: LLM reads `raw/`, produces structured wiki articles in `wiki/`
3. **Index**: LLM auto-maintains index files, summaries, and cross-references
4. **Query**: User asks questions; LLM researches across the wiki to answer
5. **Output**: Answers rendered as markdown, slides, charts, or other artifacts
6. **File back**: Useful outputs are filed back into the wiki, compounding value
7. **Lint**: Periodic health checks find inconsistencies, gaps, and new connections

---

## Five Pipeline Stages

### 1. Ingest

**Goal:** Get raw source material into a structured directory.

| Source Type | Ingestion Method |
|------------|-----------------|
| Web articles | Obsidian Web Clipper extension -> .md files |
| Images | Hotkey to download all related images to local |
| Papers/PDFs | Manual download or API pull |
| Code repos | Git clone or snapshot |
| Datasets | CSV/JSON download |
| Screenshots | Screen capture to raw/ |

**Key principle:** Always pull images local. LLMs need direct file access, not URLs that may break. The web clipper converts HTML to markdown; a hotkey downloads all referenced images alongside it.

### 2. Compile

**Goal:** LLM transforms raw sources into a structured, interlinked wiki.

The compile pass produces:
- **Concept articles**: One article per concept, with definition, context, and examples
- **Source summaries**: Brief summaries of each raw document with backlinks
- **Category pages**: Groupings of related concepts
- **Index files**: Master index with brief descriptions of every article
- **Cross-references**: Backlinks between related concepts

**Key principle:** The wiki is the LLM's domain. You do not edit it manually. If something is wrong, you tell the LLM and it fixes it. This keeps authorship consistent and cross-references intact.

### 3. Query (Q&A)

**Goal:** Ask complex questions and get researched answers from the wiki.

At sufficient scale (~100+ articles, ~400K+ words), the wiki becomes a genuine research corpus. The LLM:
- Reads index files to identify relevant articles
- Pulls and synthesizes content from multiple articles
- Cites sources within the wiki
- Identifies gaps where the wiki lacks coverage

**Key principle:** You do not need RAG or vector search at this scale. The LLM's ability to read index files and follow cross-references is sufficient for corpora up to hundreds of articles. Auto-maintained indexes and brief summaries serve as the discovery mechanism.

### 4. Output

**Goal:** Render answers and analysis as reusable artifacts.

| Output Format | Use Case | Viewer |
|--------------|----------|--------|
| Markdown (.md) | Reports, analysis, summaries | Obsidian |
| Marp slides (.md) | Presentations | Obsidian Marp plugin |
| Matplotlib charts (.png) | Data visualization | Obsidian, any image viewer |
| Excalidraw diagrams | Architecture, flows | Obsidian Excalidraw plugin |
| CSV/JSON | Structured data exports | Any editor |

**Key principle:** Outputs are often filed back into the wiki. Your explorations and queries compound into the knowledge base, making future queries richer.

### 5. Lint

**Goal:** Incrementally improve wiki quality and coverage.

Linting operations the LLM can perform:
- **Consistency checks**: Find contradictory claims across articles
- **Gap detection**: Identify concepts referenced but not defined
- **Data imputation**: Use web search to fill missing data points
- **Connection discovery**: Find non-obvious links between concepts for new articles
- **Staleness detection**: Flag articles that may be outdated
- **Structure normalization**: Ensure consistent formatting, headings, metadata

**Key principle:** The LLM is good at suggesting further questions to investigate. Each lint pass both fixes issues and generates candidates for new research.

---

## Design Principles

### 1. LLM-as-Author
The wiki is written and maintained entirely by the LLM. Human edits are rare and limited to high-level direction. This keeps the corpus internally consistent and allows the LLM to maintain its own indexing and cross-referencing system.

### 2. Incremental Compilation
The wiki is never rebuilt from scratch. Each new raw source triggers an incremental update: new articles, updated cross-references, revised summaries. This keeps compilation cost proportional to new data, not total corpus size.

### 3. Index-Driven Navigation
Instead of vector search or embeddings, the LLM maintains plain-text index files with brief summaries. These serve as the table of contents the LLM reads to find relevant articles. This is simple, inspectable, and works well up to hundreds of articles.

### 4. Output-as-Input Loop
Answers and analyses generated from the wiki are themselves filed back in. This creates a flywheel: every question you ask makes the wiki better for future questions. Your exploration history becomes part of the knowledge base.

### 5. Obsidian as IDE
Obsidian provides the viewing layer: markdown rendering, backlink graphs, image display, and plugin-based extensions (Marp for slides, Excalidraw for diagrams). The LLM is the backend; Obsidian is the frontend.

### 6. Tool Augmentation
Custom CLI tools extend the LLM's capabilities over the wiki. A naive search engine over the corpus, available both as a web UI and as a CLI tool the LLM can invoke, is the most common first tool. Others follow based on need.

---

## Scaling Considerations

### Current Sweet Spot
- ~100-500 articles
- ~100K-1M words
- Index-driven navigation (no embeddings needed)
- Single LLM agent with full context of indexes

### Scaling Boundaries

| Scale | Challenge | Mitigation |
|-------|-----------|------------|
| 500-2000 articles | Index files too large for context | Hierarchical indexes: domain -> subdomain -> article |
| 2000+ articles | LLM cannot hold enough context | RAG with embeddings, or chunked retrieval |
| Multi-topic wikis | Cross-domain confusion | Separate wikis per topic with cross-wiki linking |
| Team use | Merge conflicts, authorship | Git-based collaboration, PR-based review of LLM edits |

### Future Direction: Weight-Based Knowledge
As corpora grow very large, the natural next step is synthetic data generation and finetuning to embed knowledge into model weights rather than relying on context windows. This shifts the bottleneck from context length to training compute.

---

## Comparison with Other Approaches

| Approach | Strengths | Weaknesses vs. LLM KB |
|----------|-----------|----------------------|
| Traditional wiki (Confluence, Notion) | Familiar, collaborative | Manual authorship, no auto-linking, no Q&A |
| RAG over documents | Scales to large corpora | Complex infrastructure, lossy retrieval, no curation |
| Vector database + embeddings | Fast retrieval | Black-box relevance, no human-readable structure |
| Knowledge graph | Explicit relationships | Expensive to build, brittle schema |
| LLM Knowledge Base | Auto-authored, queryable, self-improving | Scale ceiling, LLM cost, requires trust in LLM authorship |

---

## Product Opportunity

This pattern today exists as a "hacky collection of scripts." The product gap is clear:

**What exists:** Individual scripts for web clipping, LLM compilation, search, and viewing, stitched together manually.

**What should exist:** An integrated tool that handles:
- One-click ingest from web, PDF, repo, or file drop
- Automatic incremental compilation with configurable wiki structure
- Built-in Q&A with source citation and confidence scoring
- Output rendering (slides, charts, reports) with one command
- Scheduled linting and enhancement passes
- Obsidian-native or standalone viewer with backlink graph
- Git-backed version control of the wiki
- Multi-wiki support with cross-wiki queries

The closest analogs are Obsidian (viewing only), Mem.ai (AI-native but cloud-locked), and Notion AI (bolted onto an existing product). None combine LLM-as-author with local-first, inspectable, markdown-based knowledge compilation.
