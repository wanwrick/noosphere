# Feedback & Corrections Log

> Captures corrections, preferences, and learnings from interactions. This log helps Claude improve over time by remembering what works and what doesn't.

---

## How to Use This Log

When Claude gets something wrong or Paroz expresses a preference, log it here so the pattern isn't repeated.

### Entry Format
```
### [Date] — [Category]
**Context:** [What was happening]
**Correction:** [What was wrong and what's right]
**Rule:** [The general principle to remember]
```

---

## Categories
- **Style** — Writing tone, formatting, length preferences
- **Technical** — Databricks, architecture, code patterns
- **Process** — Agile, communication, meeting protocols
- **Framework** — When a framework was misapplied or a better one exists
- **Preference** — Personal working style preferences

---

## Log Entries

### 2026-03-07 — Process
**Context:** Building the Work OS system, Paroz specified token efficiency as a priority.
**Correction:** Broad Notion searches waste tokens. Always use targeted page ID fetches from the Reference Map in CLAUDE.md.
**Rule:** Never search Notion broadly — use `notion-fetch` with specific page IDs. Check local Knowledge/ files first before hitting Notion.

### 2026-03-07 — Preference
**Context:** Paroz described communication preferences during Work OS creation.
**Correction:** N/A (initial capture)
**Rule:** Paroz prefers BLUF (Bottom Line Up Front) in all written communication. Emails under 5 sentences. Decks under 10 slides. Options presented as "3 choices + recommendation" not open-ended.

### 2026-03-07 — Style
**Context:** Work OS file design and documentation.
**Correction:** N/A (initial capture)
**Rule:** Keep .md files tight and scannable. Use tables over paragraphs for reference material. Include "When to Use" guidance so routing is unambiguous.
