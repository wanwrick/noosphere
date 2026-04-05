# Knowledge Base Operations

Step-by-step playbook for building and operating an LLM-powered knowledge base. For the conceptual framework, see `Knowledge/Frameworks/llm-knowledge-bases.md`.

---

## Setup (One-Time)

### 1. Create the Directory Structure

```
kb/
+-- raw/                 # Source documents (articles, papers, images)
+-- wiki/                # LLM-compiled articles (do not edit manually)
|   +-- _index.md        # Master index (auto-maintained by LLM)
|   +-- concepts/        # One .md per concept
|   +-- sources/         # Summaries of each raw document
|   +-- categories/      # Grouping pages
+-- output/              # Generated artifacts (reports, slides, charts)
+-- tools/               # Custom CLIs and scripts
```

### 2. Configure Obsidian
- Open the `kb/` directory as an Obsidian vault
- Install plugins: Marp Slides (presentations), Excalidraw (diagrams)
- Set `wiki/` as the default note location
- Enable backlinks panel

### 3. Set Up Web Clipping
- Install Obsidian Web Clipper browser extension
- Configure output directory to `kb/raw/`
- Set up a hotkey to download all page images to `kb/raw/images/`
- Preferred format: markdown with front matter (title, URL, date, tags)

---

## Ingest: Adding New Sources

### Step 1: Clip or Download
- Web article: Use Obsidian Web Clipper -> saves to `raw/`
- PDF/paper: Download to `raw/`, optionally convert to .md
- Repository: Clone or snapshot relevant files to `raw/repos/`
- Dataset: Download CSV/JSON to `raw/data/`
- Images: Save to `raw/images/` with descriptive filenames

### Step 2: Verify Source Quality
Before compiling, check:
- [ ] Source is complete (not truncated, images downloaded)
- [ ] Front matter present (title, source URL, date)
- [ ] Duplicates checked (not already in raw/ under different name)

### Step 3: Trigger Incremental Compile
Prompt the LLM:

> "I have added new sources to raw/. Read the new files, then update the wiki: create or update concept articles, add source summaries, update the master index, and add cross-references to existing articles."

The LLM should:
1. Read `wiki/_index.md` to understand existing coverage
2. Read new files in `raw/`
3. Identify new concepts and connections to existing concepts
4. Create new articles in `wiki/concepts/`
5. Create source summaries in `wiki/sources/`
6. Update `wiki/_index.md` with new entries
7. Update cross-references in affected existing articles

---

## Query: Asking Questions

### Simple Lookup
> "What does the wiki say about [concept]?"

The LLM reads `_index.md`, finds the relevant article(s), and summarizes.

### Research Question
> "Based on the wiki, what is the relationship between [concept A] and [concept B]?"

The LLM reads both articles, follows cross-references, and synthesizes.

### Gap-Aware Question
> "What does the wiki say about [topic]? If coverage is thin, flag the gap."

The LLM answers what it can and explicitly notes where the wiki lacks depth.

### Cross-Cutting Analysis
> "Across all articles tagged [category], what are the common patterns?"

The LLM reads the category page, pulls all referenced articles, and identifies patterns.

---

## Output: Generating Artifacts

### Markdown Report
> "Write a report on [topic] based on the wiki. Save to output/reports/[topic].md."

### Marp Slide Deck
> "Create a 10-slide Marp presentation on [topic]. Save to output/slides/[topic].md."

Marp format:
```markdown
---
marp: true
theme: default
---

# Slide Title

Content here

---

# Next Slide

More content
```

### Data Visualization
> "Generate a chart showing [data relationship]. Save the matplotlib PNG to output/charts/."

### Filing Output Back
After reviewing an output:
> "This report on [topic] is good. File it into the wiki as a new article under concepts/."

This is the output-as-input loop. Your explorations compound into the knowledge base.

---

## Lint: Health Checks

Run these periodically (weekly for active wikis, monthly for stable ones).

### Consistency Check
> "Read all articles in wiki/concepts/. Find any contradictory claims across articles. List each contradiction with the two source articles."

### Gap Detection
> "Read wiki/_index.md and all concept articles. Find any concepts that are referenced or linked but do not have their own article. List them as candidates for new articles."

### Connection Discovery
> "Read all concept articles. Identify pairs of concepts that are not currently cross-referenced but share significant thematic overlap. Suggest new cross-references or bridging articles."

### Data Imputation
> "Read articles flagged as incomplete (missing sections, TODO markers). Use web search to find the missing information and propose updates."

### Staleness Check
> "Read all source summaries. Flag any sources older than [threshold] that cover fast-moving topics. Suggest which should be refreshed."

### Structure Normalization
> "Check all articles for consistent formatting: H1 title, front matter, sections, cross-references section at the bottom. Fix any that deviate."

---

## Maintenance

### Weekly (Active Wiki)
- [ ] Ingest any new sources collected during the week
- [ ] Run consistency check and gap detection
- [ ] Review and file any useful outputs back into wiki
- [ ] Check `_index.md` is current

### Monthly
- [ ] Run full lint pass (all six checks)
- [ ] Review category pages for reorganization
- [ ] Archive stale sources in `raw/archive/`
- [ ] Back up the wiki (git commit + push)

### Quarterly
- [ ] Review wiki scope: is it still focused or has it drifted?
- [ ] Prune low-value articles
- [ ] Assess whether scale warrants hierarchical indexes
- [ ] Evaluate custom tooling needs

---

## Tool Development

### Search Engine (First Tool to Build)
A naive full-text search over wiki articles, available as:
- **Web UI**: For human browsing and exploration
- **CLI**: For LLM to invoke as a tool during complex queries

Minimal implementation: index all .md files, support keyword search with snippet preview, rank by relevance (TF-IDF or simpler).

### Other Useful Tools
| Tool | Purpose |
|------|---------|
| Link checker | Verify all cross-references resolve to existing articles |
| Stats dashboard | Article count, word count, coverage by category, growth over time |
| Diff viewer | Show what changed in the wiki after each compile pass |
| Export pipeline | Convert wiki subset to PDF, EPUB, or static site |

---

## Verification Checklist

Before considering a compile or lint pass complete:

- [ ] `_index.md` reflects all articles (no orphans, no stale entries)
- [ ] Every new concept article has at least one cross-reference
- [ ] Source summaries link back to the raw file
- [ ] No broken internal links
- [ ] Consistent formatting across all new/modified articles
