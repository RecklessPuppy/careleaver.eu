# Overnight Runbook

Last updated: 2026-04-29

Use this when Codex is allowed to keep improving `careleaver.eu` while the owner is away.

## Operating Goal

Make as much useful progress as possible without creating factual risk.

Safe progress means:

- the site remains static and deployable on GitHub Pages
- `CNAME` still contains `careleaver.eu`
- public facts are source-linked and cautious
- changes are committed and pushed to `main`
- each autonomous run leaves a clear report for the owner

## Start Of Every Run

1. Run `git pull --ff-only origin main`.
2. Run `git status --short --branch`.
3. Read:
   - `STATE.md`
   - `AGENTS.md`
   - `PROJECT_BRIEF.md`
   - `ROADMAP.md`
   - `OPERATING_MODEL.md`
   - `SOURCE_POLICY.md`
   - `CONTENT_SAFETY.md`
   - `research/qa-report.md`
   - `research/open-questions.md`
   - `research/source-log.md`
4. Inspect the files likely to change.
5. Pick one highest-impact safe task.

## Task Priority Ladder

Prefer tasks in this order unless `STATE.md` says otherwise:

1. Fix anything that can break deployment, navigation, `CNAME`, internal links, or the main user flow.
2. Improve safety around high-risk content without inventing facts: source visibility, cautious wording, review dates, and open-question logging.
3. Improve accessibility, mobile usability, print behavior, and no-JavaScript resilience.
4. Improve SEO basics and discoverability without implying false coverage or partnerships.
5. Improve practical templates and appointment preparation using already sourced, cautious language.
6. Add or improve maintenance automation, check scripts, and review prompts.
7. Draft future content in `content/` or `research/` without publishing unsourced claims.

## Safe Autonomous Work

These are usually safe without waking the owner:

- fixing broken internal anchors
- improving semantic HTML, headings, labels, focus states, and print styles
- adding source/review-date displays for already logged sources
- softening unsupported wording
- moving uncertain claims to `research/open-questions.md`
- adding docs, prompts, runbooks, reports, and lightweight CI
- checking links and logging failures
- adding static templates that do not promise legal or benefit outcomes
- improving `robots.txt`, `sitemap.xml`, titles, descriptions, and social metadata carefully

## Human-Decision Work

Do not guess these. Log a blocker and choose another task:

- operator, impressum, owner, or public contact details
- new phone numbers, addresses, opening hours, or direct service contacts
- legal rights, appeal periods, deadlines, eligibility, benefit amounts, or thresholds
- non-Wien Bundesland pages without fresh official sources
- affiliation, partnership, endorsement, or outreach wording
- analytics, tracking, forms, backend services, or data collection
- domain or `CNAME` changes

## Factual Content Rules

Before publishing factual content, confirm:

- the source is official or clearly trustworthy
- the URL is logged in `research/source-log.md`
- the public text is cautious and does not promise outcomes
- a review date is visible or documented
- uncertain details are in `research/open-questions.md`

If the source is not fresh enough, link users to the official page instead of copying details.

## One Autonomous Cycle

1. Pull latest `main`.
2. Choose one task from the priority ladder.
3. Make the change.
4. Run checks:
   - `git status --short --branch`
   - `git diff --check`
   - verify `CNAME` contains exactly `careleaver.eu`
   - run `.github/workflows/site-check.yml` logic locally when practical
   - run browser/mobile/print checks when public UI changes
5. Review the diff.
6. Update `STATE.md`.
7. Write a dated report in `research/automation-reports/`.
8. Commit with a short message.
9. Push to `origin main`.
10. Final response should mention commit hash, checks, and next safe task.

## Report Format

Use this filename pattern:

`research/automation-reports/YYYY-MM-DD-short-title.md`

Use this structure:

```md
# Automation Report: Short Title

Date: YYYY-MM-DD
Mode: overnight autonomous

## Summary

- What changed.
- Why it was safe and useful.

## Files Changed

- `path`

## Checks

- Check name: pass/fail/not run.

## Factual Safety

- Public factual content touched: yes/no.
- Source log updated: yes/no/not needed.
- Open questions added: yes/no/not needed.

## Next Recommended Task

- One concrete next task.
```

## Recommended Cadence

For unattended overnight progress, run `prompts/06-overnight-operator.md` every 90 minutes from 22:30 to 07:30 Europe/Vienna.

This gives enough time for one meaningful static-site pass per cycle while avoiding tiny noisy commits.

Use `prompts/07-morning-review.md` once after waking, ideally around 08:00 Europe/Vienna.

## Stop Conditions

Stop autonomous work if:

- `git pull --ff-only` fails because of divergence
- GitHub push authentication fails
- a required file is missing in a way that makes the repo unsafe to edit
- the next useful task requires private owner facts
- checks show a public high-risk factual regression that cannot be fixed confidently

When stopping, write a report explaining the blocker if the worktree can be safely committed. If not, leave the worktree as clear as possible and explain the exact state.
