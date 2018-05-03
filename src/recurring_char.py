"""Find first recurring character. Return None if no recurring chars."""


def recurring(strg):
    """O(n) solution."""
    for idx, c in enumerate(strg):
        if c in strg[idx + 1:]:
            return c
    return None


def recurring_2(strg):
    """Hash map solution O(n)."""
    counts = {}
    for c in strg:
        if c in counts:
            return c
        else:
            counts[c] = 1
    return None
