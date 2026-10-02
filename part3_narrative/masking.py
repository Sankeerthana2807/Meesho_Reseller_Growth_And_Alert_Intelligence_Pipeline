def alias_for(reseller_id: str) -> str:
    """
    Mask reseller IDs into alias format.
    Example: RS019 -> ALIAS-19
    """
    return f"ALIAS-{reseller_id[3:]}"

def assert_no_raw_names_leak(text: str, reseller_names: list[str]) -> bool:
    """
    Ensure no raw reseller names appear in narrative text.
    Returns False if any raw name is found.
    """
    for name in reseller_names:
        if name in text:
            return False
    return True


# Example narrative using alias
narrative = "Top reseller in West region is ALIAS-19 with strong performance."
reseller_names = ["Mumbai Reseller 1", "Mumbai Reseller 4", "Hyderabad Reseller 6", "Lucknow Reseller 6", "Jaipur Reseller 5"]

assert assert_no_raw_names_leak(narrative, reseller_names) == True
assert assert_no_raw_names_leak("Mumbai Reseller 1 had high sales", reseller_names) == False
