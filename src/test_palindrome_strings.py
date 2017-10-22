"""Test file for Is Palindrome Function."""
import pytest

pal_tests = [("anna", True),
             ("walter", False),
             (12321, True),
             (123456, False),
             ("maam", True),
             ("matt", False),
             ("tugboat", False),
             (11, True)
             ]


@pytest.mark.parametrize('string, result', pal_tests)
def test_is_palindrome(string, result):
    """Function checks if string is actually palindrome."""
    from palindrome_strings import is_palindrome
    assert is_palindrome(string) == result
