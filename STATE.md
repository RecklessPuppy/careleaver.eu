# State

Last updated: 2026-04-29

## Current Status

- Repo is cloned locally at `/Users/hardwork/Developer/Codex/workspaces/careleaver.eu`.
- Current branch: `main`.
- Remote: `origin` points to `https://github.com/RecklessPuppy/careleaver.eu.git`.
- Site is a static GitHub Pages site.
- Public live site: `https://careleaver.eu`.
- Custom domain is preserved through `CNAME`, which contains `careleaver.eu`.
- Current public site is one static page: `index.html`, plus `robots.txt` and `sitemap.xml`.
- The site is German-language and now explicitly Wien-first.
- The site includes source-sensitive material: emergency numbers, Wien routes, rights/background, deadlines, benefit/housing notes, and health/crisis routes.
- A research swarm was completed on 2026-04-29 to decide the product direction before public content changes.
- A content architecture pass was completed on 2026-04-29 to turn the research into reviewable page/template drafts.
- A public Wien-first MVP pass was completed on 2026-04-29.
- A focused safety/fact/link/mobile QA pass was completed on 2026-04-29 and logged in `research/qa-report.md`.
- An overnight autonomous operating setup was added on 2026-04-29, including runbook, prompts, report folder, and lightweight GitHub Actions checks.

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
- Removed old public placeholder contact/impressum fields; public footer now says verified operator/contact details still need to be added before broad outreach.
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
- Public review dates are present, but crisis, money, housing, and contact routes must be reviewed again by 2026-07-29.

## Next Recommended Action

Run `prompts/06-overnight-operator.md` in Codex Automations every 90 minutes overnight, then run `prompts/07-morning-review.md` after waking.

Recommended first task for the next Codex chat:

> Read `AGENTS.md`, `PROJECT_BRIEF.md`, `STATE.md`, `ROADMAP.md`, `OPERATING_MODEL.md`, `OVERNIGHT_RUNBOOK.md`, `SOURCE_POLICY.md`, `CONTENT_SAFETY.md`, `research/qa-report.md`, `research/source-log.md`, `research/open-questions.md`, and `index.html`. Pull latest `main`, choose the highest-impact safe task that does not need missing owner facts, implement it, run checks, write a dated automation report, update `STATE.md`, commit, and push. Do not expand Bundeslaender yet.

## Safe Editing Rule For The Next Step

Do not make factual wording stronger until the source log supports it. It is better to say "please verify with the official service" than to give a confident but unsupported answer.

Operator/contact/impressum details and human factual review before broad outreach remain unresolved owner-level decisions.
