# QA Report

Last updated: 2026-04-30

Scope: strict safety, quality, and fact-check review of the current public `index.html` for `careleaver.eu`.

## Summary

The Wien-first MVP is mostly cautious and source-linked. It avoids legal/benefit decisions, avoids copied non-emergency contact directories, discloses local browser storage, and uses respectful practical language.

Safe fixes shipped in this QA pass:

- Added a visible BMI source pill for DEC112/SMS emergency information in the crisis area.
- Fixed sticky navigation behavior so desktop offset follows the real crisis-bar height and mobile navigation stays static instead of covering content.
- Added table header `scope="col"` attributes for better screen-reader semantics.
- Added an inline favicon to remove the local browser 404 console error.

## Checks

1. Broken links: PASS. Link check found no missing internal anchors and all unique external `index.html` links returned HTTP 200 on 2026-04-29. FMA and Care Leaver Österreich needed GET fallback because HEAD was not accepted.
2. Placeholder text: PARTIAL. No lorem/old fake contact fields found. The public footer still says verified operator/contact/impressum details must be added before broad outreach; this is a real unresolved TODO, not safe to guess.
3. Unsupported legal/benefit/contact claims: PASS WITH CAUTION. The page links to official sources and avoids benefit amounts, legal deadlines, or entitlement promises. `§ 33 WKJHG` is linked only as legal background.
4. Crisis/emergency wording: IMPROVED. Immediate danger routes are visible. PSD Wien, Rat auf Draht, and BMI sources support the displayed crisis routes. Text-based emergency information now has a visible BMI source pill.
5. Mobile usability: FIXED. Playwright check at 390x844 found no horizontal page overflow, but the sticky nav offset was smaller than the actual crisis bar. Desktop nav now uses a measured offset; mobile nav is static so it does not cover content.
6. Accessibility basics: IMPROVED. The page has `lang`, skip link, landmarks, labelled form controls, visible focus styles, and accessible checkbox labels. Table column scopes were added. A later automation pass added static HTML accessibility guardrails to `scripts/check-site.py`; a full browser/axe audit is still a future improvement after a stable test setup exists.
7. Privacy concerns: PASS WITH CAUTION. No backend, tracking, analytics, or form submission. Checklist state and explicitly saved drafts use `localStorage`; shared-device risk and deletion are disclosed.
8. Tone: PASS. Tone is practical and respectful. It avoids savior language and avoids blaming the young person.
9. Official sources linked where needed: PASS WITH CAUTION. High-risk sections link mainly to official or operator pages. The page should keep preferring official pages over copied contact blocks.
10. Last-reviewed dates: IMPROVED. Public source/review dates are visible by claim group. A later automation pass added review-date checks to `scripts/check-site.py`, so public/source-log review dates now warn before they are due and fail strict checks when overdue. Crisis, money, housing, contacts, and time-sensitive routes remain on 2026-07-29 review cycles.
11. Sitemap/canonical consistency: IMPROVED. A later automation pass added local checks that root HTML pages have the expected canonical URL, appear in `sitemap.xml`, and stay connected from `robots.txt`.

## Fact-Check Notes

- BMI supports 112, 133, 144, 147, DEC112, and 0800 133 133 emergency information.
- Rat auf Draht supports the 147 youth advice route as free/confidential and reachable around the clock.
- PSD Wien supports 01 31330 as a daily 0-24 psychiatric crisis route for Wien.
- Stadt Wien supports Care Leaver counselling up to the 24th birthday and the MA 11 Servicestelle as a central guide.
- Stadt Wien U25 supports routing for Wiener*innen under 25 around work, education, and social issues.
- Stadt Wien Wohnbeihilfe supports the official application/underlagen route, but the public page correctly avoids eligibility promises and amounts.
- FSW supports cautious homelessness/housing-crisis routing and does not support a guaranteed placement claim.
- waff source says the youth job-offensive wording is 18-24; the public page currently avoids stating an age range and links users to verify directly.

## Risky TODOs

TODO - Operator/impressum/contact details: do not invent these. The site needs verified public operator, contact, and impressum/legal owner details before broad outreach.

TODO - Human factual review before outreach: a second human review is still recommended because the site covers crisis, housing, benefits, and youth-welfare routing.

TODO - Automated recurring source checks: link checks and review-date guardrails now exist, but they only flag reachability and due dates. A human or careful source-refresh pass still has to reopen crisis, money, housing, and contact sources by the review date.

TODO - Dedicated axe/assistive-technology audit: static guardrails now run locally and in CI, and a Playwright browser/mobile pass was completed on 2026-04-29. A focused axe and assistive-technology review is still useful before broad outreach.

TODO - Benefits/legal expansion: do not add amounts, thresholds, appeal deadlines, or entitlement wording without fresh official sources and source-log entries.

TODO - Bundesland expansion: keep non-Wien Bundesländer as "in Arbeit" until each has its own official source set.

## Automation QA Addendum 2026-04-29 10:05

- Added hidden captions to public review/source tables and made the wide table regions keyboard-focusable with accessible labels.
- Replaced viewport-relative heading font sizing with breakpoint-based fixed sizes to keep mobile/desktop text sizing more predictable.
- Extended `scripts/check-site.py` to fail future public tables without captions and future public `font-size` rules that use viewport units.
- Rendered mobile/desktop image and print PDF smoke checks passed after the changes.
- Playwright CLI still could not complete because of local npm cache and Chrome launch/cleanup permissions; a full modern-browser/axe audit remains useful when that environment is fixed.

## Browser/Mobile/Accessibility Addendum 2026-04-29

- Used Playwright/Chromium against a local static server for `/` and `/quellen.html` at 320, 390, 768, 1024, and 1440 px widths.
- Initial findings: the homepage had a small 320 px horizontal overflow caused by checklist text/grid sizing; mobile keyboard focus could move partly below or outside the viewport in the homepage/source-page navigation; primary link-buttons could inherit the global red hover color and fail contrast on dark button backgrounds.
- Safe fixes shipped: checklist copy now shrinks and wraps inside the 320 px viewport; button-link hover colors now keep adequate contrast; both public pages now keep focused elements scrolled into view for keyboard users.
- Post-fix Playwright findings: no horizontal overflow at tested widths, no sticky crisis/nav coverage after anchor jumps, skip links visible with a 3 px focus outline, router/checklist/template interactions passed, homepage no-JavaScript fallback passed, no computed contrast failures found at 390 and 1024 px, and print media hid interactive/sticky chrome.
- Print check: Playwright print media generated PDFs for `/` and `/quellen.html`; `qpdf --check` found no syntax or stream errors.
- Visual mobile screenshot smoke check at 390 px found no obvious top-viewport overlap on `/` or `/quellen.html`.
- No factual public claims, links, contact details, legal/benefit/housing/health/emergency instructions, backend, analytics, forms, or personal-data collection were added.

## Template Privacy Addendum 2026-04-29

- Added `autocomplete="off"` to the remaining free-text fields in the appointment and one-page-plan templates.
- Extended `scripts/check-site.py` so sensitive template fields with `plan-` or `appointment-` IDs must keep browser autocomplete disabled.
- This reduces accidental reuse of sensitive appointment text on shared devices, but it does not replace the visible shared-device warning or the "Lokale Daten löschen" action.
- No factual public claims, contact details, legal/benefit/housing wording, emergency instructions, backend, analytics, forms, or server-side data collection were added.

## Bundesland Router Addendum 2026-04-29

- Added an explicit "not in Wien / anderes Bundesland" route to the public topic router, no-JavaScript fallback, and Next-Step Finder.
- The route warns that Wien examples should not be read as contact or jurisdiction information for other Bundeslaender.
- Extended `scripts/check-site.py` so the non-Wien route and cautious Bundesland wording stay present.
- No Bundesland contacts, eligibility rules, deadlines, benefit amounts, service promises, emergency routes, backend, analytics, forms, or server-side data collection were added.

## Brief / Fristen Route Addendum 2026-04-29

- Added a dedicated public route for "Brief, Bescheid oder mögliche Frist" in the homepage router, no-JavaScript fallback, and Next-Step Finder.
- Added a practical card in the documents section for sorting official letters: mark dates, sender, reference numbers, keep a copy, ask for a written explanation, and get help quickly if a deadline may exist.
- Extended `scripts/check-site.py` so the route, finder option, anchor, and "Diese Website berechnet keine Fristen" safety wording remain present.
- No legal deadline, appeal period, legal advice, eligibility rule, benefit amount, contact detail, backend, analytics, form submission, or server-side data collection was added.

## Glossary Lesehilfe Addendum 2026-04-29

- Added a public "Begriffe schnell erklärt" section for common bureaucratic words such as Bescheid, Frist, Aktenzeichen/Geschäftszahl, Meldezettel, Vertrauensperson, and zuständige Stelle.
- The section is framed as a reading aid only and tells users to ask the responsible office or a counselling route when a word matters in a real letter.
- Added public source/review rows and a changelog note for the glossary.
- Extended `scripts/check-site.py` so the glossary anchor, safety wording, and source-page changelog note remain present.
- No legal deadline, appeal instruction, eligibility rule, benefit amount, service promise, contact detail, backend, analytics, form submission, or server-side data collection was added.

## Begleitperson Template Addendum 2026-04-29

- Added a copyable "Vertrauensperson fragen" script to the public templates.
- The script helps users ask a trusted person to sort questions, listen, write notes, or ask follow-up questions.
- Safety wording says to ask the relevant office whether and how the person can be involved, and to share only necessary private details in messages.
- Extended `scripts/check-site.py` so the support-person script and cautious wording remain present.
- No legal right to accompaniment, service promise, eligibility rule, deadline, benefit amount, contact detail, backend, analytics, form submission, or server-side data collection was added.

## Arbeits-/Ausbildungsroute Addendum 2026-04-29

- Added a dedicated "Schule, Lehre oder Arbeit" route to the public topic router, no-JavaScript fallback, and Next-Step Finder.
- The route points users toward the existing official education/work source group and asks them to prepare questions and documents for the next realistic step.
- Extended `scripts/check-site.py` so the route, finder option, anchor, and source-page changelog note remain present.
- No eligibility rule, age range, benefit amount, job/training promise, deadline, contact detail, backend, analytics, form submission, or server-side data collection was added.

## Print Link Visibility Addendum 2026-04-29

- Added print CSS so external official links show their full URLs when `index.html`, `quellen.html`, or printed template popups are printed.
- Extended `scripts/check-site.py` so both public pages keep the print URL guardrail.
- Added a short public changelog note on `quellen.html`.
- No public factual claims, contact details, legal/benefit/housing/health/emergency instructions, backend, analytics, forms, or personal-data collection were added.

## Broad Outreach Readiness Addendum 2026-04-29

- Added an optional `scripts/check-site.py --readiness` gate for pre-outreach checks.
- The normal site check still passes and remains suitable for routine pushes.
- The readiness gate intentionally fails while owner-level blockers remain: unchecked human review packet items, unresolved operator/contact/impressum questions, Care Leaver Österreich referral/outreach review, and the public note that broad-outreach blockers remain.
- Added a manual GitHub Actions input so the owner can run the readiness gate from workflow dispatch without changing the default push/scheduled checks.
- No public factual claim, contact detail, legal/benefit/housing/health/emergency instruction, backend, analytics, form submission, or server-side data collection was added.

## Termin-Nachbereitung Addendum 2026-04-29

- Added a copyable "Nach dem Termin kurz bestätigen" script to the public templates.
- Linked the existing "Nach dem Termin" document card to the new follow-up script.
- Extended `scripts/check-site.py` so the follow-up script, cautious no-deadline-calculation wording, and public changelog note remain present.
- No legal deadline, appeal advice, eligibility rule, benefit amount, service promise, contact detail, backend, analytics, form submission, or server-side data collection was added.

## Unterlagen-Nachreichung Addendum 2026-04-29

- Added a copyable "Unterlagen nachreichen" script to the public templates.
- Linked the existing "Nach dem Termin" document card to the new document-submission script.
- Extended `scripts/check-site.py` so the document-submission script, cautious copy/scan/original wording, and public changelog note remain present.
- No legal deadline, appeal advice, eligibility rule, benefit amount, service promise, contact detail, backend, analytics, form submission, or server-side data collection was added.

## Copy Fallback Addendum 2026-04-30

- Added a copy fallback for public template buttons when `navigator.clipboard` is unavailable or blocked.
- The fallback uses a temporary readonly textarea selection, restores focus afterward, and reports success through the existing screen-reader status message.
- Updated `scripts/check-site.py` so the Clipboard API guard and fallback remain present.
- Added a public changelog note on `quellen.html` and updated sitemap/JSON-LD modification dates.
- No factual public claim, contact detail, legal/benefit/housing/health/emergency instruction, backend, analytics, form submission, or server-side data collection was added.

## Sources Checked

- https://www.bmi.gv.at/notrufnummern/
- https://www.rataufdraht.at/telefonberatung
- https://psd-wien.at/einrichtung/sozialpsychiatrischer-notdienst
- https://www.wien.gv.at/zusammenleben/care-leaver-beratung
- https://www.wien.gv.at/zusammenleben/servicestelle-kinder-jugendhilfe
- https://www.wien.gv.at/amtswege/anmelden-wohnsitz
- https://www.wien.gv.at/amtswege/wohnbeihilfe-antrag
- https://www.wien.gv.at/kontakt/ma40-u25-jugendunterstuetzung
- https://www.fsw.at/p/wohnungslosigkeit
- https://www.waff.at/beruf-weiterbildung/jugendliche-und-berufseinstieg/
- https://www.neba.at/jugendcoaching
- https://kija-wien.at/
- https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=LrW&Gesetzesnummer=20000259&Paragraf=33
