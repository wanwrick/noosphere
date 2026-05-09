# Attribution Policy

> Authored IP and Curated IP are separate buckets. They are never blurred. Lint enforces.

## The rule

| Bucket | Rule |
|---|---|
| **`ip/authored/`** | Original IP authored by the practice. Sanitized of any employer / team / stakeholder reference. The practitioner is the author and accountable for the content. May draw on curated work but is not a derivative. |
| **`ip/curated/`** | Industry methodologies attributed to a named author or organization. Every file MUST start with a Source callout naming the author and a stable URL (post, repo, doc, article). Lint enforces. |

The split exists because credibility depends on it. A recruiter or peer reading the repo must be able to tell, at a glance, which work is the practitioner's own and which is an integrated synthesis of named external sources.

## Source-callout format

Every `ip/curated/*.md` file starts with:

```
> **Source:** [Author Name][, Affiliation if relevant]. [Source type]. [URL].
```

Examples:
- `> **Source:** Yassine Mahboub, Data & BI Consultant. LinkedIn post + [yassinemahboub.com](https://www.yassinemahboub.com/).`
- `> **Source:** Bain & Company. *The Three Layers of an Agentic AI Platform* (Apr 2026). [Read it](https://www.bain.com/insights/the-three-layers-of-an-agentic-ai-platform/).`
- `> **Source:** Yasar Kocyigit. Open-source GitHub project. LinkedIn post + repo.`

## What "drawing on" curated work means

`ip/authored/` files often cite curated frameworks. That's expected and welcome — synthesis is consulting craft. The discipline:

- The authored file's *thesis* and *structure* belong to the practitioner.
- Every curated framework cited gets explicit attribution at the cross-reference.
- If the authored file is mostly summary of a single curated source, it doesn't belong in `authored/`; move it to `curated/`.

## Edge cases

| Case | Rule |
|---|---|
| Framework with unclear original author (e.g., CDO Top 10 Deliverables) | Add to `curated/` with a "synthesized — origin unclear" disclaimer. Forks identifying a primary source should add citation. |
| Multiple authors on a framework (e.g., Fisher & Ury principled negotiation) | Cite both. |
| Practitioner's prior employer's IP that appears similar | NOT eligible for `authored/`. The practitioner is *not* the author of someone else's IP. Cite the public version if there is one; otherwise, omit. |
| Open-source frameworks (e.g., Yasar Kocyigit's repo) | `curated/` with author + repo URL. |

## Lint enforcement

Pre-commit hook checks every file under `ip/curated/` for a `> **Source:**` line in the first 10 lines. Missing → commit refused. (Implementation in `scripts/lint_sanitization.sh` next major.)

## Why this is non-negotiable

The repo doubles as a portfolio artifact for senior roles (MBB consulting, Director-level data, Senior Tech PM). Recruiters fact-check. A repo that blurs authored vs curated reads as either dishonest or unaware — both are disqualifying signals.

The rule isn't ceremonial. It's the credibility floor.
