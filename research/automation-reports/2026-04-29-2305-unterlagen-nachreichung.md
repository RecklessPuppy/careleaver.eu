# Automation Report: Unterlagen-Nachreichung

Date: 2026-04-29 23:05 +0200
Mode: overnight autonomous

## Summary

- Added a copyable "Unterlagen nachreichen" script to the public templates.
- Linked the existing "Nach dem Termin" document card to the new script.
- Added a public changelog note and local checker guardrails so the script and cautious copy/scan/original wording stay present.

## Files Changed

- `index.html`
- `quellen.html`
- `scripts/check-site.py`
- `ROADMAP.md`
- `STATE.md`
- `research/source-log.md`
- `research/qa-report.md`

## Checks

- Static site check with review-date report: pass.
- Python compile for `scripts/check-site.py`: pass.
- Whitespace diff check: pass.
- `CNAME` check: pass, still `careleaver.eu`.
- Strict external link check: pass.
- Local HTTP preview for `/` and `/quellen.html`: pass, both returned `HTTP 200`.
- Mobile render smoke check with `wkhtmltoimage --width 390`: pass.
- Print PDF smoke check with `wkhtmltopdf`: pass.
- `qpdf --check` on print PDF: pass.
- `pdftotext` on print PDF: pass, the new template appears in print output.
- Optional broad-outreach readiness gate: failed as expected on known owner-review and operator/impressum blockers.
- Playwright CLI preview: attempted, but Chrome launch still failed in the local sandbox; render/print smoke checks were used as fallback.

## Factual Safety

- Public factual content touched: no new factual claims.
- Source log updated: yes, as a safety note for the template change.
- Open questions added: no, not needed.
- The new wording does not add legal advice, deadline calculation, eligibility rules, benefit amounts, service promises, contact details, backend, analytics, forms, or server-side data collection.

## Remaining Risk Or Human Review

- The template asks users to check document format and possible dates directly with the responsible office or a counselling route.
- Owner factual review, verified operator/contact/impressum/offenlegung details, Care Leaver Österreich outreach/referral review, and dedicated axe/assistive-technology testing remain unresolved before broad outreach.

## Next Recommended Task

- Owner should complete `research/human-review-packet-2026-04-29.md` and decide verified operator/contact/impressum/offenlegung wording before broad outreach.
