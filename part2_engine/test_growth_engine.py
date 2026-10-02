import pytest
from growth_engine import mom_growth, is_flagged, validate_feed

def test_mom_growth_and_flagged():
    # GIVEN April→May Ethnic Wear revenue
    assert mom_growth(104520.77, 185107.61) == 77.1
    assert is_flagged(77.1) == "flagged"

    # GIVEN May→June Beauty & Personal Care revenue
    assert mom_growth(35542.11, 37559.07) == 5.67
    assert is_flagged(5.67) == "not_flagged"

    # GIVEN synthetic boundary case
    assert mom_growth(100000, 108000) == 8.0
    assert is_flagged(8.0) == "escalate_exact_boundary"

def test_validate_feed_corrupted():
    valid, errors = validate_feed("part2_engine/fixtures/corrupted_feed.csv")
    assert not valid
    assert errors == [
        "line 3: negative revenue (-4200.0) for category=Western Wear",
        "line 4: missing category (month=July)",
        "line 6: missing revenue (category=Home & Kitchen)"
    ]

def test_validate_feed_clean():
    valid, errors = validate_feed("part2_engine/fixtures/monthly_category_revenue.csv")
    assert valid
    assert errors == []
