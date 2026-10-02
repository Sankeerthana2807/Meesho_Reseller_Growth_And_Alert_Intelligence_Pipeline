# Meesho Reseller Growth & Alert Intelligence Pipeline

This repository implements a complete end-to-end pipeline for monitoring reseller growth and generating stakeholder-ready narratives. It is divided into four parts, each feeding into the next.

---

## How to Run Each Part

### Part 1 — SQL Business Query Engine
1. Generate dataset:
   python data/generate_dataset.py

   This creates:
   - data/resellers.csv
   - data/orders.csv
   - data/meesho_reseller.db

2. Run queries:
   - Linux/macOS (bash):
     sqlite3 data/meesho_reseller.db < part1_sql/queries.sql

   - Windows (PowerShell):
     Get-Content part1_sql/queries.sql | sqlite3 data/meesho_reseller.db

   - Or inside sqlite shell:
     .read part1_sql/queries.sql

3. Outputs are saved under part1_sql/output/.

---

### Part 2 — Growth Engine
Implements guardrails and growth detection.

Run tests:
   pytest part2_engine/test_growth_engine.py

Fixtures:
- part2_engine/fixtures/corrupted_feed.csv
- part2_engine/fixtures/monthly_category_revenue.csv

---

### Part 3 — Narrative Layer
Contains:
- prompt_pack.md — reusable narrative template.
- narrative_report.md — worked examples and chart-choice justification.
- masking.py — aliasing and leak-prevention functions.

Run masking test:
   python part3_narrative/masking.py

---

### Part 4 — Agent Runner
Implements agent workflow with validation, flagging, drafting, and JSON output.

Run:
   python part4_agent/mock_agent_runner.py

Outputs structured JSON with keys:
- run_month
- validation_status
- validation_errors
- flagged_categories
- suppressed_categories
- escalated_categories
- action_taken

---

## Zero API Keys
This pipeline runs entirely offline. No API keys or paid services are required.

---

## Workflow Mapping
- Part 1 → Part 2: Mirrors “compute real numbers via SQL first, then hand off to detection engine.”
- Part 2 → Part 3: Mirrors “validated numbers → narrative templates.”
- Part 4: Mirrors “Intake → Summary → Report Draft → Validate → Human Approval.”

---

## References
- Python Standard Library docs (csv, sqlite3, unittest/pytest)
- SQLite official documentation
