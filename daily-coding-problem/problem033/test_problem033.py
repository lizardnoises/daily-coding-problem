__author__ = "Sean Moore"

import pytest
from problem033 import list_medians

@pytest.mark.parametrize("input,expected", [
    ([2,1,5,7,2,0,5], [2,1.5,2,3.5,2,2,2])
])
def test_medians(input, expected):
    assert list_medians(input) == expected