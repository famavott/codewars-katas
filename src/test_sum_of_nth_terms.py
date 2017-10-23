"""Test file for series_sum function."""
import pytest


test_cases = [(1, '1.00'), (2, '1.25'), (3, '1.39')]


@pytest.mark.parametrize('n, result', test_cases)
def test_series_sum(n, result):
    """Test function to for series sum to check for expected result."""
    from sum_of_nth_terms import series_sum
    assert series_sum(n) == result
