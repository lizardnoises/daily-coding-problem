__author__ = "Sean Moore"

import pytest
import solution

@pytest.mark.parametrize("s,k,expected", [
    ('abcba', 2, 3)
])
def test_length_k_substring(s, k, expected):
    assert solution.length_k_substring(s, k) == expected