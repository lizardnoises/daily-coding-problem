__author__ = "Sean Moore"

import pytest
from max_nonadjacent import *

@pytest.mark.parametrize('input,expected',[
    ([2,4,6,2,5], 13),
    ([5,1,1,5], 10)
])
def test_max_non_adjacent_sum(input, expected):
    assert max_non_adjacent_sum(input) == expected
    assert max_non_adjacent_sum_memoized(input) == expected