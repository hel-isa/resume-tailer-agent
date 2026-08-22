# Preferences & Learned Rules (EXAMPLE)

> Copy to `preferences.md` and tune. The agent obeys everything here.

## Settings
- Match threshold to auto-generate: **75%**. Postings with inclusive "apply even if you don't meet all requirements" language drop it by 10%.
- Posture: default to GENERATE for in-domain roles at or above threshold. Reserve SKIP for hard blockers, clearly off-domain roles, or a required named language/tool that is the spine of the role.
- Output format: PDF, two pages max, using `template.html`.
- File naming: `<Name>-<Company>-<RoleShort>.pdf`.
- PII handling: store locally in `profile.md`; use only in the final resume; never elsewhere.

## Style rules
- No em-dashes in any candidate-facing output. Use colons, periods, or commas.
- Frame the candidate as a problem-solver and builder, not a narrow specialist.
- Lead with principal strengths; keep growth areas honest and secondary. Never overstate.
- Once a resume is generated, it is frozen. New details apply only to the resume being actively worked and to future ones, never retroactively.

## Learned rules (append new ones, dated, terse)
- YYYY-MM-DD Weight required experience heavily; a hard required gap keeps the score well below threshold even if fundamentals fit.
- YYYY-MM-DD Never borrow the posting's vocabulary for tools or methods not in `profile.md`. Tailoring means reorder and reword true facts only.
- YYYY-MM-DD For roles pitched at a junior or mid level, do not lead with total years of experience; it triggers overqualification screening.
