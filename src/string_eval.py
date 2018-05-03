"""String evaluation kata (6 kyu)."""


def string_evaluation(strng, conditions):
    """Iterate through conditions and eval to return list of bools."""
    final = []
    for item in conditions:
        if item[0].isdigit():
            left = item[0]
        else:
            left = str(strng.count(item[0]))
        if item[-1].isdigit():
            right = item[-1]
        else:
            right = str(strng.count(item[-1]))
        expr = left + item[1:-1] + right
        final.append(eval(expr))
    return final
