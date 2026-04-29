# AGENTS.md

Last updated: 2026-04-29

This file is the first stop for any future Codex chat or automation working on `careleaver.eu`.

## Project In One Sentence

`careleaver.eu` is a practical Austrian Care Leaver resource website for young people leaving child/youth welfare, starting with a Wien-first MVP and expanding carefully across Austria.

## Working Style For This Repo

- Treat the user as a capable beginner: explain important choices in plain language, but keep moving.
- Work directly on `main` and push frequently unless the user asks for a branch.
- Keep changes small and reviewable. This site is low-stakes for design/code iteration, but high-stakes for factual claims.
- Before editing, inspect the current file shape and Git status. Do not assume a framework exists.
- Prefer simple static HTML/CSS/JS. Add build tools, dependencies, databases, forms, or servers only when there is a strong practical reason.
- Preserve the custom domain. The `CNAME` file must keep `careleaver.eu` unless the user explicitly decides otherwise.

## Overnight Autonomous Mode

Use this mode when the user asks for overnight, autonomous, aggressive, or low-involvement progress.

- Start by running `git pull --ff-only origin main`, then inspect `git status --short --branch`.
- Read `STATE.md` first after pulling, then read the project safety files listed below.
- Choose the highest-impact safe task from `STATE.md`, `ROADMAP.md`, `research/qa-report.md`, and `research/open-questions.md`.
- Implement aggressively within safe boundaries: finish one useful improvement instead of only planning it.
- Prefer safe progress: UX, accessibility, SEO metadata, static structure, templates, source-display improvements, link checks, internal anchors, documentation, and automation.
- Factual/legal/health/housing/emergency/contact changes are allowed only when source-linked, dated, and logged according to `SOURCE_POLICY.md`.
- Never invent legal rights, eligibility, benefit amounts, deadlines, phone numbers, addresses, opening hours, emergency routes, or contact details.
- Do not expand non-Wien Bundesland content beyond "in progress" without a fresh official source set.
- Run checks before committing. At minimum verify `CNAME`, important files, obvious placeholders, and internal links; run browser/mobile/print checks when public layout changes.
- Commit each useful pass with a short clear message and push directly to `origin main`.
- Write a dated report in `research/automation-reports/` for each autonomous pass.
- Update `STATE.md` with what changed, what checks ran, and the next recommended task.
- Do not delete or change `CNAME`.
- Do not add secrets, analytics, tracking pixels, third-party forms, backend services, or personal-data collection without an explicit user decision.
- If blocked by missing human facts, do not guess. Log the blocker in `research/open-questions.md` and pick the next safe task.

## Current Technical Shape

- Static GitHub Pages site.
- Public site: `https://careleaver.eu`
- GitHub repo: `https://github.com/RecklessPuppy/careleaver.eu`
- Current core files:
  - `index.html` - the public website.
  - `CNAME` - GitHub Pages custom domain.
- No package manager, build step, or framework is currently required.

## Content Language And Scope

- Use German for public site content unless the user says otherwise.
- Default scope: Austria-first, Wien-first.
- Wien should be the first complete MVP because the current site already contains many Wien-specific contacts and support paths.
- Expand to other Bundeslaender only after source checking. If a Bundesland is not researched yet, say it is in progress instead of guessing.

## Safety Rules For Factual Content

This site may guide vulnerable young people leaving child/youth welfare. Design and code can change quickly, but factual content must be handled carefully.

- Source-link and date claims about:
  - legal rights and laws
  - child/youth welfare processes
  - benefits, money, fees, deadlines, eligibility, and application steps
  - emergency, crisis, health, housing, and counselling services
  - phone numbers, addresses, opening hours, forms, and contact pages
- Do not invent contact details, addresses, opening hours, legal thresholds, benefit amounts, or deadlines.
- If a detail is uncertain, mark it as needing verification and add it to `research/open-questions.md`.
- If a source is old, unclear, or unofficial, do not state the claim with certainty.
- Never present the site as legal advice, medical advice, therapy, or a guaranteed entitlement decision.
- For urgent danger or crisis content, prioritize official emergency numbers and official service pages.

Use `SOURCE_POLICY.md` and `CONTENT_SAFETY.md` before editing factual content.

## Research And Source Logging

- Log factual sources in `research/source-log.md`.
- Keep research synthesis in `research/research-synthesis.md`.
- Keep unresolved questions in `research/open-questions.md`.
- For each important claim, capture:
  - source title
  - URL
  - publisher/owner
  - date accessed
  - what claim it supports
  - freshness/review note

## No Secrets

- Do not commit API keys, passwords, private tokens, private email inbox data, private notes, or unpublished personal information.
- Do not add tracking pixels, analytics, third-party forms, or data collection without an explicit user decision.
- The current static site should avoid collecting personal data. Browser-only local storage is acceptable when clearly disclosed.

## Design And Build Defaults

- Do not do a big redesign unless the user asks for it.
- Prefer accessible, mobile-friendly, print-friendly patterns.
- Keep pages useful on a phone and printable for appointments.
- Avoid decorative complexity that makes urgent information harder to find.
- Test obvious workflows after editing:
  - page loads
  - mobile layout is readable
  - print/PDF behavior still works if touched
  - links changed in the edit open correctly

## Git Defaults

- Work directly on `main`.
- Before committing:
  - run `git status --short --branch`
  - review the diff
  - ensure `CNAME` still says `careleaver.eu`
- Commit messages should be short and clear, for example:
  - `Add project operating docs`
  - `Update Wien source log`
  - `Fix print styles`
- Push to `origin main` after each useful commit unless the user says not to.

## Files To Read First In New Chats

1. `AGENTS.md`
2. `PROJECT_BRIEF.md`
3. `STATE.md`
4. `SOURCE_POLICY.md`
5. `CONTENT_SAFETY.md`
6. `ROADMAP.md`
7. `OPERATING_MODEL.md`
8. `OVERNIGHT_RUNBOOK.md` when running unattended or overnight work

Then inspect `index.html`, `research/source-log.md`, and `research/open-questions.md` before changing public content.
