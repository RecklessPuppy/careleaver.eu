# Prompt 07: Morning Review

Use this prompt after an overnight automation run.

```text
We are working on /Users/hardwork/Developer/careleaver.eu.

Mode: morning owner review. Do not make code/content changes unless needed to produce the review. The goal is to summarize what happened overnight and what needs human attention.

Start:
1. Run git pull --ff-only origin main.
2. Run git status --short --branch.
3. Read:
   - AGENTS.md
   - PROJECT_BRIEF.md
   - STATE.md
   - ROADMAP.md
   - OPERATING_MODEL.md
   - OVERNIGHT_RUNBOOK.md
   - research/automation-reports/
   - research/qa-report.md
   - research/open-questions.md
4. Inspect recent commits on main since the last owner review or since yesterday evening.
5. If GitHub Actions exists, check whether the latest site-check workflow passed if practical.

Return a human-readable morning brief with:
- commits made overnight, newest first
- files changed and why they matter
- whether public factual/legal/health/housing/emergency/contact content changed
- any high-risk claims that need human review
- any checks that failed or were not run
- any unresolved blockers from research/open-questions.md
- whether CNAME still preserves careleaver.eu
- the single safest next task for today

Keep the review short enough to read with coffee, but include exact file paths and commit hashes.

Do not invent missing facts. If operator/contact/impressum details are still missing, say that they still require the owner.
```
