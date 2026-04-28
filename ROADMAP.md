# Roadmap

Last updated: 2026-04-29

This roadmap keeps the project moving in phases. The safer default is to finish each phase well before expanding the scope.

## Current MVP Decision

The single best MVP direction after the 2026-04-29 research swarm is:

> A Wien-first, source-dated "Was mache ich als Naechstes?" guide for Care Leavers after child/youth welfare.

The site should help users prepare for real support routes: crisis help, MA 11 / Wien Care Leaver counselling, housing, money, U25/AMS/education, health, documents, appointments, and rights/complaints.

It should not become a legal encyclopedia, benefit calculator, chatbot, backend service, advocacy organization, or broad stale contact database.

## Phase 0: Repo / Project Setup

Goal: make the project understandable to future Codex chats and maintainers.

- Add project operating files.
- Document content safety rules.
- Document source policy.
- Confirm static GitHub Pages structure.
- Preserve `CNAME` and custom domain.
- Keep Git status clean after setup.

Status: completed 2026-04-29.

## Phase 1: Research And Content Map

Goal: know what content exists, what is sourced, and what needs checking.

- Run research swarm for needs, Wien services, existing organizations, UX/product, SEO/reach, and safety.
- Build a source log for legal, benefit, emergency, health, housing, and contact claim groups.
- Mark stale, weak, or missing sources.
- Create a content map for Wien MVP.
- Decide which existing content should stay, change, or be removed until verified.
- Audit current `index.html` claim-by-claim before public factual rewrites.

Deliverables:

- updated `research/source-log.md`
- updated `research/research-synthesis.md`
- updated `research/open-questions.md`
- a clear Wien MVP content outline

Status: research swarm completed 2026-04-29; claim-by-claim public-page audit still pending.

## Phase 1B: Wien Safety And Source Audit

Goal: make the current public page safer before broad use.

- Audit `index.html` against `research/source-log.md`.
- Add visible source links and "last checked" dates to high-risk sections.
- Replace or soften unsupported legal, benefit, housing, and contact claims.
- Rename "Anspruchs-Check" to a safer routing/prep name.
- Replace generic or weak links, including ORF -> OBS and Meldepflicht -> exact Wien registration page.
- Check and correct the waff age range.
- Add non-affiliation wording for Care Leaver Oesterreich unless collaboration is agreed.
- Add shared-device/localStorage safety wording if tools keep local saving.
- Resolve Impressum/contact placeholders before outreach.

Deliverables:

- safer `index.html`
- updated `research/source-log.md` for any public factual edits
- updated `research/open-questions.md` for unresolved claims

Status: next recommended build step.

## Phase 2: Austria / Wien MVP

Goal: publish a reliable, useful Wien-first version.

- Make emergency and crisis information clear and source-linked.
- Verify Wien contacts, phone numbers, addresses, and links.
- Verify key Wien child/youth welfare and aftercare claims.
- Verify benefits, housing, appointment, and document guidance.
- Improve wording for plain German and low-stress reading.
- Keep the site static, mobile-friendly, and printable.
- Add a top "Ich brauche Hilfe mit ..." router.
- Add Wien appointment-prep kits for MA 11/Care Leaver counselling, U25, MA 50/Wohnbeihilfe, KIJA, and housing crisis.
- Add short German scripts for calls, emails, written decisions, and bringing a trusted person.
- Prefer official contact pages over copied contact details where possible.

## Phase 3: Bundesland Expansion

Goal: expand carefully beyond Wien.

- Add one Bundesland at a time.
- Start each Bundesland with official sources and KIJA/ombuds routes.
- Keep "in progress" placeholders where information is not yet verified.
- Avoid copying Wien-specific assumptions into other Bundeslaender.
- Use provider-specific offers only after eligibility and access routes are verified.

## Phase 4: Templates / Tools

Goal: add practical appointment and planning tools without collecting sensitive data.

- Improve document checklists.
- Add appointment preparation templates.
- Add printable one-page plans.
- Add source-linked explainers for common processes.
- Keep tools browser-side where possible.
- Avoid storing personal data on a server.
- Avoid separately maintained PDFs until print styles are stable, so facts do not diverge.
- Consider opt-in or session-only local storage for sensitive fields.

## Phase 5: Outreach / SEO

Goal: help people find and trust the site.

- Improve page titles, descriptions, and headings.
- Add source and update dates visibly.
- Add clear contact/impressum information only after verified.
- Consider outreach to care leaver organizations, youth workers, and relevant Wien/Austria support services.
- Add analytics only if the privacy tradeoff is explicitly accepted.
- Use practical German search language such as "Care Leaver Wien", "nach der Jugendhilfe", "mit 18 aus der Jugendhilfe", "Care Leaver Beratung Wien", "Wohnbeihilfe Wien", and "U25 Wien".
- Prefer Google Search Console over visitor analytics for early query discovery.
- Do not imply partnership with Care Leaver Oesterreich or other organizations without permission.

## Phase 6: Maintenance Automation

Goal: keep information from becoming stale.

- Create a regular source review routine.
- Track time-sensitive claims and review dates.
- Automate link checks if tooling is added.
- Consider scheduled Codex maintenance prompts.
- Keep a simple changelog of factual updates.
