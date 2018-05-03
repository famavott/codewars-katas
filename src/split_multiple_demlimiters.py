"""Split string by multiple delimiters."""


def multiple_split(string, delimiters=[]):
    """."""
    if delimiters == []:
        return [string]
    for x in delimiters:
        string = string.replace(x, ' ')
    return string.split()
