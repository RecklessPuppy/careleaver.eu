# Automation Report: Template Privacy Hardening

Date: 2026-04-29
Mode: overnight autonomous

## Summary

- Disabled browser autocomplete on the remaining free-text fields in the one-page-plan and appointment-prep templates.
- Added a static checker guardrail so sensitive `plan-` and `appointment-` template fields keep `autocomplete="off"`.
- Added a short public changelog note and updated QA/state documentation.

## Why It Was Safe

- The change only affects static HTML attributes, QA checks, and documentation.
- It does not add or change factual claims, contact details, legal/benefit/housing/health wording, emergency routing, backend behavior, analytics, forms, or server-side data collection.
- The privacy improvement supports the existing shared-device warning and local-data deletion pattern.

## Files Changed

- `index.html`
- `quellen.html`
- `scripts/check-site.py`
- `research/qa-report.md`
- `STATE.md`
- `research/automation-reports/2026-04-29-1404-template-privacy.md`

## Checks

- `python3 scripts/check-site.py --today 2026-04-29 --report-review-dates`: pass
- `python3 -m py_compile scripts/check-site.py`: pass
- `git diff --check`: pass
- `cat CNAME`: pass, contains `careleaver.eu`
- `python3 scripts/check-site.py --today 2026-04-29 --external --external-timeout 30`: pass
- Local HTTP preview for `/` and `/quellen.html`: pass, both returned `HTTP 200`

## Factual Safety

- Public factual content touched: no.
- Source log updated: not needed.
- Open questions added: not needed.

## What Remains Risky Or Needs Human Review

- Browser autocomplete settings reduce accidental retention, but cannot guarantee privacy on every shared device or browser.
- Human factual review is still needed before broad outreach.
- Verified operator/contact/impressum/offenlegung details remain an owner decision.
- A dedicated axe/assistive-technology accessibility pass remains recommended.

## Next Recommended Task

- Run the human factual review packet in `research/human-review-packet-2026-04-29.md`, then do the dedicated axe/assistive-technology accessibility pass.
