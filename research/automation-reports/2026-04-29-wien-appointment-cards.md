# Wien Appointment Cards

Date: 2026-04-29

## What Changed

- Added a new static `Wien Termin-Karten` section to `index.html`.
- Added five provider-specific appointment-prep cards:
  - Care Leaver Beratung / MA 11
  - U25 / Geld / soziale Unterstützung
  - Wohnbeihilfe / MA 50
  - Wohnkrise / FSW Wohnungslosenhilfe
  - KIJA / Beschwerde / Vertrauensperson
- Updated `quellen.html` with a public review-table row and changelog note for the new cards.
- Updated `research/source-log.md` with an audit note for the public factual wording change.
- Extended `scripts/check-site.py` so local/CI checks guard the required appointment-card count, labels, official-page warning, and review dates.

## Why This Was Safe

- The cards reuse existing official/source-log links.
- The cards avoid copied phone numbers, emails, addresses, opening hours, benefit amounts, thresholds, legal deadlines, eligibility promises, appointment promises, housing promises, and service promises.
- The wording focuses on preparation questions and asks users to check the official page for decisions.
- The implementation remains static, printable, mobile-friendly, and no-JS compatible.

## Public Factual Content Changed

Yes. Public content changed because new provider-specific Wien appointment-prep cards were added.

No new source entries were needed because the cards only reuse existing official links already tracked in `research/source-log.md`.

## Checks Run

- `python3 scripts/check-site.py` - passed.
- `python3 -m py_compile scripts/check-site.py` - passed.
- `git diff --check` - passed.
- `cat CNAME` - passed; exact content remains `careleaver.eu`.
- `python3 scripts/check-site.py --external --soft-external` inside sandbox - completed with DNS warnings because sandbox network could not resolve external hosts.
- `python3 scripts/check-site.py --external --soft-external` with approved network access - passed; external links OK.
- Temporary localhost preview on port 8029 - used for render checks, then stopped.
- `wkhtmltoimage --width 390` for `index.html` - passed; output `/private/tmp/careleaver-wien-appointment-mobile.png`.
- Visual mobile screenshot smoke-check - passed for obvious overlap in the rendered page.
- `wkhtmltopdf --print-media-type` for `index.html` - passed; output `/private/tmp/careleaver-wien-appointment-print.pdf`.
- `qpdf --check /private/tmp/careleaver-wien-appointment-print.pdf` - passed.

## Next Recommended Task

Include the new appointment-prep cards in the next human factual review before broad outreach, alongside crisis, housing, money, contacts, and legal-background wording.
