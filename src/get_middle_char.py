"""Return middle character of word. If length is even, return middle two."""


def get_middle(word):
    """Return middle character in a given string."""
    hold = []
    for i in word:
        hold.append(i)
    mid = len(hold) // 2
    if len(hold) % 2 != 0:
        return hold[mid]
    else:
        return hold[mid - 1] + hold[mid]
