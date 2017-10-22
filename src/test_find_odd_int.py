"""Test file for find_it Function."""
import pytest

odd_tests = [([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5),
             ([1, 1, 1, 1, 7], 7),
             ([17, 18, 99, 17, 18, 18, 18], 99),
             ([9, 9, 9, 9, 0], 0),
             ([100, 200, 200, 200, 100, 1000, 1000], 200)
             ]


@pytest.mark.parametrize('seq, result', odd_tests)
def test_find_it(seq, result):
    """Test to see if num with odd num of occurences returned."""
    from find_odd_int import find_it
    assert find_it(seq) == result
