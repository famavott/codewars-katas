"""Kata: Find num that is unique in array."""


def find_unique(arr):
    """."""
    in_order = sorted(arr)
    if (in_order[0] < in_order[len(in_order) - 1] and in_order[0] < in_order[len(in_order) - 2]):
        num = in_order[0]
    else:
        num = in_order[len(in_order) - 1]
    return num
