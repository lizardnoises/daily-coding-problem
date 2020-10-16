__author__ = "Sean Moore"

"""
Return True if any pair of elements in the array a sums to the value k.
O(n^2)
"""
def hasSum(a, k):
    if len(a) < 2:
        return False
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k:
                return True
    return False

"""
Return True if any two elements in the array a sums to the value k.
Python set is implemented as a hash table. Lookup is O(1) average, O(n) worst.
So this implementation is O(n) average, O(n^2) worst.
"""
def hasSumBonus(a, k):
    visited = set()
    for x in a:
        if k - x in visited:
            return True
        visited.add(x)
    return False