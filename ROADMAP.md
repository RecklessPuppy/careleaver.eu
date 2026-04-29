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
- draft content architecture in `content/architecture.md`
- draft page structures in `content/page-drafts/`
- draft practical templates in `content/templates/`

Status: research swarm and content architecture pass completed 2026-04-29; claim-by-claim public-page audit still pending.

## Phase 1A: Content Architecture Drafts

Goal: turn research into a low-maintenance information architecture before rebuilding the public site.

- Define the first useful site map.
- Draft the first homepage structure.
- Draft the Wien page structure.
- Draft a generic Bundesland page template.
- Draft appointment-prep and Jugendhilfe email templates.
- Define source/review-date display patterns.
- List content that should not be published until verified.
- Identify the lowest effort, highest impact build plan.

Deliverables:

- `content/architecture.md`
- `content/page-drafts/home.md`
- `content/page-drafts/wien.md`
- `content/page-drafts/bundesland-template.md`
- `content/templates/appointment-prep.md`
- `content/templates/email-jugendhilfe.md`

Status: completed 2026-04-29.

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

Status: completed as a first public MVP pass on 2026-04-29. A second QA/fact-check pass is still recommended before broad outreach.

## Phase 2: Austria / Wien MVP

Goal: publish a reliable, useful Wien-first version.

- Use the draft architecture in `content/` as the source for the build. Status: first pass done 2026-04-29.
- Make emergency and crisis information clear and source-linked. Status: first pass done; recheck quarterly.
- Verify Wien contacts, phone numbers, addresses, and links. Status: official-link-first approach used; second QA still needed.
- Verify key Wien child/youth welfare and aftercare claims. Status: source-linked first pass done; legal wording should stay cautious.
- Verify benefits, housing, appointment, and document guidance. Status: source-linked first pass done; no benefit amounts published.
- Improve wording for plain German and low-stress reading. Status: first pass done.
- Keep the site static, mobile-friendly, and printable. Status: first pass done; browser QA still needed.
- Add a top "Ich brauche Hilfe mit ..." router. Status: done.
- Add Wien appointment-prep kits for MA 11/Care Leaver counselling, U25, MA 50/Wohnbeihilfe, KIJA, and housing crisis. Status: generic practical templates added; provider-specific templates can be expanded after QA.
- Add short German scripts for calls, emails, written decisions, and bringing a trusted person. Status: first pass done.
- Prefer official contact pages over copied contact details where possible. Status: done in the public MVP.

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
- Add safe structured data without operator/contact or partnership claims. Status: first WebSite/WebPage/BreadcrumbList pass completed 2026-04-29, with JSON-LD guardrails in `scripts/check-site.py`.
- Add source and update dates visibly.
- Add clear contact/impressum information only after verified.
- Keep public source/review information easy to find. Status: first public `quellen.html` page added 2026-04-29.
- Consider outreach to care leaver organizations, youth workers, and relevant Wien/Austria support services.
- Add analytics only if the privacy tradeoff is explicitly accepted.
- Use practical German search language such as "Care Leaver Wien", "nach der Jugendhilfe", "mit 18 aus der Jugendhilfe", "Care Leaver Beratung Wien", "Wohnbeihilfe Wien", and "U25 Wien".
- Prefer Google Search Console over visitor analytics for early query discovery.
- Do not imply partnership with Care Leaver Oesterreich or other organizations without permission.

## Phase 6: Maintenance Automation

Goal: keep information from becoming stale.

- Create a regular source review routine. Status: first runbook and prompts added 2026-04-29.
- Track time-sensitive claims and review dates. Status: source log and public review dates exist; `scripts/check-site.py` now checks public/source-log review dates, warns before due dates, and fails strict checks once a review date is overdue.
- Automate link checks if tooling is added. Status: basic GitHub Actions internal-link/placeholder/required-file check added 2026-04-29; optional external HTTP link smoke check added 2026-04-29 for manual/local runs and scheduled CI warnings.
- Keep same-domain public URLs checked locally before deployment. Status: `scripts/check-site.py` now validates `careleaver.eu` links against local files.
- Add lightweight accessibility checks to the repeatable QA path. Status: static HTML accessibility guardrails added to `scripts/check-site.py` on 2026-04-29.
- Consider scheduled Codex maintenance prompts. Status: `prompts/06-overnight-operator.md` and `prompts/07-morning-review.md` added 2026-04-29.
- Keep a simple changelog of factual updates.

## Phase 6A: Overnight Autonomous Mode

Goal: let Codex make unattended safe progress while the owner sleeps.

- Add an overnight runbook. Status: completed 2026-04-29.
- Add a reusable automation prompt for unattended work. Status: completed 2026-04-29.
- Add a morning review prompt. Status: completed 2026-04-29.
- Add an automation report folder. Status: completed 2026-04-29.
- Update `AGENTS.md`, `OPERATING_MODEL.md`, and `STATE.md` so future runs know the rules. Status: completed 2026-04-29.
- Keep each run small enough to review, but complete enough to be useful.
- Use reports in `research/automation-reports/` as the overnight audit trail.

Status: setup completed 2026-04-29. Actual overnight improvement cycles can now start.
