"""Kata: Given string of words, return length of shortest."""


def find_short(strg):
    """Return length of shortest word in sentence."""
    words = strg.split()
    min_size = float('inf')
    for word in words:
        if len(word) < min_size:
            min_size = len(word)
    return min_size
