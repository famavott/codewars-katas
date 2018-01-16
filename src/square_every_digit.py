"""Square every digit of a number."""


def square_digits(num):
    """Function takes an integer and returns an integer."""
    temp = [int(x) ** 2 for x in list(str(num))]
    return int(''.join(map(str, temp)))
