"""Kata Find the Odd Int

#1 Best practice solution

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""


def find_it(seq):
    """Function returns number that occurs odd num of times."""
    counts = {}
    for item in seq:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for prop in counts:
        if counts[prop] % 2 != 0:
            return(prop)
