import csv
import json
from part2_engine.growth_engine import mom_growth, is_flagged, validate_feed

def draft_message(category, prev_rev, curr_rev, mom_pct, month, prev_month):
    return (
        f"Context: Reviewing {category} performance for {month} vs {prev_month}. "
        f"Insight: Revenue moved from {prev_rev} to {curr_rev}, a {mom_pct}% change. "
        f"Implication: Regional managers should investigate drivers of this flagged change."
    )

def run(month: str, previous_month_csv_path: str, current_month_csv_path: str) -> dict:
    valid, errors = validate_feed(current_month_csv_path)
    if not valid:
        return {
            "run_month": month,
            "validation_status": "invalid",
            "validation_errors": errors,
            "flagged_categories": [],
            "suppressed_categories": [],
            "escalated_categories": [],
            "action_taken": "hard_stop"
        }

    # Load previous and current month revenues
    def load_csv(path):
        data = {}
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data[row["category"]] = float(row["revenue"])
        return data

    prev_data = load_csv(previous_month_csv_path)
    curr_data = load_csv(current_month_csv_path)

    flagged = []
    suppressed = []
    escalated = []

    # Compute MoM growth
    for category, curr_rev in curr_data.items():
        prev_rev = prev_data.get(category, 0.0)
        mom_pct = mom_growth(prev_rev, curr_rev)
        flag_status = is_flagged(mom_pct)

        if flag_status == "flagged":
            flagged.append({
                "category": category,
                "mom_pct": mom_pct,
                "previous_revenue": prev_rev,
                "current_revenue": curr_rev,
                "drafted": False,
                "message": ""
            })
        elif flag_status == "escalate_exact_boundary":
            escalated.append(category)

    # Sort flagged by magnitude
    flagged.sort(key=lambda x: abs(x["mom_pct"]), reverse=True)

    # Draft top 3
    for i, item in enumerate(flagged):
        if i < 3:
            item["drafted"] = True
            item["message"] = draft_message(
                item["category"], item["previous_revenue"], item["current_revenue"],
                item["mom_pct"], month, "previous_month"
            )
        else:
            suppressed.append(item["category"])

    return {
        "run_month": month,
        "validation_status": "valid",
        "validation_errors": [],
        "flagged_categories": flagged,
        "suppressed_categories": suppressed,
        "escalated_categories": escalated,
        "action_taken": "drafted_and_held_for_approval"
    }

if __name__ == "__main__":
    result = run("May", "part2_engine/fixtures/monthly_category_revenue.csv", "part2_engine/fixtures/monthly_category_revenue.csv")
    print(json.dumps(result, indent=2))
