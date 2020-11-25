__author__ = 'Sean Moore'

"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that,
given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3},
{1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.

---

I was thinking of using a recursive approach by breaking the problem into 
subproblems of subsets. But after looking into the other approaches, I found a
one that takes advantage of the binary representations of numbers to
map a counter to subsets. Each bit represents an index into all elements of the
set and can be used to uniquely construct every subset. For each subset in the
powerset, each element of the set is either included or not. So there are
2^N subsets covering all combinations. This solution is my attempt at applying
that approach.
"""

def power_set(s):
    """Returns the power set of s."""
    s = list(s)
    pset = []
    for x in range(pow(2, len(s))):
        sset = []
        for i in range(len(s)):
            if x & (1 << i):
                sset.append(s[i])
        pset.append(sset)
    return set(map(frozenset, pset))

def power_set_recursive(s):
    """Returns the power set of the s."""
    def helper(s):
        if len(s) == 0:
            return [[]]
        pset = helper(s[1:])
        return pset + [sset + [s[0]] for sset in pset]
    return set(map(frozenset, helper(list(s))))