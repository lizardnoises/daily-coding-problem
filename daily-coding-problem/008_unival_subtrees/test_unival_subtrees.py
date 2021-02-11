__author__ = "Sean Moore"

import pytest
from unival_subtrees import Node as N, count_unival_subtrees

@pytest.mark.parametrize("input,expected", [
    (N(0,N(1),N(0,N(1,N(1),N(1)),N(0))), 5),
    (None, 0),
    (N(0), 1),
    (N(1,N(1,N(1),N(1)),N(2,N(2),N(2))), 6)
])
def test_count_unival_subtrees(input, expected):
    assert count_unival_subtrees(input) == expected