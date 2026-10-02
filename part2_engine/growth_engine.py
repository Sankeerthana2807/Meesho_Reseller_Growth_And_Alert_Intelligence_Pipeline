# Growth Engine for Meesho Reseller Pipeline
# Implements MoM growth, flagging logic, and feed validation

import csv

def mom_growth(previous: float, current: float) -> float:
    """
    Calculate Month-on-Month growth percentage.
    Formula: ((current - previous) / previous) * 100
    Rounded to 2 decimals.
    """
    return round((current - previous) / previous * 100, 2)


def is_flagged(mom_pct: float, threshold: float = 8.0) -> str:
    """
    Flagging logic:
    - "flagged" if abs(mom_pct) > threshold
    - "not_flagged" if abs(mom_pct) < threshold
    - "escalate_exact_boundary" if abs(mom_pct) == threshold
    """
    if abs(mom_pct) > threshold:
        return "flagged"
    elif abs(mom_pct) < threshold:
        return "not_flagged"
    else:
        return "escalate_exact_boundary"


def validate_feed(csv_path: str) -> tuple[bool, list[str]]:
    """
    Validate the monthly revenue feed CSV.
    Checks:
    - Missing category
    - Missing revenue
    - Non-numeric revenue
    - Negative revenue
    Returns (True, []) if valid, else (False, [errors]).
    """
    errors = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):  # line numbers start at 2 (header = line 1)
            month = row.get("month", "")
            category = row.get("category", "")
            revenue = row.get("revenue", "")

            if category.strip() == "":
                errors.append(f"line {i}: missing category (month={month})")
            if revenue.strip() == "":
                errors.append(f"line {i}: missing revenue (category={category})")
            else:
                try:
                    rev_val = float(revenue)
                    if rev_val < 0:
                        errors.append(f"line {i}: negative revenue ({rev_val}) for category={category}")
                except ValueError:
                    errors.append(f"line {i}: revenue not numeric: {revenue!r}")

    return (len(errors) == 0, errors)
