"""Test file for pig_latin Function."""
import pytest


vowel_test = [('abracadabra', 5),
              ('aaa', 3),
              ('matt', 1),
              ('programming', 3),
              ('parametrize', 5)]


@pytest.mark.parametrize('inputstr, result', vowel_test)
def test_getcount(inputstr, result):
    """Test function to ensure output is correct num vowels."""
    from vowel_count import getcount
    assert getcount(inputstr) == result
