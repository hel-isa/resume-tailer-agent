# Contributing

This started as a personal job-search tool, shared publicly as a reference for security-minded agent design. Contributions are welcome, especially around the trap-scanning, scoring logic, and template rendering.

## Getting started

1. Fork and clone the repo.
2. Copy the `.example.md` files (`profile.example.md`, `preferences.example.md`, `job-search-filters.example.md`) if you want to exercise the agent end to end — never commit real personal data.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt -r requirements-dev.txt
   ```

## Running tests

```bash
pytest -v
```

CI (`.github/workflows/tests.yml`) runs the same suite on Python 3.11. PRs must pass it before merge.

## Security checks

Before opening a PR, it helps to run the same checks CI runs:

```bash
pip install pip-audit bandit
pip-audit -r requirements.txt
bandit -r . --exclude ./.git -ll
```

See `SECURITY.md` for how to report a vulnerability privately instead of via a public issue.

## Making changes

- Keep `AGENT.md` as the source of truth for scoring/disqualifier/trap-scanning logic — update it alongside any behavior change, not just the code around it.
- Never add real names, contact details, or work history to tracked files; only the `.example.md` files should be committed.
- Add or update a test when changing `template.html` or the scoring rules.
- Keep dependency pins in `requirements.txt` exact (`==`) so Dependabot and `pip-audit` can flag issues precisely.

## Pull requests

Open a PR against `master` with a clear description of the change and why. Small, focused PRs are easier to review than large ones.
