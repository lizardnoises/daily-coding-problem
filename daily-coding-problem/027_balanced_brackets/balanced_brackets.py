__author__ = 'Sean Moore'

"""
Problem:

Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def is_balanced(s):
    """Return True if the brackets in string s are balanced."""
    stack = []
    match = {')':'(', '}':'{', ']':'['}
    for c in s:
        if c in match.values():
            stack.append(c)
        elif c in match:
            top = stack.pop()
            if top != match[c]:
                return False
    if len(stack) == 0:
        return True
    return False
