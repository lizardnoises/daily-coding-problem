__author__ = "Sean Moore"

import pytest
import solution

@pytest.mark.parametrize("input,expected", [
    ([3,4,-1,1], 2),
    ([1,2,0], 3),
    ([], 1),
    ([1,2,3,4], 5),
    ([-3,-6,-1], 1)
])
def test_solution(input, expected):
    assert solution.first_missing_brute(input) == expected
    assert solution.first_missing_sort(input) == expected
    assert solution.first_missing(input) == expected