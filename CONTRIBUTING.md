# Contributing

This project is designed to be **forked and customized**, not contributed to directly. Your Noosphere should be yours.

## How to Use This Template

1. **Fork** this repository to your own GitHub account
2. **Clone** it locally
3. **Customize** every file with your own knowledge, context, and preferences
4. **Use** it as your Claude Code or Cowork project folder

## If You Want to Improve the Template

If you have ideas that would improve the template structure for everyone:

1. Open an issue describing the improvement
2. Fork the repo and make your changes
3. Submit a pull request with a clear description of what you changed and why

### Pull Request Process

1. Create a feature branch from `main` (e.g., `add-workflow-sprint-planning`)
2. Make your changes
3. Verify your changes work by testing with Claude Code or Cowork (see Validation below)
4. Submit a PR with a clear description of what changed and why

### What Makes a Good Template Improvement

- Structural changes that benefit any user (new file categories, better routing patterns)
- Bug fixes in the template format
- Documentation improvements
- New template or workflow formats that are broadly useful

### What Doesn't Belong in the Template

- Personal knowledge content (that goes in your fork)
- Company-specific context
- Domain-specific frameworks (add these to your own fork)

## Before Your First Commit

**Set your commit identity.** `git log` publishes the author email of every
commit permanently, to anyone who clones or forks. No gate in this repository
can see it, and it cannot be fixed retroactively — a history rewrite does not
reach the `refs/pull/*` refs GitHub keeps for every pull request.

```bash
git config user.email "<id>+<username>@users.noreply.github.com"
```

Find your address under GitHub → Settings → Emails → *Keep my email address
private*. Set it per clone, before you commit.

**Bootstrap the sanitization lexicon**, or the banned-token gate runs on fake
terms:

```bash
cp .sanitization-lexicon.example .sanitization-lexicon.local
# then replace the placeholders with your real terms
```

## Validation

Before submitting, verify:
1. **Gates pass:** Run `bash scripts/verify_all.sh` and confirm 10 pass · 0 fail.
2. **Routing works:** Ask Claude a question that should route to your new/changed file. Does it find the right content?
3. **Templates render:** If you changed a template, ask Claude to generate a document using it. Does the output match the format?
4. **No broken cross-references:** Search for any file paths or cross-references you changed. Update all references in CLAUDE.md and other files.

### Never Commit Personal Data

Real emails, phone numbers, national IDs, postal addresses, and payment
details are blocked by `scripts/lint_pii.py` on every commit. Use the
placeholder conventions below instead.

This applies to **other people's** data as much as your own. A recruiter's
name in a tracker, a colleague's email in an example — neither consented to
being published. Full procedure: `Workflows/pii-audit-pass.md`.

Writing a commit message that removes a person's reference? Describe the
change, do not name them. "Remove third-party attribution" — never "remove
<name>". A commit subject is permanent on more surfaces than the file it
changes.

Found personal data already published here? See `SECURITY.md` and report it
privately. Do not open a public issue.

### Placeholder Conventions

All personalizable content uses bracket syntax: `[Your Name]`, `[Company Name]`, `[Platform Name]`, etc. For Notion page IDs, use `your-notion-page-id-here`. Keep this convention when adding new customizable content.

## Code of Conduct

Be kind. Be constructive. Be helpful.

---

*Questions? Open an issue.*
