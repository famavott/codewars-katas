"""Test file for pig_latin Function."""
import pytest


fizz_tests = [
              (10, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']),
              (3, [1, 2, 'Fizz']),
              (2, [1, 2]),
              (5, [1, 2, 'Fizz', 4, 'Buzz']),
              (7, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7])
              ]


@pytest.mark.parametrize('num, result', fizz_tests)
def test_fizzbuzz(num, result):
    """Function checks if correct array is returned from rules defined in kata."""
    from fizzbuzz import fizzbuzz
    assert fizzbuzz(num) == result
