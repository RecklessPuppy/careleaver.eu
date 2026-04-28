# Prompt 04: Factcheck QA

Use this prompt before treating a content update as ready.

```text
We are working on careleaver.eu.

Please do a factcheck QA pass.

Read:
- AGENTS.md
- SOURCE_POLICY.md
- CONTENT_SAFETY.md
- STATE.md
- index.html
- research/source-log.md
- research/open-questions.md

Check:
1. Are high-risk claims source-linked and dated?
2. Are phone numbers, addresses, opening hours, and forms verified from official/current sources?
3. Are benefit amounts, deadlines, age limits, and legal statements cautious enough?
4. Are there invented or placeholder contact details?
5. Is crisis/emergency content clear and not buried?
6. Does the page avoid claiming to provide legal, medical, or therapy advice?

Return:
- high-priority issues first
- exact file/section references
- recommended wording or next action
- whether it is safe to push as-is

If you edit, keep changes small, commit, and push to main.
```
