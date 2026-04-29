# State

Last updated: 2026-04-29

## Current Status

- Repo is cloned locally at `/Users/hardwork/Developer/Codex/workspaces/careleaver.eu`.
- Current branch: `main`.
- Remote: `origin` points to `https://github.com/RecklessPuppy/careleaver.eu.git`.
- Site is a static GitHub Pages site.
- Public live site: `https://careleaver.eu`.
- Custom domain is preserved through `CNAME`, which contains `careleaver.eu`.
- Current public site is mainly one file: `index.html`.
- The site is German-language and already Austria/Wien-focused.
- The site includes source-sensitive material: emergency numbers, Wien contacts, rights, deadlines, benefit/housing notes, and health/crisis routes.
- A research swarm was completed on 2026-04-29 to decide the product direction before public content changes.
- A content architecture pass was completed on 2026-04-29 to turn the research into reviewable page/template drafts.
- The public site was not changed in the research-swarm or content-architecture passes.

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

- The existing public page contains many factual/contact claims that should be audited source-by-source before major outreach.
- The public page currently has placeholder contact fields in the legal/accessibility area, such as placeholder email/phone text. These should be resolved before wider publication.
- The header says information status is November 2025. Time-sensitive claims should be reviewed and updated before the site is treated as current.
- Bundesland content outside Wien is currently incomplete/beta.
- The current "Anspruchs-Check" wording can sound like a legal/benefit decision tool. Rename and soften before wider use.
- `careleaver.eu` may be confused with Care Leaver Oesterreich / `careleaver.at`. Add non-affiliation wording unless collaboration is agreed.
- The current ORF link should likely point to OBS for exemption claims.
- The current Meldezettel link should likely point to the exact City of Vienna residence-registration page.
- The waff age range in the current page may be wrong or stale; source research suggests rechecking `18-25` against current `18-24` wording.
- localStorage may preserve sensitive appointment details on shared devices. Improve warning or storage behavior if tools are edited.

## Next Recommended Action

Run Phase 1B: Wien safety and source audit, using the new `content/` drafts as the content direction.

Recommended first task for the next Codex chat:

> Read `AGENTS.md`, `PROJECT_BRIEF.md`, `SOURCE_POLICY.md`, `CONTENT_SAFETY.md`, `STATE.md`, `ROADMAP.md`, `content/architecture.md`, `content/page-drafts/home.md`, `content/page-drafts/wien.md`, `content/templates/appointment-prep.md`, `content/templates/email-jugendhilfe.md`, `research/research-synthesis.md`, `research/source-log.md`, `research/open-questions.md`, and `index.html`. Make a small Wien MVP safety pass: add a top "Schnelle Hilfe in Wien" / "Ich brauche Hilfe mit ..." router, rename "Anspruchs-Check" to a safer next-steps/prep tool, add visible source/last-checked notes for the highest-risk sections, replace weak ORF/Meldezettel links, and soften any unsupported entitlement wording. Do not expand Bundeslaender yet.

## Safe Editing Rule For The Next Step

Do not make factual wording stronger until the source log supports it. It is better to say "please verify with the official service" than to give a confident but unsupported answer.
