"""Kata: Palindrome Strings

#1 Best practice solution

def is_palindrome(string):
    return str(string)[::-1] == str(string)

"""


def is_palindrome(string):
    """Function checks if passed string is palindrome."""
    converted_string = str(string)
    rev = converted_string[::-1]
    if rev == converted_string:
        return True
    else:
        return False


def is_palindrome(strng):
    """Return bool if strng is palindrome."""
    return str(strng) == str(strng)[::-1]
