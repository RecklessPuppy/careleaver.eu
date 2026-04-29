# Content Architecture: First Useful Version

Last updated: 2026-04-29

Status: draft for review. This is not yet the public site.

Inputs used:

- `research/research-synthesis.md`
- `research/source-log.md`
- `research/open-questions.md`
- `ROADMAP.md`
- `SOURCE_POLICY.md`
- `CONTENT_SAFETY.md`

## Product Direction

The first useful version should be a Wien-first, Austria-scoped guide:

> Care Leaver Wien: Hilfe nach der Kinder- und Jugendhilfe.

The domain can stay `careleaver.eu`, but the visible product promise should not suggest Europe-wide coverage. The homepage should say clearly that the site starts with Wien and expands across Austria only after source checks.

The site should help a young person or trusted helper answer:

- What should I do next?
- Who is the right official or trusted contact in Wien?
- What should I prepare before a call, email, or appointment?
- Which claims are sourced, and when were they last checked?
- What is still in progress or not verified?

It should not become:

- a legal advice service
- a benefits decision tool
- a therapy or emergency service
- a chatbot
- a broad stale contact directory
- a Europe-wide Care Leaver portal before research exists

## 1. Proposed Site Map

Lowest-maintenance public shape:

- `/`
  - Start page and router.
  - Explains Wien-first scope.
  - Shows urgent help routes.
  - Routes users by need: crisis, housing, money, Jugendhilfe/Care Leaver counselling, documents, rights/complaints, templates.
- `/wien/` or `wien.html`
  - First complete MVP page.
  - Source-dated Wien guide.
  - Uses official pages and appointment preparation instead of copying every phone/address detail.
- `/bundeslaender/` or `bundeslaender.html`
  - Austria overview.
  - Shows Wien as available.
  - Other Bundeslaender say "in Arbeit" until official source sets exist.
- `/bundeslaender/[bundesland]/` later
  - One Bundesland at a time.
  - Only publish after a source log exists for that Bundesland.
- `/vorlagen/` or `vorlagen.html`
  - Appointment prep.
  - Email to Jugendhilfe.
  - Call scripts.
  - Document checklist.
  - "Please give that to me in writing" script.
- `/quellen/` or `quellen.html`
  - Public source and review-date overview.
  - Should be generated manually from `research/source-log.md` at first.
- `/hinweise/` or footer section
  - Not legal advice, not therapy, not emergency service.
  - Privacy note.
  - Impressum/contact only after verified.
  - Independence/non-affiliation note for Care Leaver Oesterreich unless collaboration is agreed.

Implementation note: the first build does not need all of these as separate HTML files. It is acceptable to keep a single static page with clear anchors first, then split pages only when maintenance becomes easier that way.

## Suggested Navigation Labels

Use practical German labels:

- Start
- Wien
- Schnelle Hilfe
- Wohnen
- Geld & Arbeit
- Jugendhilfe
- Rechte & Beschwerde
- Vorlagen
- Bundeslaender
- Quellen

Avoid navigation labels that sound like official decisions, for example:

- Anspruchs-Check
- Rechtsanspruch berechnen
- Leistungsrechner
- Garantierte Hilfe

Safer replacement labels:

- Naechste-Schritte-Finder
- Termin vorbereiten
- Was kann ich fragen?
- Unterlagenliste

## 2. First Homepage Structure

The homepage should be a calm router, not a marketing landing page.

Recommended order:

1. Header
   - H1: `Care Leaver Wien: Hilfe nach der Jugendhilfe`
   - Subline: `Praktische Schritte, Vorlagen und offizielle Links fuer Wien. Andere Bundeslaender sind in Arbeit.`
   - Small scope note: `Diese Seite startet Wien-first und ist unabhaengig.`

2. Urgent help strip
   - Immediate danger: 112 / 133 / 144.
   - Youth crisis/advice: Rat auf Draht 147.
   - Wien mental-health crisis: PSD Wien official page/phone if source-checked.
   - Text-based emergency route: DEC112/SMS only after source display is verified.
   - Source note visible in or directly below the strip.

3. "Ich brauche Hilfe mit ..."
   - Large tap targets for:
     - Wohnen / keine sichere Unterkunft
     - Geld, AMS, U25, Schulden
     - Jugendhilfe / Care Leaver Beratung
     - Termin vorbereiten
     - Dokumente
     - Rechte, Beschwerde, Vertrauensperson
     - Anderes Bundesland

4. "Heute ein kleiner naechster Schritt"
   - Three low-pressure actions:
     - official page oeffnen
     - Unterlagenliste starten
     - eine Person bitten, zum Termin mitzukommen

5. Wien first
   - Short explanation that Wien is the first complete section because the source base is currently strongest.
   - Button/link: `Zur Wien-Seite`.

6. Templates
   - Appointment prep.
   - Email Jugendhilfe.
   - "Bitte schriftlich" script.

7. Sources and review dates
   - Explain that high-risk facts get source links and review dates.
   - Link to source/review overview.

8. Footer notes
   - Not legal advice.
   - Not medical/therapy advice.
   - Not an emergency service.
   - Independent information/navigation site.
   - Impressum/contact only after verified.

## 3. Wien Page Structure

The Wien page is the first complete MVP page.

Recommended order:

1. Header
   - H1: `Wien: Hilfe nach der Kinder- und Jugendhilfe`
   - Scope note: `Fuer Care Leaver und Menschen, die sie unterstuetzen.`
   - Last checked summary: `Wien-Quellen zuletzt geprueft: 2026-04-29` only for sources actually checked then.

2. Schnelle Hilfe in Wien
   - Immediate danger.
   - Mental-health crisis.
   - Youth advice.
   - Unsafe housing / homelessness risk.
   - Violence/acute safety concern.
   - Use official source links near the section.

3. Was ist gerade dein Thema?
   - Router cards to sections:
     - Ich verlasse bald die Jugendhilfe.
     - Ich bin schon ausgezogen und brauche Hilfe.
     - Ich habe keine sichere Unterkunft.
     - Ich brauche Geld/AMS/U25/Sozialhilfe-Klaerung.
     - Ich habe einen Brief/Bescheid bekommen.
     - Ich will jemanden mitnehmen oder mich beschweren.

4. Care Leaver Beratung und MA 11
   - Link to City of Vienna Care Leaver counselling page.
   - Link to MA 11 Servicestelle.
   - Carefully state only sourced, current claims.
   - Prefer: `Die offizielle Seite beschreibt ...`
   - Avoid: `Du hast sicher Anspruch auf ...`

5. Wohnen
   - First-flat prep.
   - Meldezettel link to exact City of Vienna registration page.
   - Wohnbeihilfe / MA 50 official application link.
   - Wohnberatung Wien official page.
   - Housing crisis route through official FSW/P7/official provider pages after verification.
   - Do not promise placement.

6. Geld, AMS, U25, Schulden
   - U25 as official route for under-25 Wien users, carefully sourced.
   - AMS/MA 40 appointment prep.
   - Basiskonto source.
   - OBS/ORF contribution exemption source.
   - Schuldenberatung Wien source.
   - Do not publish benefit amounts, thresholds, or fee amounts unless freshly checked.

7. Schule, Ausbildung, Arbeit
   - NEBA / Jugendcoaching.
   - AusBildung bis 18.
   - waff only after age range is corrected and sourced.

8. Gesundheit und Krise
   - PSD Wien for acute psychiatric crisis.
   - Rat auf Draht for youth advice.
   - OeGK link for insurance questions.
   - No diagnosis or treatment advice.

9. Rechte, Beschwerde, Vertrauensperson
   - KIJA Wien.
   - Written decisions / ask for written explanation.
   - Trusted person/begleitung script.
   - Wien legal background only with cautious wording.

10. Termin vorbereiten
    - Appointment-prep checklist.
    - Document checklist.
    - Email/call scripts.
    - Print-friendly one-page plan.

11. Sources and review dates
    - Source list grouped by section.
    - Review-by dates.
    - "Bitte pruefe aktuelle Details direkt auf der offiziellen Seite" note for contacts/opening hours.

12. What is still being checked
    - Known open questions from `research/open-questions.md`.
    - Bundeslaender outside Wien.
    - Public contact/impressum placeholders.

## 4. Generic Bundesland Page Template

Do not clone the Wien page and change names. Each Bundesland needs its own source pass.

Required template:

1. Header
   - `[Bundesland]: Hilfe nach der Kinder- und Jugendhilfe`
   - Status badge:
     - `in Arbeit`
     - `teilweise geprueft`
     - `geprueft am YYYY-MM-DD`

2. Scope and safety note
   - What this page covers.
   - What is not verified yet.

3. Immediate help
   - National emergency numbers only if current source is linked.
   - Bundesland-specific crisis routes only after official source checks.

4. Official child/youth welfare route
   - Responsible Bundesland/city authority.
   - Care Leaver/aftercare wording only if official source supports it.

5. Rights/ombuds route
   - KIJA or equivalent ombuds office.
   - Source-linked.

6. Housing
   - Housing benefit, homelessness, youth housing, first-flat routes.
   - Use official contact pages first.
   - Avoid copied phone/address details until checked.

7. Money/work/education
   - AMS, Sozialhilfe/Mindestsicherung route, training/youth employment routes.
   - Avoid eligibility promises.

8. Health/crisis
   - Official crisis and health routes.
   - No clinical advice.

9. Appointment prep
   - Reuse generic templates.
   - Add local official links only after verification.

10. Sources and review dates
    - Claim-group source blocks.
    - Review schedule.

11. Open questions
    - Visible if page is not complete.

If a Bundesland is not researched, publish only:

> Diese Seite ist in Arbeit. Wien ist derzeit die erste vollstaendigere Version. Bitte nutze bis dahin offizielle Stellen deines Bundeslandes und KIJA/Ombudsstellen. Wir veroeffentlichen hier erst konkrete Kontakte, wenn sie aus offiziellen Quellen geprueft sind.

## 5. Template / Script Section Structure

Templates should be practical and printable. They should not collect personal data on a server.

Recommended `/vorlagen/` sections:

1. Appointment prep
   - What is the appointment about?
   - What do I want to ask?
   - What documents might help?
   - Who can come with me?
   - What do I need in writing afterwards?

2. Email to Jugendhilfe / MA 11 / responsible office
   - Short version.
   - Detailed version.
   - Safer privacy wording: do not include more sensitive detail than needed by email.

3. Phone script
   - "I need an appointment."
   - "I do not understand the next step."
   - "Can you tell me which documents to bring?"

4. Trusted-person script
   - "I would like to bring a person I trust."
   - "Please speak so both of us understand the next step."

5. Written-decision script
   - "Can you please give me that in writing?"
   - "Please write the reason and the next possible step."

6. After-appointment note
   - Date.
   - Person/service.
   - What was agreed.
   - Deadline.
   - Next contact.

7. Source reminder
   - Every service-specific template must link to the relevant official service page.

## 6. Source And Review-Date Pattern

Use this pattern next to high-risk content, not hidden at the bottom:

```md
Quelle: [Source title](https://example.at)
Betreiber: Official owner / publisher
Geprueft am: YYYY-MM-DD
Naechste Pruefung: YYYY-MM-DD
Gilt fuer: short claim group, for example "Wien Care Leaver Beratung"
Hinweis: Details wie Telefon, Oeffnungszeiten, Betraege und Voraussetzungen bitte direkt auf der offiziellen Seite pruefen.
```

For compact UI:

```text
Quelle: Stadt Wien, geprueft 2026-04-29, naechste Pruefung 2026-07-29.
```

Review interval defaults from `SOURCE_POLICY.md`:

- Emergency and crisis contacts: every 3 months.
- Benefits, fees, thresholds, deadlines: every 3 months.
- Legal process summaries: every 6 months or after known law changes.
- General explanatory content: every 12 months.
- Broken links: ideally monthly once tooling exists.

Rules:

- Do not update `Geprueft am` unless the source was actually reopened and checked.
- Do not copy phone numbers, addresses, fees, or opening hours without a review-by date.
- Use official pages as the source of truth.
- If a claim cannot be sourced, soften it or move it to open questions.

## 7. Content Not To Publish Until Verified

Do not publish these as public facts until checked against official/current sources:

- Any copied phone number, address, email address, opening hour, appointment route, or provider name.
- Crisis-bar details beyond well-sourced emergency routes.
- PSD Wien 24/7 wording unless checked against the current PSD page.
- DEC112 and 0800 133 133 wording unless the exact route and audience are checked.
- Exact eligibility wording for Wien Care Leaver counselling.
- Any statement that a person "has a right to" or "will receive" a service unless legal conditions are clear and sourced.
- `§ 33 WKJHG` wording that sounds like a guaranteed entitlement.
- Benefit amounts, thresholds, age limits, deadlines, fees, or reductions.
- Basiskonto fee amounts.
- Family allowance and health-insurance age wording unless split and sourced separately.
- ORF contribution exemption wording unless using OBS/current source.
- waff age range until the 18-24 vs 18-25 mismatch is resolved.
- Housing placement claims, especially emergency accommodation or youth housing.
- Provider-specific offers outside Wien.
- Bundesland pages outside Wien beyond "in Arbeit" placeholders.
- Any implication of partnership with Care Leaver Oesterreich / `careleaver.at` unless agreed.
- Impressum/contact details that still contain placeholders.
- Any tool that stores sensitive data locally unless the shared-device risk is clearly explained and deletion is easy.

## 8. Lowest Effort, Highest Impact Build Plan

Keep the site static. Do not add a framework, backend, CMS, forms, analytics, or generated PDFs for the MVP.

Recommended sequence:

1. Safety pass on current `index.html`
   - Rename "Anspruchs-Check" to "Naechste-Schritte-Finder" or "Vorbereitungs-Check".
   - Soften legal/benefit outcome language.
   - Add visible source/last-checked notes to high-risk sections.
   - Replace weak ORF/Meldezettel links with source-log-backed official links.
   - Add non-affiliation wording.

2. Add a top router
   - "Ich brauche Hilfe mit ..."
   - Anchor links to existing sections.
   - No big redesign needed.

3. Make Wien the visible MVP
   - Change the public promise from broad Austria/Europe to Wien-first Austria scope.
   - Keep Bundeslaender outside Wien as "in Arbeit".

4. Add template sections
   - Appointment prep.
   - Email Jugendhilfe.
   - Written decision / trusted-person scripts.
   - Print-friendly, no server storage.

5. Prefer official contact-page links
   - Remove or reduce copied contact details unless recently checked.
   - This lowers maintenance risk.

6. Add source review rhythm
   - Track review-by dates in source notes.
   - Later add a simple link checker only if maintenance becomes difficult.

7. Only then consider splitting pages
   - Start with anchors in one page if easiest.
   - Split into `wien.html`, `vorlagen.html`, and `bundeslaender.html` only when that makes updates clearer.

## What To Review Before Public Build

Review:

- Whether `careleaver.eu` should show an independence note near the header.
- What verified Impressum/contact details should appear.
- Whether localStorage tools should be removed, opt-in, or session-only.
- Whether copied contact details should be replaced by official contact-page buttons.
- Whether the current one-page structure is still manageable after adding source notes.
