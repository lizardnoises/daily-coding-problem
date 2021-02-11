__author__ = 'Sean Moore'

from problem081 import all_mappings
import pytest

@pytest.mark.parametrize('m,s,expected',[
    ({'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']}, '23',
    ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
])
def test_all_mappings(m, s, expected):
    assert all_mappings(m, s) == expected