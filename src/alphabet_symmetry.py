"""Kata: Alphabet Symmetry."""


def solve(arr):
    """."""
    final = [0 for x in arr]
    for idx, word in enumerate(arr):
        for ix, l in enumerate(word.lower()):
            if ix + 1 == ord(l) - 96:
                final[idx] += 1
    return final
