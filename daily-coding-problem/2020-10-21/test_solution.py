__author__ = "Sean Moore"

import pytest
import solution as s

@pytest.mark.parametrize("input,expected", [
    ('1', 1),
    ('2', 1),
    ('11', 2),
    ('10', 1),
    ('111', 3),
    ('001', 0),
    ('101', 1),
    ('163', 2)
])
def test_count_decodes(input, expected):
    assert s.count_decodes(input) == expected
