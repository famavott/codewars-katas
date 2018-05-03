"""Kata: Simple string characters."""


def solve(s):
    final = [0, 0, 0, 0]
    for x in s:
        if x.istitle():
            final[0] += 1
        elif x.islower():
            final[1] += 1
        elif x.isdigit():
            final[2] += 1
        else:
            final[3] += 1
    return final
