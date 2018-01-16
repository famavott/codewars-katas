"""Return highest and lowest nums separated by space as a string."""


def high_and_low(nums):
    """Return highest and lowest nums separated by space as a string."""
    new = [int(x) for x in nums.split()]
    return str(max(new)) + ' ' + str(min(new))
