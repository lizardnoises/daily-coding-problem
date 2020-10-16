__author__ = "Sean Moore"

import pytest
import solution

def testExample():
    a = [10,15,3,7]
    k = 17
    assert solution.hasSum(a, k) == True
    assert solution.hasSumBonus(a, k) == True

@pytest.mark.parametrize(
    "a,k,expected", [
    ([], 17, False),
    ([], 0, False),
    ([1,2], 3, True),
    ([1,2], 4, False),
    ([1,2,3], 5, True),
    ([1,2,3], 6, False),
    ([4,-5,6], 1, True),
    ([4,-5,6], -1, True),
    ([4,-5,6], 2, False),
    ([4,-5,6], -2, False)
])
def testHasSum(a, k, expected):
    assert solution.hasSum(a, k) == expected
    assert solution.hasSumBonus(a, k) == expected