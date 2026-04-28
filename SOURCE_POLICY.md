# Source Policy

Last updated: 2026-04-29

This policy applies to factual public content on `careleaver.eu`.

## Why This Matters

The website may be used by vulnerable young people leaving child/youth welfare. Wrong or stale information about housing, money, crisis support, benefits, or legal rights can cause real harm. The site should be helpful, but it must not pretend to be more certain than its sources.

## Claims That Need Sources

Always source-link and date claims about:

- laws, rights, eligibility, appeals, deadlines, or official processes
- benefits, allowances, fees, reductions, contribution amounts, and income thresholds
- child/youth welfare services and aftercare
- housing, emergency accommodation, Wohnbeihilfe, Gemeindewohnung, Wohnticket, or similar routes
- emergency, crisis, medical, psychological, counselling, and violence protection services
- phone numbers, email addresses, physical addresses, opening hours, forms, and appointment routes
- age ranges, time limits, and "you can/cannot" statements

## Preferred Sources

Use the most official and current source available.

Preferred order:

1. Official Austrian federal, city, or Bundesland pages.
2. Official service provider pages for the exact organization named.
3. Statutory text or official legal information systems where appropriate.
4. Recognized public-interest organizations with clear ownership and current pages.
5. Secondary explainers only as backup context, not as the main source for legal/benefit claims.

Avoid relying on:

- old PDFs without clear date
- unsourced blog posts
- copied phone numbers from directories if an official page exists
- AI-generated summaries as sources
- memory from prior Codex chats

## Source Log Format

Put sources in `research/source-log.md` using this format:

```md
## Source Title

- URL:
- Publisher / owner:
- Date accessed:
- Page date / last update if visible:
- Supports these claims:
- Freshness risk: low / medium / high
- Review by:
- Notes:
```

## Claim Wording Rules

- Say "may", "can", or "check whether" when eligibility depends on individual facts.
- Say "according to [source]" when the claim is legal, financial, or procedural.
- Include the information date where time matters.
- Use clear calls to verify current details before relying on phone numbers, fees, deadlines, or office hours.
- Do not write "you are entitled to X" unless the legal/source basis is clear and conditions are explained.

## Review Dates

Use conservative review intervals:

- emergency and crisis contacts: every 3 months
- benefits, fees, thresholds, deadlines: every 3 months
- legal process summaries: every 6 months or after known law changes
- general explanatory content: every 12 months
- broken links: whenever found, ideally monthly once automation exists

## What To Do When A Source Is Missing

If a claim seems useful but is not sourced:

1. Do not strengthen it.
2. Add it to `research/open-questions.md`.
3. Use softer wording or remove it from public content until verified.
4. Prefer linking users to official services rather than guessing.

## Contact Information Rule

Never invent contact details. If official contact information cannot be verified:

- do not publish it as fact
- link to the official contact page instead
- add the missing detail to `research/open-questions.md`

## Audit Trail

When factual public content changes, update:

- `research/source-log.md`
- `research/research-synthesis.md` if the change affects the content model
- `STATE.md` if it changes the current project status or next action
