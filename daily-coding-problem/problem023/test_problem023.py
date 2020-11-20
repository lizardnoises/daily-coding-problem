__author__ = 'Sean Moore'

import pytest
from problem023 import min_steps

def test_min_steps():
    b = [[False, False, False, False],
         [True,  True,  False, True ],
         [False, False, False, False],
         [False, False, False, False]]
    s = (3, 0)
    e = (0, 0)
    assert min_steps(b, s, e) == 7