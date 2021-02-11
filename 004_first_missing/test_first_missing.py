__author__ = "Sean Moore"

import pytest
from first_missing import *

@pytest.mark.parametrize("input,expected", [
    ([3,4,-1,1], 2),
    ([1,2,0], 3),
    ([], 1),
    ([1,2,3,4], 5),
    ([-3,-6,-1], 1)
])
def test_solution(input, expected):
    assert first_missing_brute(input) == expected
    assert first_missing_sort(input) == expected
    assert first_missing(input) == expected