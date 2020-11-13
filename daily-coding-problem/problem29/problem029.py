__author__ = 'Sean Moore'

"""
Problem #29 [Easy]
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
"""

def encode(s):
    """
    Returns a run-length encoding of string s. s must consist of only alpha
    characters and must be a valid string.
    """
    if not s:
        return s
    count = 0
    last_c = s[1]
    encoded = ''
    for c in s:
        if c == last_c:
            count += 1
        else:
            encoded += str(count) + last_c
            last_c = c
            count = 1
    encoded += str(count) + last_c
    return encoded
