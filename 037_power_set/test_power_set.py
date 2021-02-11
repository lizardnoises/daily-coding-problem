__author__ = 'Sean Moore'

import pytest
from power_set import *

@pytest.mark.parametrize('input,expected', [
    ({1,2,3}, set(frozenset(x) for x in
        [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]))
])
def test_power_set(input, expected):
    assert power_set(input) == expected
    assert power_set_recursive(input) == expected