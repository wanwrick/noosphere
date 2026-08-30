# PII Audit Pass

**BLUF: run this before any public push, and quarterly regardless. It proves
no personal data — the author's or anyone else's — reaches the public repo.**

Companion to `sanitization-pass.md`. That workflow protects *organizations*:
employer, team, vendor, stakeholder proper nouns. This one protects *people*.
The two are different obligations and they fail differently, so they are
separate gates.

| Workflow | Protects | Gate | Rules |
|---|---|---|---|
| `sanitization-pass.md` | Organizations and internal identifiers | `scripts/lint_sanitization.sh` | Gitignored lexicon |
| `pii-audit-pass.md` | Individuals | `scripts/lint_pii.py` | Tracked `.pii-patterns` |

## Why the PII rules are tracked and the lexicon is not

The lexicon must spell out the proper nouns it suppresses, so publishing it
defeats it. PII rules are the opposite: generic format regexes. "An email
address shaped like `x@y.z`" identifies nobody. Tracking them means every fork
inherits PII protection with no setup, which is the only way a template repo
protects the people who fork it.

## The six surfaces

An audit that checks only the working tree is not an audit. Personal data
reaches a public repo through six distinct surfaces, and four of them survive
a clean `git status`.

| # | Surface | How to check | Reversible? |
|---|---|---|---|
| 1 | Working tree | `python3 scripts/lint_pii.py` | Yes — edit and commit |
| 2 | Git history content | `git grep -I -E '<pattern>' $(git rev-list --all)` | Only by history rewrite |
| 3 | Commit metadata | `git log --all --format='%an <%ae>' \| sort -u` | Only by history rewrite |
| 4 | Commit messages | `git log --all --format='%s%n%b'` | Only by history rewrite |
| 5 | Pull-request refs | `git ls-remote origin 'refs/pull/*'` | **No — needs GitHub Support** |
| 6 | Forks and clones | Not enumerable | **No** |

Surfaces 5 and 6 are why prevention outranks remediation here. A history
rewrite does not reach them. See the 2026-08-21 entry in
`_Logs/sanitization-audit.md`: 29 pre-rewrite commits stayed fetchable through
`refs/pull/1..7/head` after a full `filter-repo` pass over every branch.

## Procedure

### 1. Working tree (surface 1)

```bash
python3 scripts/lint_pii.py                # local: shows matched text
python3 scripts/lint_pii.py --files-only   # anywhere output is public
```

Use `--files-only` in CI and in any log a third party can read. This
repository is public, so its CI logs are public. Printing a match would
republish the personal data the gate exists to suppress — the same trap the
sanitization lint fell into before v1.3.0.

### 2. History, metadata, messages (surfaces 2–4)

```bash
git log --all --format='%an <%ae>' | sort -u        # author identities
git log --all --format='%s' | less                  # subjects
git grep -I -n -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $(git rev-list --all)
```

Read the subjects with care. A commit that *removes* a name usually names the
person in its own subject line, which republishes exactly what the commit was
removing. Write "remove third-party attribution", never "remove <name>".

### 3. Pull-request refs (surface 5)

```bash
git ls-remote origin 'refs/pull/*/head'
```

These refs are read-only. A repository owner cannot delete, rewrite, or
force-push them. If pre-rewrite commits carry personal data, the only route is
a GitHub Support request to garbage-collect unreachable objects and drop stale
PR refs. Record it as outstanding until Support confirms. Never log a rewrite
as a complete fix when these refs still resolve.

## Triage

Not every regex hit is a leak, and not every leak is remediable.

| Verdict | Meaning | Action |
|---|---|---|
| **Leak** | Real personal data, not the author's own, published without consent | Remove, then assess surfaces 2–6 |
| **Byline** | The author's own published identity, deliberate | Add a narrow `.pii-allowlist` entry with a dated justification |
| **Attribution** | A public figure cited for published work | Keep. Invariant #3 requires the citation |
| **False positive** | Structurally shaped like PII, identifies nobody | Add to `.pii-allowlist` with a comment saying why |
| **Residual** | Real, but only on an unreachable surface | Log in `_Logs/sanitization-audit.md`; do not mark resolved |

The byline and attribution rows matter. Stripping every human name from a
practice OS would break Invariant #3, which *requires* citing the authors of
curated frameworks. The test is not "is this a name" but **"did this person
consent to being named here?"** A published author cited for their published
work has. A recruiter whose name landed in a tracker has not.

## Allowlisting

`.pii-allowlist` entries are regexes matched against the **matched text**, not
the line. That precision is deliberate: a line carrying both a documentation
IP and a real one still fails.

Every entry needs a comment giving the reason. Entries fall into three honest
categories — reserved values (RFC 2606 domains, RFC 5737 and RFC 1918
addresses, NANP 555-01xx), non-personal identities (`noreply@`, GitHub
`users.noreply.github.com`), and reviewed bylines. Anything else is a finding
you are hiding from yourself. Keep byline entries narrow: allowlist the one
profile URL, never the whole platform.

## Commit identity

`git log` publishes the author email of every commit, permanently, to anyone
who clones. It is the most common way personal data reaches a public repo,
and no working-tree gate can see it.

```bash
git config user.email "<id>+<username>@users.noreply.github.com"
```

Set it per clone before the first commit. It does not apply retroactively —
existing commits keep the address they were authored with, on every surface
including PR refs.

## Adding a rule

Append a tab-separated line to `.pii-patterns`:

```
category <TAB> flags <TAB> pattern <TAB> severity <TAB> canary
```

The canary is not optional discipline, it is the point. A regex typo compiles
fine and then matches nothing, so the gate reports "clean" while protecting
nothing — a silent failure indistinguishable from success. A rule that cannot
match its own canary is a hard load error.

Then prove it fires:

```bash
printf 'seeded value here\n' > /tmp/pii_probe.md && cp /tmp/pii_probe.md ./PII_PROBE.md
python3 scripts/lint_pii.py ; rm -f PII_PROBE.md
```

A gate you have never seen fail is a gate you have not tested.

## Cadence

| When | Scope |
|---|---|
| Every commit | Surface 1, via pre-commit |
| Every PR and push to `main` | Surface 1, via `.github/workflows/sanitization.yml` |
| Before publishing or announcing the repo | All six surfaces |
| Quarterly | All six surfaces, plus re-review every `.pii-allowlist` entry |
| Before accepting a fork's PR | Surface 1 against their branch |

Log every full pass in `_Logs/sanitization-audit.md`. Record the category and
the reason, never the matched value — that log is public.
