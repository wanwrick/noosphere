# Knowledge Base Operations

Step-by-step playbook for building and operating an LLM-powered knowledge base. Applicable to any markdown-based wiki where an LLM is the primary author and operator. For the conceptual framework, see `Knowledge/Frameworks/llm-knowledge-bases.md`.

---

## Setup

### Directory Structure

Adapt to your context. A typical LLM knowledge base has four zones:

```
[root]/
+-- sources/             # Raw input material (articles, papers, images)
+-- knowledge/           # LLM-compiled articles (the wiki itself)
|   +-- _index.md        # Master index (auto-maintained by LLM)
+-- output/              # Generated artifacts (reports, slides, charts)
+-- tools/               # Custom CLIs and scripts (optional)
```

> **Noosphere mapping:** `_Sources/` = sources, `Knowledge/` = the wiki, `_Registry/Index.md` = the master index. There is no separate output/ directory; outputs are filed directly into the knowledge base or delivered to the user.

### Viewer Setup

Obsidian is the recommended viewing layer:
- Open the root directory as an Obsidian vault
- Install plugins as needed: Marp Slides (presentations), Excalidraw (diagrams)
- Enable backlinks panel for cross-reference navigation

### Web Clipping (for Research-Scale Wikis)

- Install Obsidian Web Clipper browser extension
- Configure output to the sources directory
- Set up a hotkey to download all page images locally
- Preferred format: markdown with front matter (title, URL, date, tags)

---

## Ingest: Adding New Sources

### Step 1: Collect
- Web article: Use web clipper or manual save to sources/
- PDF/paper: Download, optionally convert to .md
- Repository: Clone or snapshot relevant files
- Dataset: Download CSV/JSON
- Images: Save with descriptive filenames

### Step 2: Verify Source Quality
- [ ] Source is complete (not truncated, images downloaded locally)
- [ ] Front matter present (title, source URL, date)
- [ ] Duplicates checked (not already ingested under a different name)

### Step 3: Trigger Incremental Compile

Prompt the LLM to read new sources and update the wiki:

> "I have added new sources. Read them, then update the wiki: create or update concept articles, add source summaries, update the master index, and add cross-references to existing articles."

The LLM should:
1. Read the master index to understand existing coverage
2. Read new source files
3. Identify new concepts and connections to existing concepts
4. Create or update articles
5. Update the master index with new entries
6. Update cross-references in affected existing articles

> **Noosphere:** At current scale, "compilation" is manual curation. When adding new knowledge, use `Templates/knowledge-article.md` as the article format and update `_Registry/Index.md` afterward.

---

## Query: Asking Questions

### Simple Lookup
> "What does the wiki say about [concept]?"

The LLM reads the index, finds the relevant article(s), and summarizes.

### Research Question
> "Based on the wiki, what is the relationship between [concept A] and [concept B]?"

The LLM reads both articles, follows cross-references, and synthesizes.

### Gap-Aware Question
> "What does the wiki say about [topic]? If coverage is thin, flag the gap."

The LLM answers what it can and explicitly notes where the wiki lacks depth.

### Cross-Cutting Analysis
> "Across all articles in [category], what are the common patterns?"

The LLM reads the category or domain file, pulls all referenced articles, and identifies patterns.

> **Noosphere:** The LLM uses `CLAUDE.md` routing rules and `_Registry/Index.md` to navigate. For cross-cutting analysis, it pulls from multiple Knowledge/ files as described in routing rule 10.

---

## Output: Generating Artifacts

### Common Formats

| Output | Example Prompt | Format |
|--------|---------------|--------|
| Report | "Write a report on [topic] based on the wiki" | Markdown (.md) |
| Slide deck | "Create a 10-slide Marp presentation on [topic]" | Marp markdown |
| Chart | "Generate a chart showing [data relationship]" | matplotlib PNG |
| Diagram | "Draw the architecture of [system]" | Excalidraw |

### Filing Output Back

After reviewing an output, file it back into the wiki:

> "This report on [topic] is useful. File it into the wiki as a new article."

This is the output-as-input loop. Your explorations compound into the knowledge base.

> **Noosphere:** File useful outputs as new Knowledge/ articles or append to existing ones. Log corrections to `_Logs/feedback.md`. Update `_Registry/Index.md` after any addition.

---

## Lint: Health Checks

Run periodically to maintain wiki quality. For active wikis, weekly. For stable ones, monthly.

### Core Lint Checks

| Check | What It Finds | Fix |
|-------|---------------|-----|
| **Consistency** | Contradictory claims across articles | Reconcile with source material, update the weaker article |
| **Gap detection** | Concepts referenced but not defined | Create stub articles or flag for research |
| **Connection discovery** | Concepts with thematic overlap but no cross-reference | Add cross-references or bridging articles |
| **Data imputation** | Incomplete articles (missing sections, TODO markers) | Use web search to fill gaps, propose updates |
| **Staleness** | Sources or articles older than threshold on fast-moving topics | Flag for refresh, trigger research pass |
| **Structure normalization** | Inconsistent formatting, headings, metadata | Normalize to the standard article template |

### Lint Prompts

- Consistency: "Find contradictory claims across articles. List each contradiction with both source articles."
- Gaps: "Find concepts that are referenced or linked but have no article. List as candidates."
- Connections: "Identify concept pairs not cross-referenced but sharing thematic overlap."
- Staleness: "Flag articles on fast-moving topics not updated in 90+ days."

> **Noosphere:** Use `Workflows/self-improvement.md` Part 5 for the noosphere-specific lint checklist. It covers index freshness, cross-reference integrity, gap detection, staleness, and structure consistency, adapted for the system's architecture.

---

## Maintenance Cadences

### Weekly (Active Wiki)
- [ ] Ingest new sources collected during the week
- [ ] Run consistency check and gap detection
- [ ] Review and file useful outputs back into wiki
- [ ] Verify master index is current

### Monthly
- [ ] Run full lint pass (all checks)
- [ ] Review category/domain organization
- [ ] Archive stale sources
- [ ] Git commit + push (backup)

### Quarterly
- [ ] Review wiki scope: focused or drifted?
- [ ] Prune low-value articles
- [ ] Assess whether scale warrants hierarchical indexes
- [ ] Evaluate custom tooling needs

> **Noosphere:** The monthly lint cadence is registered in `_Registry/Cadences.md`. The quarterly review aligns with the quarterly prep checklist in the same file.

---

## Tool Development

As the wiki grows, custom tools extend the LLM's capabilities:

| Tool | Purpose | Priority |
|------|---------|----------|
| Full-text search (CLI + web UI) | Human browsing and LLM tool use for complex queries | First tool to build |
| Link checker | Verify all cross-references resolve | High (automates lint check 2) |
| Stats dashboard | Article count, word count, coverage by category, growth over time | Medium |
| Diff viewer | Show what changed after each compile pass | Medium |
| Export pipeline | Convert wiki subset to PDF, EPUB, or static site | Low |

---

## Verification Checklist

Before considering a compile or lint pass complete:

- [ ] Master index reflects all articles (no orphans, no stale entries)
- [ ] Every new article has at least one cross-reference
- [ ] Source material is traceable (summaries link to raw files)
- [ ] No broken internal links
- [ ] Consistent formatting across all new/modified articles
- [ ] Version incremented if structural changes were made (see `Workflows/self-improvement.md` Part 4)
