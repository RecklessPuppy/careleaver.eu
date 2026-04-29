# Automation Report: Broad Outreach Readiness Guardrail

Date: 2026-04-29 21:05 Europe/Vienna
Mode: overnight autonomous

## Summary

- Added an optional broad-outreach readiness gate to `scripts/check-site.py`.
- Added a manual GitHub Actions workflow input to run that gate without blocking normal pushes.
- The gate fails clearly while owner-level blockers remain: unchecked human review items, operator/contact/impressum decisions, Care Leaver Oesterreich referral/outreach wording review, and public broad-outreach blocker notes.
- This was safe because it changed maintenance automation and internal documentation only; it did not strengthen or add public factual advice.

## Files Changed

- `.github/workflows/site-check.yml`
- `scripts/check-site.py`
- `ROADMAP.md`
- `STATE.md`
- `research/qa-report.md`
- `research/automation-reports/2026-04-29-2105-broad-outreach-readiness.md`

## Checks

- `python3 scripts/check-site.py --today 2026-04-29 --report-review-dates`: pass.
- `python3 -m py_compile scripts/check-site.py`: pass.
- `git diff --check`: pass.
- `cat CNAME`: pass, still `careleaver.eu`.
- `python3 scripts/check-site.py --today 2026-04-29 --external --external-timeout 30`: pass.
- Local HTTP preview for `/` and `/quellen.html`: pass, both returned `HTTP 200`.
- `python3 scripts/check-site.py --today 2026-04-29 --readiness`: expected fail on known broad-outreach blockers.

## Factual Safety

- Public factual content touched: no.
- Source log updated: not needed.
- Open questions added: not needed.
- No contact detail, eligibility rule, benefit amount, legal deadline, emergency route, health advice, backend, analytics, form submission, or server-side personal-data collection was added.

## Notes

- I also tried `@axe-core/cli` locally against `/` and `/quellen.html`, but local Chrome/ChromeDriver still failed to start. This confirms the dedicated axe/assistive-technology review remains a separate tooling task.

## Next Recommended Task

- Owner completes `research/human-review-packet-2026-04-29.md` and confirms operator/contact/impressum/offenlegung wording, then runs `python3 scripts/check-site.py --readiness` or the manual GitHub Actions readiness input before broad outreach.
