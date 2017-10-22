"""Test file for pig_it Function."""
import pytest


pig_examples = [('Pig latin is cool', 'igPay atinlay siay oolcay'),
                ('This is my string', 'hisTay siay ymay tringsay'),
                ('Pigggggg', 'iggggggPay'),
                ('matt favoino', 'attmay avoinofay'),
                ('test', 'esttay'),
                ('Code Wars', 'odeCay arsWay')
                ]


@pytest.mark.parametrize('string, result', pig_examples)
def test_simple_pig_latin(string, result):
    """Test to see if result adheres to pig latin rules."""
    from simple_pig_latin import pig_it
    assert pig_it(string) == result
