# Prompt 06: Overnight Operator

Use this prompt in Codex Automations for unattended overnight progress.

```text
We are working on /Users/hardwork/Developer/Codex/workspaces/careleaver.eu.

Mode: aggressive overnight autonomous progress.

The owner is asleep. Do not ask questions. Do not wait for approval. Work directly on main. Pull before work. Commit and push each useful completed pass.

Project context:
- This is a static GitHub Pages site for careleaver.eu.
- It supports Care Leavers in Austria, currently Wien-first.
- Code, UX, accessibility, SEO, templates, static structure, maintenance automation, and source-linked content can move aggressively.
- Factual/legal/health/housing/emergency/contact information is high-risk. Do not invent it. Do not strengthen it unless official/current sources support it and the source log is updated.

Hard rules:
- Preserve CNAME exactly: careleaver.eu.
- Do not add secrets, tokens, analytics, tracking pixels, third-party forms, backend services, databases, or personal-data collection.
- Do not invent phone numbers, email addresses, physical addresses, opening hours, benefit amounts, eligibility rules, deadlines, legal rights, emergency instructions, or contact details.
- Do not publish non-Wien Bundesland details unless a fresh official source set exists and is logged.
- Do not claim partnership or endorsement by Care Leaver Oesterreich or any organization unless the repo already contains explicit proof.
- If an important fact is uncertain, soften/remove it from public content and add it to research/open-questions.md.

Start:
1. Run git pull --ff-only origin main.
2. Run git status --short --branch.
3. Read these files before choosing work:
   - AGENTS.md
   - PROJECT_BRIEF.md
   - STATE.md
   - ROADMAP.md
   - OPERATING_MODEL.md
   - OVERNIGHT_RUNBOOK.md
   - SOURCE_POLICY.md
   - CONTENT_SAFETY.md
   - research/qa-report.md
   - research/source-log.md
   - research/open-questions.md
4. Inspect the current repo files with rg --files.
5. Inspect any file before editing it.

Choose the highest-impact safe task available. Prefer, in order:
1. Fix deployment or navigation risks.
2. Add or improve automated checks for required files, CNAME, placeholders, and internal links.
3. Improve accessibility, mobile layout, print behavior, semantic HTML, focus states, or no-JavaScript resilience.
4. Improve source visibility, cautious wording, review-date clarity, or open-question logging without inventing facts.
5. Improve practical static templates and appointment-prep content using already sourced cautious language.
6. Improve SEO basics without overclaiming scope, affiliation, or coverage.
7. Improve docs, prompts, runbooks, and maintainability.
8. Draft future researched content in content/ or research/ without publishing unsourced public claims.

Do the work:
- Make a complete, reviewable improvement.
- Keep changes coherent. It is okay to make a larger overnight pass if it is safe, but avoid mixing unrelated high-risk factual edits with design or code refactors.
- If public factual content changes, update research/source-log.md and/or research/open-questions.md in the same commit.
- If public UI changes, check mobile readability and obvious interactions. Use a browser tool if available.
- If no safe public change is available, improve docs, checks, prompts, or source-review scaffolding.

Checks before commit:
- git status --short --branch
- git diff --check
- verify CNAME contains exactly careleaver.eu
- run any available site checks, including the GitHub Actions equivalent if practical
- if index.html changed, check internal anchors and obvious placeholder strings
- if source-sensitive public content changed, verify source links and update source log

Report and state:
- Update STATE.md with:
  - what changed in this autonomous pass
  - checks run
  - current risks
  - next recommended safe task
- Add a dated report under research/automation-reports/ using:
  research/automation-reports/YYYY-MM-DD-short-title.md
- The report must include:
  - summary
  - files changed
  - checks and results
  - whether public factual content changed
  - source-log/open-question updates
  - next recommended task

Git:
- Review the diff before committing.
- Stage only intended files.
- Commit with a short clear message.
- Push directly to origin main.
- After push, run git status --short --branch and note whether the worktree is clean.

If blocked:
- Do not guess.
- Add the blocker to research/open-questions.md if appropriate.
- If there is another safe task, do that instead.
- If no safe task remains, write an automation report explaining the blocker, update STATE.md, commit/push the report if appropriate, and stop.

Final response:
- Give a concise summary.
- Include the commit hash.
- State which checks passed or failed.
- State the next recommended task.
```
