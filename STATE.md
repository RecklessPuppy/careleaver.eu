# State

Last updated: 2026-04-29

## Current Status

- Repo is cloned locally at `/Users/hardwork/Developer/Codex/workspaces/careleaver.eu`.
- Current branch: `main`.
- Remote: `origin` points to `https://github.com/RecklessPuppy/careleaver.eu.git`.
- Site is a static GitHub Pages site.
- Public live site: `https://careleaver.eu`.
- Custom domain is preserved through `CNAME`, which contains `careleaver.eu`.
- Current public site has two static HTML pages: `index.html` and `quellen.html`, plus `robots.txt` and `sitemap.xml`.
- The site is German-language and now explicitly Wien-first.
- The site includes source-sensitive material: emergency numbers, Wien routes, rights/background, deadlines, benefit/housing notes, and health/crisis routes.
- A research swarm was completed on 2026-04-29 to decide the product direction before public content changes.
- A content architecture pass was completed on 2026-04-29 to turn the research into reviewable page/template drafts.
- A public Wien-first MVP pass was completed on 2026-04-29.
- A focused safety/fact/link/mobile QA pass was completed on 2026-04-29 and logged in `research/qa-report.md`.
- An overnight autonomous operating setup was added on 2026-04-29, including runbook, prompts, report folder, and lightweight GitHub Actions checks.
- An immediate overnight implementation sprint was completed on 2026-04-29 before scheduled automation, focused on public usefulness, safe routing, and repeatable QA.
- An external-link smoke-check pass was completed on 2026-04-29, adding optional networked HTTP link checks to local/manual QA and scheduled CI warnings.
- A no-JavaScript and print resilience pass was completed on 2026-04-29, focused on the public router and templates.
- A public source/review page pass was completed on 2026-04-29, adding `quellen.html`, sitemap coverage, and local same-domain URL validation.
- A lightweight accessibility-check pass was completed on 2026-04-29, adding static HTML accessibility guardrails to `scripts/check-site.py`.
- A source-review automation pass was completed on 2026-04-29, adding public/source-log review-date checks to `scripts/check-site.py`.
- A homepage quick-action pass was completed on 2026-04-29, adding a low-pressure "Heute ein kleiner nächster Schritt" block near the top router.
- A safe structured-data SEO pass was completed on 2026-04-29, adding WebSite/WebPage/BreadcrumbList JSON-LD and guardrails against premature owner/contact schema.
- A sitemap/canonical consistency pass was completed on 2026-04-29, extending `scripts/check-site.py` so page canonicals, `sitemap.xml`, and `robots.txt` stay aligned.
- A morning review was completed on 2026-04-29: latest `main` was already up to date, the latest GitHub Actions runs were green, live `index.html`, `quellen.html`, and `sitemap.xml` matched local `main` by SHA-256 hash, and the workflow checkout action was updated to `actions/checkout@v6` to address the Node.js 20 deprecation warning.

## Morning Review 2026-04-29

### Current Status

- Local branch: `main`, aligned with `origin/main` before the morning fix.
- Public site: `https://careleaver.eu` served HTTP 200 for `/`, `/quellen.html`, and `/sitemap.xml` during the morning check.
- Live files matched local `main` by SHA-256 hash for `index.html`, `quellen.html`, and `sitemap.xml`.
- GitHub Actions: the latest checked runs were successful. The latest site-check run had a warning because `actions/checkout@v4` uses the deprecated Node.js 20 runtime; the workflow now uses `actions/checkout@v6`.
- `CNAME` still contains exactly `careleaver.eu`.

### What Changed Overnight

- The project moved from initial setup into a Wien-first public MVP.
- `index.html` was rebuilt around practical routing, crisis-first help, Wien routes, appointment/email/phone templates, print/no-JavaScript resilience, and cautious source-linked wording.
- `quellen.html` was added as a public source/review and changelog page.
- `robots.txt`, `sitemap.xml`, `.github/workflows/site-check.yml`, `scripts/check-site.py`, runbooks, prompts, research logs, and automation reports were added or expanded.
- The shared checker now covers required files, `CNAME`, placeholders, internal links, optional external links, static accessibility basics, source-review dates, safe JSON-LD, sitemap/canonical consistency, and robots sitemap consistency.

### Needs Human Review

- Operator/contact/impressum details are still unresolved and should not be invented by automation.
- A human factual review is still recommended before broad outreach because the public site covers crisis, housing, benefits, health, and child/youth welfare routing.
- Non-Wien Bundesland content remains intentionally incomplete until official source sets are reviewed.
- Care Leaver Österreich / `careleaver.at` referral and outreach wording should be reviewed before implying any collaboration.
- Browser-based accessibility testing is still missing; static checks are useful guardrails but do not replace a real browser/assistive-technology pass.

### Next 3 Recommended Tasks

1. Run a real browser/mobile accessibility pass on `index.html` and `quellen.html`, then fix only layout or accessibility issues that do not change facts.
2. Do a human factual review of the Wien MVP against `research/source-log.md` and `research/qa-report.md`, especially crisis, housing, money, contacts, and legal-background wording.
3. Decide verified operator/contact/impressum wording, then add it carefully to the public site and structured data only after the details are confirmed.

## What Was Added In This Setup Pass

- Repo operating docs.
- Prompt templates for future Codex workflows.
- Research scaffolding for source logging, synthesis, and open questions.

## What Was Added In The Research Swarm Pass

- Updated `research/research-synthesis.md` with the single recommended MVP direction.
- Updated `research/source-log.md` with official and trustworthy source anchors for Wien Care Leaver support, crisis, housing, money, education/work, documents, organizations, and safety-sensitive claims.
- Updated `research/open-questions.md` with remaining high-risk factual and product decisions.
- Updated `ROADMAP.md` with Phase 1B as the next build step.

## What Was Added In The Content Architecture Pass

- Added `content/architecture.md` with the proposed site map, homepage/Wien/Bundesland structures, template structure, source/review-date pattern, unsafe-to-publish list, and low-effort build plan.
- Added page drafts:
  - `content/page-drafts/home.md`
  - `content/page-drafts/wien.md`
  - `content/page-drafts/bundesland-template.md`
- Added template drafts:
  - `content/templates/appointment-prep.md`
  - `content/templates/email-jugendhilfe.md`
- Updated `ROADMAP.md` to record the content architecture deliverables.
- The public `index.html` was intentionally not rebuilt in this pass.

## What Was Added In The Public MVP Pass

- Rebuilt `index.html` as the first useful public Wien-first version.
- Kept the implementation static and simple: no framework, backend, package manager, analytics, or form submission.
- Added top "Was brauchst du gerade?" routing.
- Added a safer 18-24 checklist.
- Added Wien starter routes for crisis, Care Leaver Beratung/MA 11, housing, money/U25, Ausbildung/Arbeit, rights/complaints, and community/self-representation.
- Added templates/scripts for appointments, email, phone calls, and "bitte schriftlich".
- Added a Bundeslaender beta section that keeps non-Wien regions "in Arbeit" until source checks exist.
- Added a visible source/review table with reviewed and next-review dates.
- Replaced the old "Anspruchs-Check" decision framing with a "Naechste-Schritte-Finder".
- Removed old public placeholder contact/impressum fields; verified operator/contact details remain an owner decision before broad outreach.
- Improved privacy wording and localStorage behavior: checkboxes save locally; free-text template drafts save only after an explicit user action.
- Added `robots.txt` and `sitemap.xml`.

## What Was Added In The QA Pass

- Added `research/qa-report.md` with the safety, link, fact, mobile, accessibility, privacy, tone, source, and review-date findings.
- Rechecked all unique external links in `index.html`; all returned HTTP 200 on 2026-04-29.
- Rechecked key official sources for crisis, Wien Care Leaver counselling, MA 11, U25, housing, money, education/work, KIJA, and WKJHG legal background.
- Added a visible BMI source pill for DEC112/SMS emergency information in the public crisis area.
- Fixed sticky navigation behavior so desktop offset follows the real crisis-bar height and mobile navigation stays static instead of covering content.
- Added table column scopes and an inline favicon.
- Updated `research/source-log.md` to record that the QA pass happened and to replace the old "still needs claim-by-claim audit" note.

## What Was Added In The Overnight Setup Pass

- Updated `AGENTS.md` with an overnight autonomous mode.
- Expanded `OPERATING_MODEL.md` with autonomous-pass expectations.
- Added `OVERNIGHT_RUNBOOK.md`.
- Added `prompts/06-overnight-operator.md` for recurring unattended Codex runs.
- Added `prompts/07-morning-review.md` for the owner after waking.
- Added `research/automation-reports/` with a README and the first dated setup report.
- Added `.github/workflows/site-check.yml` for required-file, `CNAME`, public-placeholder, and internal-link checks on push, manual dispatch, and a daily schedule.
- No public factual content was changed in this setup pass.

Checks run in this setup pass:

- `git pull --ff-only origin main`
- `git diff --check`
- `CNAME` exact-content check
- required-file check
- public placeholder grep for `index.html`, `robots.txt`, and `sitemap.xml`
- internal-link check for local HTML anchors
- YAML parse check for `.github/workflows/site-check.yml`

## What Was Added In The Immediate Overnight Sprint

- Added a fuller public "Schnelle Hilfe in Wien" section before the main router, using already logged BMI, Rat auf Draht, PSD Wien, and FSW source anchors.
- Added a short "So nutzt du diese Seite sicher" note near "Was brauchst du gerade?" so users see the limits before relying on money, housing, youth-welfare, or rights content.
- Added a printable "Ein-Seiten-Plan fuer den naechsten Termin" in the templates section.
- Removed the remaining public footer paragraph that described missing contact/impressum placeholders; the unresolved owner decision stays in `research/open-questions.md` instead of public user content.
- Added `scripts/check-site.py` and simplified `.github/workflows/site-check.yml` so local and CI checks share the same required-file, `CNAME`, placeholder, internal-link, external-link-safety, and public wording guardrails.
- Added small SEO/social metadata and critical CSS color fallbacks.
- Improved navigation state with `aria-current="location"` and added a print-popup fallback message.
- Updated `research/source-log.md` and `research/open-questions.md` to log the sprint and mark the fuller crisis/safe-use questions as lowered.

Checks run in this sprint:

- `git pull --ff-only origin main`
- `git status --short --branch`
- `python3 scripts/check-site.py`
- `git diff --check`
- `cat CNAME`
- `wkhtmltoimage` desktop and mobile render smoke checks to `/private/tmp`
- `sips` image dimension checks for rendered desktop/mobile images
- `wkhtmltopdf --print-media-type` print smoke check to `/private/tmp`
- `qpdf --check /private/tmp/careleaver-print.pdf`
- `pdftotext /private/tmp/careleaver-print.pdf -`

Browser note: the Playwright CLI wrapper hung before output and no local Playwright package was available, so this sprint used static checks plus wkhtml image/PDF smoke checks rather than a modern Chromium interaction test.

## What Was Added In The External Link Check Pass

- Extended `scripts/check-site.py` with `--external`, `--soft-external`, and `--external-timeout`.
- The default local and push checks remain stable and offline-friendly.
- Strict external HTTP checks can now run locally or from manual GitHub Actions dispatch.
- Scheduled GitHub Actions runs now perform external link checks as soft warnings, so temporary upstream outages do not block ordinary pushes.
- Updated `ROADMAP.md` and `research/open-questions.md` to mark the minimal automated link-checking question as lowered.
- No public factual content or source-sensitive wording changed.

Checks run in this pass:

- `git pull --ff-only origin main`
- `git status --short --branch`
- `python3 scripts/check-site.py`
- `python3 scripts/check-site.py --external`
- `git diff --check`
- `cat CNAME`
- YAML parse check for `.github/workflows/site-check.yml`
- local HTTP preview smoke check at `http://127.0.0.1:8765/` returned `HTTP 200`

## What Was Added In The No-JavaScript / Print Pass

- Added an explicit no-JavaScript fallback for the `Nächste-Schritte-Finder`, so users can still jump directly to the right section if scripts are disabled.
- Hid interactive buttons when JavaScript is unavailable, avoiding controls that look clickable but cannot run.
- Fixed the section print helper so typed input and textarea values are copied into the print window before printing.
- Improved print styling for template form fields.
- No public factual claims, contact details, benefit amounts, deadlines, or eligibility wording changed.

Checks run in this pass:

- `git pull --ff-only origin main`
- `git status --short --branch`
- `python3 scripts/check-site.py`
- `git diff --check`
- `cat CNAME`
- inline JavaScript syntax check with `node`
- `wkhtmltoimage --disable-javascript --width 390 index.html /private/tmp/careleaver-nojs-mobile.png`
- `sips` image dimension check for the no-JavaScript mobile render
- `wkhtmltopdf --disable-javascript --print-media-type index.html /private/tmp/careleaver-nojs-print.pdf`
- `qpdf --check /private/tmp/careleaver-nojs-print.pdf`
- `pdftotext /private/tmp/careleaver-nojs-print.pdf -` smoke check for no-JavaScript fallback text

## What Was Added In The Public Source Review Page Pass

- Added `quellen.html` as a public source/review and short changelog page.
- Linked the new page from the homepage navigation, source section, footer, and `sitemap.xml`.
- Updated `scripts/check-site.py` so same-domain `careleaver.eu` URLs are checked against local files instead of treated as third-party external links before deployment.
- Updated `ROADMAP.md`, `research/source-log.md`, and `research/open-questions.md` to record that a public source/changelog page now exists.
- No new service details, benefit amounts, legal deadlines, eligibility promises, copied contact directory, backend, analytics, or forms were added.

Checks run in this pass:

- `git pull --ff-only origin main`
- `git status --short --branch`
- `python3 scripts/check-site.py`
- `python3 scripts/check-site.py --external`
- `git diff --check`
- `cat CNAME`
- inline JavaScript syntax check with `node --check`
- `wkhtmltoimage --width 390 quellen.html /private/tmp/careleaver-quellen-mobile.png`
- `sips` image dimension check for the new page mobile render
- `wkhtmltopdf --print-media-type quellen.html /private/tmp/careleaver-quellen.pdf`
- `qpdf --check /private/tmp/careleaver-quellen.pdf`
- local HTTP preview smoke checks for `/` and `/quellen.html`, both returning `HTTP 200`

## What Was Added In The Accessibility Check Pass

- Extended `scripts/check-site.py` with static accessibility guardrails for all root HTML pages.
- The checker now catches missing or wrong language attributes, missing `main`/skip-link structure, missing or duplicate H1 structure, heading-level jumps, broken ARIA references, unlabelled form controls, unnamed links/buttons, images without `alt`, table headers without `scope`, and unlabelled navigation landmarks.
- Updated `ROADMAP.md`, `research/qa-report.md`, and `research/open-questions.md` to record that a lightweight accessibility QA path now exists.
- No public factual claims, contact details, benefit amounts, legal deadlines, eligibility wording, backend, analytics, or forms were changed.

Checks run in this pass:

- `git pull --ff-only origin main`
- `git status --short --branch`
- `python3 scripts/check-site.py`
- `python3 -m py_compile scripts/check-site.py`
- `git diff --check`
- `cat CNAME`
- `python3 scripts/check-site.py --external`
- inline JavaScript syntax check with `node --check`
- local HTTP preview smoke checks for `/` and `/quellen.html`, both returned `HTTP 200`

## What Was Added In The Source Review Automation Pass

- Extended `scripts/check-site.py` with source-review due-date checks.
- The checker now parses public "Nächste Prüfung" dates in HTML notes and review tables, plus `Review by` dates in `research/source-log.md`.
- The default check warns when a source review is due soon and fails strict checks once a review date is overdue.
- Added `--today`, `--review-warning-days`, `--soft-review-dates`, and `--report-review-dates` options for local testing and reporting.
- Updated `ROADMAP.md`, `research/qa-report.md`, and `research/open-questions.md` so future runs know this guardrail exists.
- No public factual claims, contact details, benefit amounts, legal deadlines, eligibility wording, backend, analytics, or forms were changed.

Checks run in this pass:

- `git pull --ff-only origin main`
- `git status --short --branch`
- `python3 scripts/check-site.py --today 2026-04-29 --report-review-dates`
- `python3 scripts/check-site.py --today 2026-07-30 --soft-review-dates --review-warning-days 0`
- `python3 scripts/check-site.py --today 2026-07-30 --review-warning-days 0` failed as expected on overdue source reviews
- `python3 -m py_compile scripts/check-site.py`
- `python3 scripts/check-site.py`
- `python3 scripts/check-site.py --external`
- `git diff --check`
- `cat CNAME`
- local bounded HTTP preview for `/` and `/quellen.html`, both returned `HTTP 200`

## What Was Added In The Homepage Quick-Action Pass

- Added a short "Heute ein kleiner nächster Schritt" block in the top "Was brauchst du gerade?" area.
- The new block gives three safe, practical actions: urgent help first, prepare one appointment, and sort unclear letters without guessing legal deadlines.
- Extended `scripts/check-site.py` so the quick-action block is part of the public homepage guardrails.
- No new phone numbers, contact details, benefit amounts, legal deadlines, eligibility promises, backend, analytics, or forms were added.

Checks run in this pass:

- `git pull --ff-only origin main`
- `git status --short --branch`
- `python3 scripts/check-site.py`
- `python3 -m py_compile scripts/check-site.py`
- `git diff --check`
- `cat CNAME`
- `python3 scripts/check-site.py --external`
- inline JavaScript syntax check with `node --check`
- `wkhtmltoimage --width 390 index.html /private/tmp/careleaver-quick-actions-mobile.png`
- `sips` image dimension check for the mobile render
- `wkhtmltopdf --print-media-type index.html /private/tmp/careleaver-quick-actions-print.pdf`
- `qpdf --check /private/tmp/careleaver-quick-actions-print.pdf`
- local HTTP preview smoke check for `/` returned `HTTP 200` on port 8791 after ports 8765 and 8766 were already occupied

## What Was Added In The Structured-Data SEO Pass

- Expanded homepage JSON-LD from a single WebSite node to a safe WebSite/WebPage graph.
- Added WebSite/WebPage/BreadcrumbList JSON-LD to `quellen.html`.
- Extended `scripts/check-site.py` so JSON-LD is parsed, required schema types are checked, and risky organization/person/contact/publisher/provider schema is blocked until owner details are settled.
- Updated `ROADMAP.md` and `research/open-questions.md` to record that the safe Schema.org metadata question is lowered.
- No public factual advice, service details, phone numbers, benefit amounts, legal deadlines, eligibility wording, backend, analytics, or forms were changed.

Checks run in this pass:

- `git pull --ff-only origin main`
- `git status --short --branch`
- `python3 scripts/check-site.py --today 2026-04-29 --report-review-dates`
- `python3 -m py_compile scripts/check-site.py`
- `git diff --check`
- `cat CNAME`
- `python3 scripts/check-site.py --today 2026-04-29 --external`
- inline JavaScript syntax check with `node --check`
- local bounded HTTP preview for `/` and `/quellen.html`, both returned `HTTP 200`

## What Was Added In The Sitemap / Canonical Check Pass

- Extended `scripts/check-site.py` with sitemap/canonical/robots consistency checks.
- The checker now verifies that each root HTML page has exactly one expected canonical URL, each canonical public page is listed in `sitemap.xml`, sitemap URLs map back to local root HTML files, sitemap `lastmod` values parse as dates, and `robots.txt` points to `https://careleaver.eu/sitemap.xml`.
- Updated `ROADMAP.md` and `research/qa-report.md` to record the new maintenance guardrail.
- No public factual claims, contact details, benefit amounts, legal deadlines, eligibility wording, backend, analytics, or forms were changed.

Checks run in this pass:

- `git pull --ff-only origin main`
- `git status --short --branch`
- `python3 scripts/check-site.py --today 2026-04-29 --report-review-dates`
- `python3 -m py_compile scripts/check-site.py`
- `git diff --check`
- `cat CNAME`
- `python3 scripts/check-site.py --today 2026-04-29 --external --external-timeout 30`
- local HTTP preview for `/` and `/quellen.html`, both returned `HTTP 200` on port 8792

## Current Product Decision

The best MVP direction is a Wien-first, source-dated "Was mache ich als Naechstes?" guide for Care Leavers after child/youth welfare.

The site should help young people and helpers prepare for real service routes:

- crisis and safety help
- MA 11 / Wien Care Leaver counselling
- housing and first-flat next steps
- money, U25, AMS, benefits, and debt questions
- health and mental-health routing
- documents and appointment prep
- rights, complaints, and trusted-person scripts

The site should not become a legal encyclopedia, benefit calculator, chatbot, backend service, advocacy organization, or broad stale contact database.

## Known Risks / Things To Review

- The public page is safer and source-linked, and a focused Codex QA pass is complete. A human factual review is still recommended before broad outreach because crisis, housing, benefits, and child/youth welfare routing are high-stakes.
- Verified operator/contact/impressum details still need a user decision before being published.
- Bundesland content outside Wien is intentionally incomplete/beta.
- `careleaver.eu` may be confused with Care Leaver Oesterreich / `careleaver.at`. Add non-affiliation wording unless collaboration is agreed.
- The public page includes non-affiliation wording, but outreach wording should still be reviewed before contacting Care Leaver Oesterreich or partners.
- The public page links to OBS for ORF-related exemption/support checks and the exact City of Vienna residence-registration page.
- The old waff 18-25 wording was removed; current page links to waff and warns to verify waff age ranges directly there.
- localStorage still exists for checklist state and opt-in template drafts; shared-device risk is disclosed and deletion is available.
- Public review dates are present, and the local/CI checker now flags overdue review dates, but crisis, money, housing, and contact routes still must actually be reviewed again by 2026-07-29.

## Next Recommended Action

Use the "Next 3 Recommended Tasks" in the 2026-04-29 morning review section as the current priority order:

1. Real browser/mobile accessibility pass for `index.html` and `quellen.html`.
2. Human factual review of the Wien MVP against `research/source-log.md` and `research/qa-report.md`.
3. Verified operator/contact/impressum decision and careful publication.

## Safe Editing Rule For The Next Step

Do not make factual wording stronger until the source log supports it. It is better to say "please verify with the official service" than to give a confident but unsupported answer.

Operator/contact/impressum details and human factual review before broad outreach remain unresolved owner-level decisions.
