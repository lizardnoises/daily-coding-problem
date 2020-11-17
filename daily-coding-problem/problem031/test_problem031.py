__author__ = "Sean Moore"

import pytest
from problem031 import *

@pytest.mark.parametrize("s1,s2,expected", [
    ("kitten", "sitting", 3)
])
def test_edit_distance(s1, s2, expected):
    assert edit_distance(s1, s2) == expected
    assert edit_distance_memoized(s1, s2) == expected