__author__ = 'Sean Moore'

import rl_encoding

def test_encode():
    input = 'AAAABBBCCDAA'
    expected = '4A3B2C1D2A'
    assert rl_encoding.encode(input) == expected