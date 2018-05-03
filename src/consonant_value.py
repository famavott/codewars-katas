"""Return max substring split on vowels with consonants mapped 1-26."""


def solve(s):
    """Return max substring value.

    Strips string into substring and calculates value based on mapping
    using ord() - 96 value for letters a-z.
    """
    vowels = 'aeiou'
    stripped = ''
    for l in s:
        if l in vowels:
            stripped += ','
        else:
            stripped += l
    stripped_list = stripped.split(',')
    sub_values = []
    for item in stripped_list:
        if len(item) >= 1:
            vals = sum([ord(x) - 96 for x in item])
            sub_values.append(vals)
    return max(sub_values)
