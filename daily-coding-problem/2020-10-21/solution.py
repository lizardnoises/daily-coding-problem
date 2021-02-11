__author__ = "Sean Moore"

"""
My initial thoughts are to try a brute force approach and solve an example by
hand, while looking for a pattern that allows the problem to be broken up into
subproblems. If there is significant overlap, perhaps subproblem results could
be memoized.
"""

def count_decodes(s):
    """
    Returns the number of ways the string can be decoded. Breaks the problem
    down into subproblems on substrings and adds together the partial solutions.
    """
    if not s:
        return 0
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if 11 <= int(s) <= 26:
            return 2
        return 1
    return count_decodes(s[1:]) + count_decodes(s[2:])