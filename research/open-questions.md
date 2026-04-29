# Open Questions

Last updated: 2026-04-29

Use this file for unresolved claims, missing sources, and decisions that should not be guessed.

## High Priority

- What exact email, phone number, and operator details may appear in the accessibility/impressum/contact area? The old public placeholders were removed on 2026-04-29, but verified public operator/contact details still need a user decision.
- Should Care Leaver Oesterreich be asked to review or approve any referral wording before outreach?
- Before broad outreach, should a human fact reviewer sign off on the 2026-04-29 QA findings in `research/qa-report.md`?
- Should public operator/impressum resolution happen before search indexing is encouraged or partner outreach starts?
- Should any benefit/legal topics remain link-only permanently, even after source checks, to avoid accidental advice?

## Medium Priority

- After the 2026-04-29 rewrite, does any part of the new "Naechste-Schritte-Finder" still sound like a legal/benefit decision rather than preparation and routing?
- Should each section show a visible "last checked" date after the source audit?
- Should localStorage autosave be further reduced, for example checklist-only with no saved drafts, before broad outreach?
- What exact shared-device privacy warning should appear before tools that store appointment/legal details locally?
- Which Bundesland should be expanded after Wien, and only after which official source set exists?
- Should Wien source sections show review dates per claim group: crisis, housing, money, documents, contacts?
- Should the site include a public changelog for factual updates?
- Which old/source-weak public claims should be softened or removed during the Wien MVP content pass?

## Resolved Or Lowered By 2026-04-29 QA

- Independence/non-affiliation: public page now says the site is independent and does not claim partnership with Care Leaver Österreich.
- Crisis-bar contacts: 112, 133, 144, 147, PSD Wien, DEC112 and SMS 0800 133 133 were checked against BMI/Rat auf Draht/PSD sources on 2026-04-29; next review 2026-07-29.
- Crisis section depth: a fuller "Schnelle Hilfe in Wien" section was added to the public page on 2026-04-29 using already logged BMI/Rat auf Draht/PSD/FSW sources.
- Safe-use note: the public page now includes a short "So nutzt du diese Seite sicher" note near the top router.
- PSD Wien 24/7 wording: sourced from PSD Wien on 2026-04-29; next review 2026-07-29.
- `§ 33 WKJHG`: public page links RIS as legal background and does not summarize eligibility as an entitlement.
- Wien contact details: public page avoids copied non-emergency phone/address/opening-hour blocks and uses official contact pages instead.
- Basiskonto/family allowance/health insurance: public page avoids amounts and compressed eligibility claims.
- ORF/OBS: public page links to OBS for exemption/support checks.
- waff: public page avoids the old `18-25` claim and links to waff directly; source-log records visible `18-24` wording.
- Meldezettel: public page links to the exact Stadt Wien residence-registration page.
- Automated link checking: `scripts/check-site.py` now supports `--external` for strict manual/local HTTP link checks and scheduled GitHub Actions runs external checks as soft warnings.

## Product Decisions

- Keep one long page, or split into multiple static pages after the Wien MVP is source-audited?
- Should the next build start with a top "Ich brauche Hilfe mit ..." router?
- Should appointment-prep kits be sections on the same page or separate print-friendly static pages?
- Should printable PDFs be avoided for now to reduce duplicate maintenance risk?
- Should contact cards prefer "official page" buttons instead of repeating phone/address details?

## Lower Priority / Later Expansion

- Which provider-specific Care Leaver offers outside Wien are currently active and for whom: Pro Juventute, Diakonie de La Tour, Vorarlberger Kinderdorf, Land Tirol, KIJA OOE, others?
- Which Bundesland pages should cite official KIJA/ombuds routes first?
- Is `careleaver.wien` / the "Durchblick fuer Wiener Careleaver:innen" brochure current enough to use as a user-facing source, or only as secondary context?
- Should the site include Schema.org metadata, and if yes, only WebSite/WebPage/BreadcrumbList until the operator identity is settled?
