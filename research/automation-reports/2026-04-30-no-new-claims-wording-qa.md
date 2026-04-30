# No-new-claims Wording QA

Date: 2026-04-30

## Scope

Ran a no-new-claims wording QA pass after the owner-review shortlist. The pass looked for public wording that could sound too certain about eligibility, service availability, housing placement, money or benefit outcomes, legal rights or deadlines, current contact routes, or partnership/endorsement.

## Files Reviewed

- `research/owner-review-shortlist-2026-04-30.md`
- `STATE.md`
- `ROADMAP.md`
- `research/qa-report.md`
- `index.html`
- `quellen.html`
- `scripts/check-site.py`

## Changes Made

- Softened a small set of homepage sentences so they use more cautious wording such as "kann", "prüfen", and "zuständige Stelle".
- Kept emergency routes visible.
- Left `quellen.html` public wording unchanged after review.
- Added this automation report and a short QA note in `research/qa-report.md`.

## Safety Notes

- No new public factual claims were added.
- No legal, benefit, housing, emergency, health, organization, contact, phone, email, operator, or impressum details were added.
- No partnership, endorsement, placement, eligibility, benefit, legal-deadline, or service-availability promise was added.

## Checks Run

- `python3 scripts/check-site.py --today 2026-04-30 --report-review-dates` - passed.
- `python3 -m py_compile scripts/check-site.py` - passed.
- `git diff --check` - passed.
- `cat CNAME` - confirmed `careleaver.eu`.
