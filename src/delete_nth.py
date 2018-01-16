"""Delete occurences of element if it occurs more than n times."""


def delete_nth(order, max_e):
    """Create new list that contains each number at most N times."""
    counting = {x: 0 for x in order}
    final = []
    for i in order:
        if counting[i] < max_e:
            counting[i] += 1
            final.append(i)
    return final
