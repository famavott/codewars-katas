"""Create digital root func that is recursive sum of all digits in num."""


def digital_root(n):
    """Digital root of number passed."""
    if n < 10:
        return n
    else:
        total = 0
        for i in str(n):
            total += int(i)
        return digital_root(total)
