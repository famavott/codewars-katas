"""Return count of pairs that have consecutive numbers in array."""


def pairs(arr):
    """Return count of pairs with consecutive nums."""
    count = 0
    pairs = [arr[i:i + 2] for i in range(0, len(arr), 2)]
    for pair in pairs:
        if len(pair) == 2:
            if abs(pair[0] - pair[1]) == 1:
                count += 1
    return count
