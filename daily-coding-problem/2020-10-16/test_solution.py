__author__ = "Sean Moore"

import pytest
import solution

@pytest.mark.parametrize(
    "a,expected", [
    ([], []),
    ([4], [1]),
    ([1,2,3,4,5], [120,60,40,30,24]),
    ([2,3,0,4,5], [0,0,120,0,0]),
    ([0], [1]),
    ([0,0,0,0], [0,0,0,0]),
    ([1,0,2,0,3], [0,0,0,0,0]),
    ([-3,4,10], [40,-30,-12]),
    ([-3,-4,10], [-40,-30,12]),
    ([-4,0], [0,-4])
])
def test_excluded_product(a, expected):
    assert solution.excluded_products(a) == expected
    assert solution.excluded_products_div(a) == expected
    assert solution.excluded_products_bonus(a) == expected