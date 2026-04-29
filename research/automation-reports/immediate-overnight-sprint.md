# Automation Report: Immediate Overnight Sprint

Date: 2026-04-29
Mode: overnight autonomous

## Summary

- Improved the live homepage before scheduled automation starts.
- Added a fuller "Schnelle Hilfe in Wien" section, a safe-use note near the main router, and a printable one-page appointment plan.
- Removed the remaining public footer placeholder text about missing contact/impressum details; the unresolved decision remains tracked internally.
- Added a reusable local QA script and made GitHub Actions call it directly.

## Files Changed

- `index.html`
- `.github/workflows/site-check.yml`
- `scripts/check-site.py`
- `research/source-log.md`
- `research/open-questions.md`
- `STATE.md`
- `research/automation-reports/immediate-overnight-sprint.md`

## Checks

- `git pull --ff-only origin main`: pass
- `git status --short --branch`: pass
- `python3 scripts/check-site.py`: pass
- `git diff --check`: pass
- `cat CNAME`: pass, contains `careleaver.eu`
- `wkhtmltoimage` mobile and desktop render smoke checks: pass
- `sips` image dimension checks: pass
- `wkhtmltopdf --print-media-type`: pass
- `qpdf --check /private/tmp/careleaver-print.pdf`: pass
- `pdftotext /private/tmp/careleaver-print.pdf -`: pass

Browser note: Playwright CLI did not complete and no local Playwright package was available, so this sprint used static checks plus wkhtml image/PDF smoke checks instead of a modern Chromium interaction pass.

## Factual Safety

- Public factual content touched: yes, crisis/safety routing.
- Source log updated: yes.
- Open questions added: no; two existing questions were lowered/resolved.
- New sources added: no.
- Unsupported legal/contact/emergency claims added: no.
- Contact/impressum details invented: no.

## Next Recommended Task

- Let the scheduled automation add a lightweight external-link check that can run when network is available, or improve print/no-JavaScript polish for the template section. Do not expand non-Wien Bundesland content yet.
