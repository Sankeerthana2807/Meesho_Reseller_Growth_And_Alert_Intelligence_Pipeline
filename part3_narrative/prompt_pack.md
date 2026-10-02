# Prompt Pack — Flagged Category Narrative

## Trigger
A category’s `is_flagged` result is `"flagged"`.

## Input List
- {category}
- {previous_revenue}
- {current_revenue}
- {mom_pct}
- {month}
- {prev_month}

## Prompt
"Context: We are reviewing {category} performance for {month} vs {prev_month}.  
Insight: Revenue moved from {previous_revenue} to {current_revenue}, a {mom_pct}% change.  
Implication: Based on this flagged movement, the recommendation is to investigate drivers of this change — e.g., pricing, promotions, or reseller activity — and take corrective or scaling action accordingly."

## Checklist
- Every number in the draft matches a supplied placeholder exactly.  
- Every claim is labeled explicitly as **fact** (numbers) or **hypothesis** (causes).  
- The recommendation is specific and actionable (e.g., check pricing strategy, review reseller activity).  
- No raw reseller names appear; only aliases or categories are referenced.  
