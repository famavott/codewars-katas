"""Given array comprised of either odd/even nums except for a single int.

Write method that takes array as argument and returns the outlier.
"""


def find_outlier(arr):
    """Return outlier from list of even and odd ints."""
    even = []
    odd = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if len(even) > 1:
        return odd[0]
    else:
        return even[0]
