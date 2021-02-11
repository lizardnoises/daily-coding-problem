__author__ = "Sean Moore"

import pytest
from k_distinct import length_k_substring

@pytest.mark.parametrize("s,k,expected", [
    ('abcba', 2, 3)
])
def test_length_k_substring(s, k, expected):
    assert length_k_substring(s, k) == expected