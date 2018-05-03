"""Given input string, check if all lowercase and return letters that are upper."""


def case_sensitive(strg):
    """Return list with bool and letters not upper."""
    upper = []
    for let in strg:
        if let == let.upper():
            upper.append(let)
    if len(upper):
        return [False, upper]
    return [True, []]
