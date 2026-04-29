# QA Report

Last updated: 2026-04-29

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
10. Last-reviewed dates: PASS. Public source/review dates are visible by claim group. Crisis, money, housing, contacts, and time-sensitive routes remain on 2026-07-29 review cycles.

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

TODO - Automated recurring link/source checks: add monthly link checking and quarterly source review for crisis, money, housing, and contacts.

TODO - Browser accessibility audit: static guardrails now run locally and in CI, but a full axe/browser audit is still useful once the browser test setup is stable.

TODO - Benefits/legal expansion: do not add amounts, thresholds, appeal deadlines, or entitlement wording without fresh official sources and source-log entries.

TODO - Bundesland expansion: keep non-Wien Bundesländer as "in Arbeit" until each has its own official source set.

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
