__author__ = 'Sean Moore'

"""
Problem:

Given a mapping of digits to letters (as in a phone number), and a digit
string, return all possible letters the number could represent. You can assume
each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should
return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

def all_mappings(digit_map, digit_string):
    """Return all possible applications of the given digit-to-letter mapping to 
    the given digit string. Assume all digits in the digit string have valid
    mappings. O(n*m) runtime, where n is the number of mappings per digit and
    m is the length of the digit string.
    """
    if len(digit_string) == 0:
        return []
    if len(digit_string) == 1:
        return digit_map[digit_string]
    possibilities = []
    for l in digit_map[digit_string[0]]:
        for p in all_mappings(digit_map, digit_string[1:]):
            possibilities.append(l + p)
    return possibilities