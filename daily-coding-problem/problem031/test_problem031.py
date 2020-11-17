__author__ = "Sean Moore"

import pytest
from problem031 import *

@pytest.mark.parametrize("s1,s2,expected", [
    ("kitten", "sitting", 3),
    ("", "", 0),
    ("abc", "abc", 0),
    ("abc", "bca", 2)
])
def test_edit_distance(s1, s2, expected):
    assert edit_distance(s1, s2) == expected
    assert edit_distance1(s1, s2) == expected
    assert edit_distance2(s1, s2) == expected