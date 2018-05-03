"""Given two strings, return string with nums in str2 not in str1."""


def find_added(st1, st2):
    """."""
    for i in st1:
        st2 = st2.replace(i, '')
    return ''.join(sorted(st2))
