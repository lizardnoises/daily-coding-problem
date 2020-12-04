__author__ = 'Sean Moore'

import pytest
from problem050 import Node as N
from problem050 import eval_tree

@pytest.mark.parametrize('input,expected', [
    (N('+',N(3),N(2)), 5),
    (N('-',N(3),N(2)), 1),
    (N('*',N(3),N(2)), 6),
    (N('/',N(3),N(2)), 1.5),
    (N('*',N('+',N(3),N(2)),N('+',N(4),N(5))), 45)
])
def test_eval_tree(input, expected):
    assert eval_tree(input) == expected