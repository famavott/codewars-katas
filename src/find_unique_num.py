"""Find unique number in given array."""


def find_uniq(arr):
    """Return unique integer in array."""
    sort = sorted(arr)
    if (sort[0] < sort[len(sort) - 1] and sort[0] < sort[len(sort) - 2]):
        n = sort[0]
    else:
        n = sort[len(sort) - 1]
    return n
