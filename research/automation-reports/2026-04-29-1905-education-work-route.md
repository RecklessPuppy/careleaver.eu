# Automation Report: Education Work Route

Date: 2026-04-29 19:05 CEST
Mode: overnight autonomous

## Summary

- Added a dedicated "Schule, Lehre oder Arbeit" route to the homepage router, Nächste-Schritte-Finder, and no-JavaScript fallback.
- Connected the route to the existing Wien education/work card with an `#arbeit` anchor.
- Updated public changelog, source log, QA report, checker guardrails, and project state.
- The change was safe and useful because it uses already logged official education/work sources, improves the main routing experience, and avoids eligibility, age, benefit, deadline, job, training, or contact-detail claims.

## Files Changed

- `index.html`
- `quellen.html`
- `scripts/check-site.py`
- `research/source-log.md`
- `research/qa-report.md`
- `STATE.md`
- `research/automation-reports/2026-04-29-1905-education-work-route.md`

## Checks

- `python3 scripts/check-site.py --today 2026-04-29 --report-review-dates`: pass
- `python3 -m py_compile scripts/check-site.py`: pass
- `git diff --check`: pass
- `cat CNAME`: pass, exact `careleaver.eu`
- `python3 scripts/check-site.py --today 2026-04-29 --external --external-timeout 30`: pass
- Local HTTP preview for `/` and `/quellen.html`: pass, both returned `HTTP 200`

## Factual Safety

- Public factual content touched: yes, limited to routing/preparation wording for education/work.
- Source log updated: yes, noting reuse of existing NEBA, AusBildung bis 18, waff, and U25 source anchors.
- Open questions added: not needed.
- No eligibility rules, age ranges, benefit amounts, deadlines, copied contact details, job/training promises, backend, analytics, form submissions, or server-side data collection were added.

## What Remains Risky Or Needs Human Review

- Human factual review is still needed before broad outreach because the Wien MVP covers crisis, housing, money, health, contacts, and Jugendhilfe routes.
- Verified operator/contact/impressum details remain unresolved and should not be invented by automation.
- Dedicated axe/assistive-technology accessibility testing remains recommended.

## Next Recommended Task

- Run the human factual review of the Wien MVP against `research/human-review-packet-2026-04-29.md`, then schedule a dedicated axe/assistive-technology accessibility pass.
