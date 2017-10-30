"""Test if a string of parentheses is open, balanced, or broken with the use of a data structure."""

from que_ import Queue


def proper_parenthetics(string):
    """Function tests if string is open, balanced, or broken."""
    new_queue = Queue()
    count = 0
    for item in string:
        new_queue.enqueue(item)
    while len(new_queue) > 0:
        new_queue.dequeue(item)
        if item == '(':
            count += 1
        elif item == ')':
            count -= 1
    if count == 0:  # balanced
        return 0
    elif count > 0:  # open
        return 1
    else:
        return -1  # broken
