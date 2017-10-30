"""Tests for parenthetics.py file."""
import pytest

tests = [
        ['()()()()())', -1],
        ['()()', 0],
        ['(', 1],
        ['))))', -1],
        ['()()()()()()()()()()()()()()', 0],
        ['()(', 1]
]


@pytest.mark.parametrize('string, output', tests)
def test_proper_parenthetics():
    """Function tests if string passed gives expected output of -1, 0, or 1."""
    from parenthetics import proper_parenthetics
    assert proper_parenthetics(string) == output
