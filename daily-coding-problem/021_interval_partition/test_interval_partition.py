__author__ = "Sean Moore"

import pytest
from interval_partition import find_min_num_rooms

@pytest.mark.parametrize("input,expected", [
    ([], 0),
    ([(1,2)], 1),
    ([(30,75), (0,50), (60,150)], 2),
    ([(30,75), (0,50), (20,150)], 3),
    ([(30,75), (0,30), (75,150)], 1)
])
def test_find_min_num_rooms(input, expected):
    assert find_min_num_rooms(input) == expected