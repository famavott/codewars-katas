"""Test file for List Filtering Function."""
import pytest


example_tests = [([1, 2, 'a', 'b'], [1, 2]),
                 ([1, 'a', 'b', 0, 15], [1, 0, 15]),
                 ([1, 2, 'aasf', '1', '123', 123], [1, 2, 123]),
                 ([2, 4, '0', 'd'], [2, 4]),
                 ([555, 0, 'the'], [555, 0]),
                 ([7, 4, 5, 92], [7, 4, 5, 92]),
                 (['hi', 'there', '0', 9], [9]),
                 ([1, 4, '909', 'ccc'], [1, 4]),
                 ]


@pytest.mark.parametrize('given_list, result', example_tests)
def test_filter_list(given_list, result):
    """Function checks if list successfully removes strings."""
    from list_filtering import filter_list
    assert filter_list(given_list) == result

    # test.assert_equals(filter_list([1,'a','b',0,15]),[1,0,15])
    # test.assert_equals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])
