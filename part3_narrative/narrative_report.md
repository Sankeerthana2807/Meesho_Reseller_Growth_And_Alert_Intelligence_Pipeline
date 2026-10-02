# Narrative Report

## Worked Narratives

### May — Ethnic Wear (+77.1% MoM growth, flagged)
- **Context:** Ethnic Wear revenue is being tracked between April and May.  
- **Insight (fact):** Revenue increased from INR 104520.77 in April to INR 185107.61 in May, a 77.1% growth.  
- **Implication (hypothesis):** This flagged growth suggests a surge in demand. Regional managers should verify whether promotions or seasonal factors drove this spike, and consider scaling inventory or marketing to sustain momentum.  

### June — Ethnic Wear (-58.74% MoM growth, flagged)
- **Context:** Ethnic Wear revenue is being tracked between May and June.  
- **Insight (fact):** Revenue dropped from INR 185107.61 in May to INR 76371.53 in June, a -58.74% decline.  
- **Implication (hypothesis):** This flagged decline may indicate post-season demand drop or supply chain issues. Regional managers should review stock availability and customer feedback to prevent further losses.  

---

## Self-Scoring Against Checklist
- **Specificity:** Exact category names, months, and percentages are used.  
- **Audience Fit:** Written for regional managers, focusing on actionable insights rather than technical details.  
- **Completeness:** Each narrative includes context, insight, and implication.  
- **Actionability:** Recommendations are concrete (check promotions, review stock, investigate supply chain).  

---

## Chart-Choice Justification

1. **Which month had the highest total revenue?**  
   → Use a **bar chart** (univariate). Clear comparison of April, May, June totals; easy to see May is highest.  

2. **What percentage share does Ethnic Wear represent of April’s total revenue?**  
   → Use a **pie chart** (univariate share). Shows Ethnic Wear’s 24.92% share of April’s revenue clearly.  

3. **How do the four regions compare on total revenue?**  
   → Use a **grouped bar chart** (bivariate). Each region’s revenue side by side makes comparison immediate.  

---

## Masking Policy Test

Example narrative for top resellers:  
"Top reseller in West region is ALIAS-19 with strong performance."  

Validation:  
- `alias_for("RS019") == "ALIAS-19"`  
- `assert_no_raw_names_leak("Top reseller in West region is ALIAS-19 with strong performance.", ["Mumbai Reseller 1", "Mumbai Reseller 4", "Hyderabad Reseller 6", "Lucknow Reseller 6", "Jaipur Reseller 5"]) == True`  
- Negative case: `assert_no_raw_names_leak("Mumbai Reseller 1 had high sales", [...]) == False`  

This confirms raw names are never leaked in external-facing narratives.







