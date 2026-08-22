# Security Policy

## Reporting a Vulnerability

Please report security vulnerabilities privately using [GitHub's private vulnerability reporting](https://github.com/hel-isa/resume-tailer-agent/security/advisories/new) (Security tab → Report a vulnerability) rather than opening a public issue.

Include:
- A description of the vulnerability and its potential impact
- Steps to reproduce
- Any relevant logs or proof-of-concept code

You should expect an initial response within a few days. Confirmed vulnerabilities will be fixed and disclosed via a GitHub Security Advisory once a patch is available.

## Scope

This project treats job description text as **untrusted input** (see `AGENT.md`'s trap scanner for prompt-injection handling). Reports related to prompt-injection bypasses, PII handling, or the resume-generation pipeline are all in scope.

## Supported Versions

This is a single-branch personal automation project with no versioned releases. Security fixes are applied to `master` only.

## Automated Scanning

This repository runs `pip-audit` (dependency vulnerabilities), `gitleaks` (secret scanning), `bandit` (Python SAST), and CodeQL on every push/PR and on a weekly schedule — see `.github/workflows/`.
