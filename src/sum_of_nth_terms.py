"""Kata Sum of nth terms

# 1 Best practice solution

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

"""
from __future__ import division


def series_sum(n):
    """Function sums the a series of numbers up to the nth parameter."""
    denom = 4
    sum_arr = [1]
    if n == 0:
        return '0.00'
    for num in range(1, n):
        sum_arr.append((1 / (denom)))
        denom += 3
    return('%.2f' % (sum(sum_arr)))
