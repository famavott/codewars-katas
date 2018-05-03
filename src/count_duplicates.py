"""Write a function that will return the count of distinct alphabetic chars and nums."""


def duplicate_count(text):
    """."""
    normalize = text.lower()
    letters = {}
    for l in normalize:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return len([k for k, v in letters.items() if v > 1])
