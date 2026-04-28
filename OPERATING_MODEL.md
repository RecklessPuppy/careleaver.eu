# Operating Model

Last updated: 2026-04-29

This is the practical way to run the project.

## Default Workflow

1. Read `AGENTS.md`, `PROJECT_BRIEF.md`, `STATE.md`, `SOURCE_POLICY.md`, and `CONTENT_SAFETY.md`.
2. Check Git status and confirm the branch is `main`.
3. Inspect the files that will be changed.
4. Make a small, focused change.
5. Review the diff.
6. Run a simple local check if the public page changed.
7. Commit with a clear message.
8. Push to `origin main`.
9. Update `STATE.md` if the project status or next action changed.

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
- committed and pushed
- Git status clean
