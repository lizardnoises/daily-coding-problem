__author__ = "Sean Moore"

"""
This looks like a combinatorics problem, which I might be able to break down
into a divide and conquer approach using memoization to compute in O(n) time
and space. Here is a recursive relationship I noticed while walking through the
example manually:

case 1: 2,4,6,2,5
        -   -----
case 2: 2,4,6,2,5
          -   ---
"""

def max_non_adjacent_sum(a):
    """
    Recursive solution, breaking down the problem into subproblems.
    """
    if not a:
        return 0
    if len(a) == 1:
        return a[0]
    return max(a[0] + max_non_adjacent_sum(a[2:]),
               a[1] + max_non_adjacent_sum(a[3:]))

def max_non_adjacent_sum_memoized(a):
    """
    Improving the runtime complexity using memoization of the subproblems.
    """
    table = dict()
    def helper(a, table, i):
        if i in table:
            return table[i]
        if len(a) - i == 0:
            table[i] = 0
        elif len(a) - i == 1:
            table[i] = a[i]
        elif len(a) - i == 2:
            table[i] = max(a[0], a[1])
        else:
            table[i] = max(a[i] + helper(a, table, i + 2),
                           a[i + 1] + helper(a, table, i + 3))
        return table[i]
    return helper(a, table, 0)