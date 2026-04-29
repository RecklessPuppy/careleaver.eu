# Browser/Mobile/Accessibility Pass - 2026-04-29

## Summary

Safe post-MVP browser QA was completed against the current static site using a local preview server and Playwright/Chromium. The pass focused on rendered mobile behavior, keyboard accessibility, no-JavaScript resilience, print media, and contrast without changing public factual content.

## Files Changed

- `index.html`
- `quellen.html`
- `research/qa-report.md`
- `STATE.md`
- `research/automation-reports/2026-04-29-browser-mobile-accessibility.md`

## Checks Run And Results

- `git pull --ff-only origin main`: passed; already up to date.
- `git status --short --branch`: branch was `main...origin/main` before edits.
- `python3 scripts/check-site.py`: passed before and after edits.
- `python3 -m py_compile scripts/check-site.py`: passed before and after edits.
- `python3 scripts/check-site.py --external`: passed; external links OK.
- `git diff --check`: passed before and after edits.
- `CNAME` exact display: `careleaver.eu`.
- Local HTTP preview for `/`: `HTTP 200`.
- Local HTTP preview for `/quellen.html`: `HTTP 200`.
- Playwright/Chromium browser QA at 320, 390, 768, 1024, and 1440 px for `/` and `/quellen.html`: passed after fixes.
- Playwright no-JavaScript check at 390 px: homepage fallback visible, JS-only action buttons hidden, no overflow; source page had no JS-only controls to hide.
- Playwright print-media check: sticky/action chrome hidden, no overflow, white print background.
- Playwright print PDFs for `/` and `/quellen.html`: generated in `/private/tmp`.
- `qpdf --check /private/tmp/careleaver-index-print-playwright.pdf`: passed.
- `qpdf --check /private/tmp/careleaver-quellen-print-playwright.pdf`: passed.
- Playwright 390 px viewport screenshots for `/` and `/quellen.html`: visually smoke-checked for obvious overlap.

## Browser/Mobile/Accessibility Findings

- Found and fixed a 320 px homepage horizontal overflow caused by checklist text/grid sizing.
- Found and fixed link-button hover contrast where global link hover styling could override button text color.
- Found and fixed mobile keyboard focus visibility problems where focused navigation links could sit partly outside the viewport.
- Confirmed no sticky crisis bar or navigation coverage after anchor jumps at tested widths.
- Confirmed skip links are first in tab order, visible on focus, and show a 3 px outline.
- Confirmed router, checklist save/clear, template draft save/reload/clear, and print-clone behavior worked in Playwright.
- Confirmed public tables remain keyboard-focusable horizontal-scroll regions. Large table regions cannot fit fully inside one mobile viewport, but their focused region remains visible and scrollable.
- Computed contrast check found no remaining failures at 390 or 1024 px after the hover fix.

## Public Factual Content Changed

No. This pass changed CSS and small browser-side focus behavior only. It did not add or change service facts, legal/benefit/housing/health/emergency instructions, phone numbers, addresses, opening hours, eligibility rules, deadlines, organization details, external links, forms, analytics, backend services, tracking, secrets, or personal-data collection.

## Unresolved Blockers

- A dedicated axe/assistive-technology pass is still recommended before broad outreach.
- Human factual review is still needed for crisis, housing, money, contacts, and legal-background wording.
- Verified operator/contact/impressum details remain unresolved and must not be invented.

## Next Recommended Task

Run a human factual review of the Wien MVP against `research/source-log.md` and `research/qa-report.md`, starting with crisis, housing, money, contacts, and legal-background wording.
