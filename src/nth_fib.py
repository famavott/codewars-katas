"""N-th Fibonacci Kata."""


def nth_fib(num):
    """Return n-th number in the Fibonacci Sequence."""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return nth_fib(num - 1) + nth_fib(num - 2)
