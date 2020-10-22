__author__ = "Sean Moore"

import pytest
from solution import Node as N
import solution

@pytest.mark.parametrize("input,expected", [
    (N(0,N(1),N(0,N(1,N(1),N(1)),N(0))), 5),
    (None, 0),
    (N(0), 1),
    (N(1,N(1,N(1),N(1)),N(2,N(2),N(2))), 6)
])
def test_count_unival_subtrees(input, expected):
    assert solution.count_unival_subtrees(input) == expected