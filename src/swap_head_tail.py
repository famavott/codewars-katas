"""Swap head and tail of given array."""


def swap_head_tail(arr):
    """Swap head and tail of given array."""
    mid = int(len(arr) // 2)
    if len(arr) % 2 == 0:
        return arr[mid + 1:] + [arr[mid]] + arr[:mid]
    else:
        return arr[mid:] + arr[:mid]
