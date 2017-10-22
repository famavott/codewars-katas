"""Test file for pig_latin Function."""
import pytest


pig_tests = [('map', 'apmay'),
             ('egg', 'eggway'),
             ('spaghetti', 'aghettispay'),
             ('ttttt', 'tttttay'),
             ('roast', 'oastray'),
             ('yes', 'esyay'),
             ('ghoul', 'oulghay')
             ]


@pytest.mark.parametrize('word, result', pig_tests)
def test_pig_latin(word, result):
    """Test to see if pig latin word follows rules from kata."""
    from single_word_piglatin import pig_latin
    assert pig_latin(word) == result
