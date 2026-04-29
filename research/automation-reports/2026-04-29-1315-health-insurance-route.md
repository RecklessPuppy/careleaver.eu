# Automation Report: Health Insurance Route

Date: 2026-04-29 13:15 CEST
Mode: overnight autonomous

## Summary

- Added a cautious health, E-Card, and insurance route to the public homepage.
- Used already logged official source anchors: Gesundheitsportal Österreich for general Care Leaver health context and ÖGK for mitversicherung information.
- Added matching source/review visibility and checker guardrails so the route keeps its safety wording.

## Files Changed

- `index.html`
- `quellen.html`
- `research/source-log.md`
- `scripts/check-site.py`
- `STATE.md`
- `research/automation-reports/2026-04-29-1315-health-insurance-route.md`

## Checks

- `git pull --ff-only origin main`: pass, already up to date.
- `git status --short --branch`: pass, branch was clean before edits.
- Official-source spot check: pass for Gesundheitsportal Österreich and ÖGK pages.
- `python3 scripts/check-site.py --today 2026-04-29 --report-review-dates`: pass.
- `python3 -m py_compile scripts/check-site.py`: pass.
- Inline JavaScript syntax check for `index.html` and `quellen.html`: pass.
- `git diff --check`: pass.
- `cat CNAME`: pass, exactly `careleaver.eu`.
- `python3 scripts/check-site.py --today 2026-04-29 --external --external-timeout 30`: pass.
- Local HTTP preview for `/` and `/quellen.html`: pass, both returned `HTTP 200`.
- `wkhtmltoimage --width 390` for `/` and `/quellen.html`: pass with macOS LaunchServices warning only.
- `wkhtmltoimage --width 1280` for `/`: pass with macOS LaunchServices warning only.
- `wkhtmltopdf --print-media-type` for `/`: pass with macOS LaunchServices warning only.
- `qpdf --check /private/tmp/careleaver-health-route-index-print.pdf`: pass.
- Visual smoke-check of rendered 390 px screenshots: pass.

## Factual Safety

- Public factual content touched: yes.
- Source log updated: yes.
- Open questions added: no.
- No diagnosis, therapy recommendation, treatment guidance, insurance decision, eligibility promise, amount, deadline, phone number, email, address, opening hour, backend, analytics, form, or personal-data collection was added.

## Remaining Risk / Human Review

- Health and insurance wording should stay cautious unless refreshed against official sources.
- The owner/human reviewer should include the new health route in the next factual review before broad outreach.
- Operator/contact/impressum details remain unresolved and must not be invented by automation.
- Dedicated axe/assistive-technology testing is still recommended when browser tooling is available.

## Next Recommended Task

- Run the human factual review packet against the current public Wien MVP, now including the health/insurance route.
