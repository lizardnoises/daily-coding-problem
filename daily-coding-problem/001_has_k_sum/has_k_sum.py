__author__ = "Sean Moore"

"""
Problem:

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def hasSum(a, k):
    """Return True if any pair of elements in the array a sums to the value k.
    O(n^2)
    """
    if len(a) < 2:
        return False
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k:
                return True
    return False

def hasSumBonus(a, k):
    """Return True if any two elements in the array a sums to the value k.
    Python set is implemented as a hash table. Lookup is O(1) average, O(n) worst.
    So this implementation is O(n) average, O(n^2) worst. A binary search tree
    could be used instead for O(nlogn) worst case.
    """
    visited = set()
    for x in a:
        if k - x in visited:
            return True
        visited.add(x)
    return False