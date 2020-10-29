__author__ = "Sean Moore"

import pytest
import solution

@pytest.mark.parametrize("n,expected", [
    (4, 5),
    (1, 1),
    (2, 2),
    (3, 3)
])
def test_number_of_ways_1(n, expected):
    assert solution.number_of_ways_1(n) == expected

@pytest.mark.parametrize("n,x,expected", [
    (4, [1, 2], 5),
    (4, [1], 1),
    (4, [2], 1),
    (4, [1, 3], 3)
])
def test_number_of_ways_2_3(n, x, expected):
    assert solution.number_of_ways_2(n, x) == expected
    assert solution.number_of_ways_3(n, x) == expected