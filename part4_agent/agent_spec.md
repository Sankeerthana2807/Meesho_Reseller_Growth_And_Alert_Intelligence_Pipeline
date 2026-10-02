# Agent Specification — Meesho Reseller Growth Monitoring

## Goal
Keep Meesho category managers informed of any category whose month-on-month revenue moves beyond the 8% threshold, with a human approving every message before it goes out.

## Tools
- `validate_feed` (Part 2) — ensures input CSV is valid before processing.
- `mom_growth` (Part 2) — computes MoM growth percentage.
- `is_flagged` (Part 2) — determines flagged/not_flagged/escalate boundary.
- Prompt-pack template (Part 3) — drafts stakeholder-ready narratives.

## Memory / State
- Stores previous month’s revenue per category to compute MoM growth.
- Tracks flagged categories across runs for trend analysis.

## Planner (Ordered Subtasks)
1. Load the monthly revenue feed and run `validate_feed`.
2. If invalid → Hard Stop, report errors.
3. If valid → compute `mom_growth` for each category vs previous month.
4. Run `is_flagged` for each category.
5. Sort flagged categories by absolute MoM percentage descending.
6. Draft messages (via prompt-pack) for top 3 flagged categories only.
7. Log remaining flagged categories as “suppressed, review manually.”
7b. Log exact-boundary cases separately in `escalated_categories`.
8. Emit structured JSON output.

## Feedback Loop
Every drafted message is held for human approval before sending. No auto-send.

## Guardrails
- **Input:** Must pass `validate_feed` before proceeding.
- **Action:** No message is auto-sent; only drafted and held.
- **Output:** Every number in a draft must trace back to Part 1/Part 2 values.

## Success & Error Conditions
- **Success:** Drafts produced (or zero drafts if nothing flagged), all numbers traceable.
- **Error:** `validate_feed` returns False → Hard Stop, errors surfaced.

## Given-When-Then Specs
- GIVEN April→May Ethnic Wear revenue moves from 104520.77 to 185107.61, WHEN processed, THEN MoM growth = 77.1% and flagged narrative drafted.
- GIVEN May→June Beauty & Personal Care revenue moves from 35542.11 to 37559.07, WHEN processed, THEN MoM growth = 5.67% and not flagged.
- GIVEN synthetic case previous=100000, current=108000, WHEN processed, THEN MoM growth = 8.0% and escalated boundary logged.
- GIVEN corrupted feed, WHEN processed, THEN validation fails and run halts with 3 errors surfaced.
