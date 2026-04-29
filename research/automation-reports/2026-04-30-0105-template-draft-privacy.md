# Automation Report: Template Draft Privacy

Date: 2026-04-30 01:05 CEST
Mode: overnight autonomous

## Summary

- Changed the public template draft flow so saved free-text drafts no longer auto-load when the homepage opens.
- Added a visible "Gespeicherten Entwurf laden" button for deliberate restore.
- Added a checker guardrail so future edits fail if `DOMContentLoaded` restores saved free-text drafts automatically again.
- Added public and internal notes for the change.

## Files Changed

- `index.html`
- `quellen.html`
- `scripts/check-site.py`
- `ROADMAP.md`
- `STATE.md`
- `research/source-log.md`
- `research/qa-report.md`
- `research/automation-reports/2026-04-30-0105-template-draft-privacy.md`

## Checks

- `python3 scripts/check-site.py --today 2026-04-30 --report-review-dates`: pass.
- `python3 -m py_compile scripts/check-site.py`: pass.
- `git diff --check`: pass.
- `cat CNAME`: pass, still `careleaver.eu`.
- Inline JavaScript `node --check`: pass.
- `python3 scripts/check-site.py --today 2026-04-30 --external --external-timeout 30`: pass.
- Local HTTP preview on port 4176: `/` and `/quellen.html` returned `HTTP 200`; served homepage HTML included the new explicit draft-load control and privacy wording.

## Factual Safety

- Public factual content touched: no.
- Source log updated: yes, with a no-new-claims maintenance note.
- Open questions added: no, not needed.
- No legal deadline, appeal advice, eligibility rule, benefit amount, service promise, contact detail, backend, analytics, form submission, or server-side data collection was added.

## Remaining Risks Or Human Review

- Users can still voluntarily store sensitive free-text drafts in browser `localStorage`; the safer pattern now requires explicit save and explicit load, and the existing delete button remains available.
- Owner factual review, verified operator/contact/impressum details, and dedicated axe/assistive-technology testing remain unresolved before broad outreach.
- The local preview server on port 4176 could not be terminated from the sandbox after preview because process signalling was denied.

## Next Recommended Task

- Run the human factual review packet in `research/human-review-packet-2026-04-29.md`, then decide verified operator/contact/impressum wording before broad outreach.
