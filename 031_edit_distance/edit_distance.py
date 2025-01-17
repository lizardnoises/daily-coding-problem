__author__ = "Sean Moore"

"""
Problem:

The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""
"""
This is a clasic dynamic programming problem. The problem can be broken down
into a recursive relation of subproblems using substrings. The optimal solution
is the result of optimal solution for the substrings with one operation rewound
plus the cost of that operation. Which operation to rewind depends on which
pair of substrings form the subproblem with the best solution.
"""

def edit_distance(s1, s2):
    """Return the edit distance between strings s1 and s2."""
    def helper(i, j):
        if i < 0:
            return j + 1 # all dels
        if j < 0:
            return i + 1 # all adds
        if s1[i] == s2[j]:
            return helper(i-1, j-1)
        return min(helper(i-1, j-1) + 1, # sub
                   helper(i, j-1) + 1, # add
                   helper(i-1, j) + 1) # del
    return helper(len(s1)-1, len(s2)-1)

def edit_distance1(s1, s2):
    """Return the edit distance between strings s1 and s2. This recursive
    relation has a lot of overlap, so memoization improves runtime efficiency.
    """
    memo = {}
    def helper(i, j):
        if (i, j) not in memo:
            if i < 0:
                memo[(i, j)] = j + 1 # all dels
            elif j < 0:
                memo[(i, j)] = i + 1 # all adds
            elif s1[i] == s2[j]:
                memo[(i, j)] = helper(i-1, j-1)
            else:
                memo[(i, j)] = min(helper(i-1, j-1) + 1, # sub
                                helper(i, j-1) + 1, # add
                                helper(i-1, j) + 1) # del
        return memo[(i, j)]
    return helper(len(s1)-1, len(s2)-1)

def memoize(f):
    memo = {}
    def helper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return helper

def edit_distance2(s1, s2):
    """Return the edit distance between strings s1 and s2. Decorates the
    recursive helper function with a memoizing function.
    """
    @memoize
    def helper(i, j):
        if i < 0:
            return j + 1 # all dels
        if j < 0:
            return i + 1 # all adds
        if s1[i] == s2[j]:
            return helper(i-1, j-1)
        return min(helper(i-1, j-1) + 1, # sub
                   helper(i, j-1) + 1, # add
                   helper(i-1, j) + 1) # del
    return helper(len(s1)-1, len(s2)-1)