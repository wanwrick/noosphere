# Security and Privacy

This repository is public and is designed to be forked. It ships gates that
block two classes of disclosure before a commit lands.

| Gate | Blocks | Rules |
|---|---|---|
| `scripts/lint_sanitization.sh` | Employer, team, vendor, stakeholder proper nouns | Gitignored lexicon |
| `scripts/lint_pii.py` | Personal data of any individual | Tracked `.pii-patterns` |
| `.gitleaks.toml` | Credentials and structural identifiers | Tracked |

All three run on every commit via `.pre-commit-config.yaml` and on every pull
request via `.github/workflows/sanitization.yml`.

## Reporting an exposure

**If you find personal data, a credential, or an internal identifier in this
repository — including in its git history or in a pull request — report it
privately. Do not open a public issue.** A public issue republishes the exact
value to everyone watching, which makes the disclosure worse.

Use GitHub's private vulnerability reporting: **Security → Report a
vulnerability** on this repository. Include the file path and commit SHA. You
do not need to quote the value; the path and SHA are enough to locate it.

Expect acknowledgement within seven days.

### If the data is yours

Say so in the report. Personal data is removed on request, and you do not have
to justify the request or explain the harm. `governance/gdpr-article-17-erasure-runbook.md`
describes the erasure procedure this practice applies to client data; the same
standard applies here.

## What this repository contains by design

The author is named, with a professional profile link, in `README.md` and
`practice-context/about.md`. That is a deliberate byline, not an exposure.

Curated frameworks in `ip/curated/` cite their original authors by name and
URL. Invariant #3 requires that citation. Removing it would misattribute other
people's published work.

Everything else naming a person is a finding. Report it.

## Known residual exposure

Some historic personal data cannot be removed by the repository owner. GitHub
retains `refs/pull/<n>/head` for every pull request ever opened, and those refs
cannot be deleted, rewritten, or force-pushed. A history rewrite does not reach
them.

Current residual items are recorded in `_Logs/sanitization-audit.md`, with what
each requires to close. They are logged as outstanding rather than resolved,
because recording an incomplete fix as complete is its own failure.

## Forking

If you fork this repository, two things are yours to configure:

1. **Bootstrap the sanitization lexicon.** `cp .sanitization-lexicon.example
   .sanitization-lexicon.local`, then replace the placeholders. Without it the
   banned-token gate runs on fake terms and prints a NOT-PROTECTED banner.
2. **Set your commit identity** before your first commit. `git log` publishes
   your email permanently to anyone who clones:
   ```
   git config user.email "<id>+<username>@users.noreply.github.com"
   ```

The PII gate needs no setup. Its rules are tracked, so your fork inherits them.

`templates/career-command-center/` holds personal career data once used. Every
such file is gitignored by default and ships as a tracked `.example` template;
`bootstrap.sh` creates the live copies. See that folder's README.

Full audit procedure: `Workflows/pii-audit-pass.md`.
