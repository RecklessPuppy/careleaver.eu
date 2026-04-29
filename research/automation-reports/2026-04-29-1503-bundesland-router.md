# Automation Report: Bundesland Router Safety

Date: 2026-04-29
Mode: overnight autonomous

## Summary

- Added an explicit "Nicht in Wien" path to the homepage router, Next-Step Finder, and no-JavaScript fallback.
- Strengthened the Bundeslaender beta wording so Wien examples are not read as verified contact or jurisdiction information for other Bundeslaender.
- Added checker guardrails and public/internal notes for the routing safety change.

## Why It Was Safe

- The change helps prevent misusing Wien-specific information outside Wien.
- It does not add Bundesland contacts, eligibility rules, deadlines, benefit amounts, service promises, emergency routes, backend behavior, analytics, forms, or data collection.
- The only new public guidance is cautionary: use official Bundesland sources until a real source pass exists.

## Files Changed

- `index.html`
- `quellen.html`
- `scripts/check-site.py`
- `research/source-log.md`
- `research/qa-report.md`
- `STATE.md`

## Checks

- `python3 scripts/check-site.py --today 2026-04-29 --report-review-dates`: pass
- `python3 -m py_compile scripts/check-site.py`: pass
- inline JavaScript syntax checks for `index.html` and `quellen.html`: pass
- `git diff --check`: pass
- `cat CNAME`: pass, contains `careleaver.eu`
- `python3 scripts/check-site.py --today 2026-04-29 --external --external-timeout 30`: pass
- Local HTTP preview for `/` and `/quellen.html`: pass, both returned `HTTP 200`

## Factual Safety

- Public factual content touched: no new source-dependent facts; cautionary regional routing only.
- Source log updated: yes, with a no-new-source routing note.
- Open questions added: not needed.

## What Remains Risky Or Needs Human Review

- Non-Wien Bundesland content remains incomplete until each Bundesland has its own official source set.
- Human factual review remains needed before broad outreach.
- Verified operator/contact/impressum/offenlegung details remain an owner decision.
- A dedicated axe/assistive-technology accessibility pass remains recommended.

## Next Recommended Task

- Run the human factual review packet in `research/human-review-packet-2026-04-29.md`, then do the dedicated axe/assistive-technology accessibility pass.
