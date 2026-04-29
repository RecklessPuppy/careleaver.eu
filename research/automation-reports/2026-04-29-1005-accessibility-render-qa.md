# Automation Report: Accessibility Render QA

Date: 2026-04-29 10:05 CEST
Mode: overnight autonomous

## Summary

- Improved mobile/accessibility resilience for the public pages without changing factual guidance.
- Added table captions, keyboard-focusable labelled wide-table regions, and predictable breakpoint-based heading sizes.
- Extended the static checker so these accessibility/layout improvements stay enforced.

## Files Changed

- `index.html`
- `quellen.html`
- `scripts/check-site.py`
- `research/qa-report.md`
- `research/automation-reports/2026-04-29-1005-accessibility-render-qa.md`
- `STATE.md`

## Checks

- `python3 scripts/check-site.py`: pass
- `python3 -m py_compile scripts/check-site.py`: pass
- inline JavaScript syntax check with `node --check`: pass
- `git diff --check`: pass
- `python3 scripts/check-site.py --external`: pass
- `cat CNAME`: pass, still `careleaver.eu`
- local HTTP smoke check `/`: pass, HTTP 200
- local HTTP smoke check `/quellen.html`: pass, HTTP 200
- `wkhtmltoimage --width 390` for `/`: pass
- `wkhtmltoimage --width 1280` for `/`: pass
- `wkhtmltoimage --width 390` for `/quellen.html`: pass
- `wkhtmltopdf --print-media-type` for `/`: pass
- `qpdf --check /private/tmp/careleaver-index-print-after.pdf`: pass

## Factual Safety

- Public factual content touched: no.
- Source log updated: not needed.
- Open questions added: not needed.
- No legal, benefit, housing, emergency, contact, deadline, eligibility, or health claims were changed.

## Tooling Note

- Playwright CLI could not complete in this sandbox. The first attempt hit npm cache ownership errors; after redirecting caches to `/private/tmp`, Chrome launch/cleanup still failed. Rendered wkhtml image/PDF checks were used as the fallback preview path.

## Next Recommended Task

- Fix the Playwright/Chrome local launch environment, then run a full modern-browser/axe accessibility pass on `index.html` and `quellen.html`.
