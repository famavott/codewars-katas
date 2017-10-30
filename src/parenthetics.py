"""Test if a string of parentheses is open, balanced, or broken with the use of a data structure."""

from stack import Stack


def proper_parenthetics(string):
    """Function tests if string is open, balanced, or broken."""
    new_stack = Stack()
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return -1
    if count == 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    print(proper_parenthetics('()()()()())'))
    print(proper_parenthetics('()()'))
    print(proper_parenthetics('('))
