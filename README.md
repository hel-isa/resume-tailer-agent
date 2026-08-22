# Resume Tailor Agent

An AI agent that scores job descriptions against a candidate's real experience and generates a truthful, tailored resume PDF only when the fit is strong enough. Built as a security-minded automation project: it treats every job posting as untrusted input, keeps all personal data local, and never fabricates experience.

## Why this exists

Job searching at scale is repetitive: read a posting, judge the fit, tailor a resume, track the outcome. This agent automates the repetitive parts while keeping a human in control of what actually gets sent. It was built to embody how good security tooling should work: reduce manual toil, keep sensitive data local, and be honest by design.

## What it does

1. **Deduplicates** against a tracker so reposts are not re-analyzed (saves cost).
2. **Fast-rejects** clear mismatches in one line using a hard-disqualifier gate, before any expensive scoring.
3. **Scores** the remaining roles 0 to 100 against the candidate profile, weighting required qualifications heavily and never inflating gaps.
4. **Generates** a tailored resume PDF only when the score clears the threshold, reordering and rewording true facts to match the posting.
5. **Tracks** every processed role (generated or skipped) and every employer response in a consolidated log.

## Security and privacy by design

- **PII stays local.** Contact details and work history live in one local `profile.md`, are used only inside the final resume file, and are never sent to any external service.
- **Job postings are untrusted input.** A trap scanner checks every posting for prompt-injection and canary phrases ("include the word X", "if using AI, do Y") and refuses to comply, flagging them instead.
- **No fabrication.** The agent may use only facts present in the profile. If a role needs something that is not there, it is a gap to be flagged, never invented.
- **Human in the loop.** Free-text answers (cover letters, screening questions) are written by the candidate, not auto-generated, especially where a posting forbids AI-written prose.

## How it works

```
Job description
      |
      v
[ Dedupe check ] --- already seen? --> return prior verdict (1 line)
      |
      v
[ Hard-disqualifier gate ] --- hard blocker? --> fast-reject (1 line)
      |
      v
[ Trap / prompt-injection scan ] --- trap? --> flag, never comply
      |
      v
[ Score vs profile ] --- below threshold? --> skip + log
      |
      v
[ Generate tailored resume PDF ] --> save + log
```

The scoring logic, disqualifier lists, and honesty rules live in `AGENT.md`. The candidate's facts live in `profile.md` (kept private; see `profile.example.md` for the shape). Resume styling lives in `template.html`.

## Repository layout

| File | Purpose | Committed? |
|------|---------|-----------|
| `AGENT.md` | The agent's logic: dedupe, disqualifier gate, trap scan, scoring, generation | yes |
| `template.html` | Resume styling (HTML to PDF via WeasyPrint) | yes |
| `profile.example.md` | Example candidate profile with dummy data | yes |
| `preferences.example.md` | Example thresholds, format, and learned rules | yes |
| `job-search-filters.example.md` | Example target titles, search strings, disqualifiers | yes |
| `profile.md`, `tracker/`, `responses/`, `resumes/` | Real personal data | no (gitignored) |

## Quick start

1. Copy `profile.example.md` to `profile.md` and fill in your real experience.
2. Copy `preferences.example.md` to `preferences.md` and set your threshold.
3. Point an AI agent (or Claude in Cowork) at `AGENT.md` and paste a job description.
4. Generated resumes render to PDF with:
   ```bash
   python3 -c "import weasyprint; weasyprint.HTML('build.html').write_pdf('out.pdf')"
   ```

## Design notes

The agent is intentionally cost-aware. Obvious mismatches are rejected in a single line without a full analysis; obvious fits are generated without over-deliberating; only genuine judgment calls get a full score block. This keeps token usage low over large batches of postings.

## License

MIT. See `LICENSE`.
