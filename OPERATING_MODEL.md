# Operating Model

Last updated: 2026-04-29

This is the practical way to run the project.

## Default Workflow

1. Pull first with `git pull --ff-only origin main`.
2. Read `STATE.md`, then `AGENTS.md`, `PROJECT_BRIEF.md`, `ROADMAP.md`, `SOURCE_POLICY.md`, and `CONTENT_SAFETY.md`.
3. Check Git status and confirm the branch is `main`.
4. Inspect the files that will be changed.
5. Make a focused, useful change.
6. Review the diff.
7. Run the most relevant checks.
8. Commit with a clear message.
9. Push to `origin main`.
10. Update `STATE.md` if the project status or next action changed.

## Recommended Work Types

### Research Pass

Use when source-sensitive content needs checking.

- Build a claim list.
- Find official sources.
- Update `research/source-log.md`.
- Update `research/open-questions.md`.
- Do not redesign during a research pass unless the user asks.

### Content Pass

Use when turning researched material into public German site text.

- Keep wording practical and calm.
- Put source links near claims.
- Keep the update date visible.
- Avoid making the page longer than necessary.

### Design / Code Pass

Use when improving readability, accessibility, print behavior, or tools.

- Keep the site static by default.
- Do not break the custom domain.
- Test mobile, desktop, and print behavior when relevant.
- Do not change factual claims casually while editing layout.

### Maintenance Pass

Use for link checks, source refreshes, and stale information.

- Check links.
- Review time-sensitive claims.
- Move stale questions into `research/open-questions.md`.
- Update source access dates only after actually checking the source.

### Overnight Autonomous Pass

Use when the owner wants maximum safe progress with minimum involvement.

- Read `OVERNIGHT_RUNBOOK.md` and `prompts/06-overnight-operator.md`.
- Work in one complete cycle: pull, choose task, implement, check, commit, push, report, update state.
- Choose the highest-impact safe task that does not require missing human facts.
- Keep public factual claims cautious. Source and log any factual change before publishing it.
- Prefer improvements that make later work safer: CI checks, source-review scaffolding, accessibility, internal-link fixes, print/mobile improvements, templates, SEO basics, and documentation.
- If a task needs owner facts, record the blocker and move to another safe task.
- Each autonomous pass must write `research/automation-reports/YYYY-MM-DD-short-title.md`.

## Commit And Push Practice

The user prefers working directly on `main` and pushing frequently.

Good commit scope:

- one documentation setup pass
- one source audit pass
- one content section update
- one visual/layout fix

Avoid mixing:

- big redesign plus legal claim edits
- many Bundeslaender at once
- factual rewrites without source-log updates

## What A New Codex Chat Should Say Back

At the start of a new work session, summarize:

- current branch and Git status
- current technical shape
- which file(s) will be changed
- whether the work touches source-sensitive content
- what will be committed and pushed

## Definition Of Done

For documentation-only changes:

- files created or updated
- diff reviewed
- committed and pushed
- Git status clean

For public site changes:

- source-sensitive claims checked if touched
- page still loads
- `CNAME` unchanged
- GitHub Actions or local equivalent checks run when available
- committed and pushed
- Git status clean

For overnight autonomous changes:

- one dated automation report written
- `STATE.md` updated
- `ROADMAP.md` updated if a roadmap phase changed
- pushed to `origin main`
- no unresolved local process left running unless explicitly needed for browser testing
