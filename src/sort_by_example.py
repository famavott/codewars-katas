"""."""

arr = [1, 3, 4, 4, 4, 4, 5]
ex_arr = [4, 1, 2, 3, 5]


def example_sort(arr, ex_arr):
    """."""
    new = []
    for i in ex_arr:
        if i in arr:
            for j in range(arr.count(i)):
                new.append(i)
    return new
