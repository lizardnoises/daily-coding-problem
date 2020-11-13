__author__ = 'Sean Moore'

import problem029 as p

def test_encode():
    input = 'AAAABBBCCDAA'
    expected = '4A3B2C1D2A'
    assert p.encode(input) == expected