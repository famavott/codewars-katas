"""Find longest consecutive character in a string."""


def consec(strg):
    """Return letter and length that is longest consecutive in string."""
    max_len = 0
    count = 0
    prev = ''
    for char in strg:
        if char == prev:
            count += 1
        else:
            count = 1
            prev = char
        max_len = max(count, max_len)
    return max_len
