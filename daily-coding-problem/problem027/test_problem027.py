__author__ = 'Sean Moore'

import pytest
from problem027 import is_balanced

@pytest.mark.parametrize('input,expected', [
    (r'([])[]({})', True),
    (r'([)]', False),
    (r'((()', False),
    (r'([a], b)[c](d, {e}, f)', True)
])
def test_is_balanced(input, expected):
    assert is_balanced(input) == expected