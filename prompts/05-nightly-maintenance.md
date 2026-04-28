# Prompt 05: Nightly Maintenance

Use this prompt for a scheduled maintenance-style check.

```text
We are working on careleaver.eu.

Please run a small maintenance pass.

Read:
- AGENTS.md
- OPERATING_MODEL.md
- SOURCE_POLICY.md
- CONTENT_SAFETY.md
- STATE.md
- research/source-log.md
- research/open-questions.md
- index.html

Tasks:
1. Check git status and branch.
2. Check whether source-sensitive claims are due for review.
3. Check for obvious broken or stale links if practical.
4. Add newly discovered issues to research/open-questions.md.
5. Update STATE.md with the next recommended action if needed.

Do not do a redesign.
Do not update source access dates unless you actually opened and checked the source.
If you make changes, commit and push to main.
```
