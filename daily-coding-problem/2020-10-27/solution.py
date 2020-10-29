__author__ = "Sean Moore"

"""
This looks like a combinitorics problem that I may be able to solve using a
recursive approach and then optimize with memoization.
"""

def number_of_ways_1(n):
    """
    Returns the number of unique ways to climb a staircase with n steps,
    taking 1 or 2 steps with each stride.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return number_of_ways_1(n - 1) + number_of_ways_1(n - 2)

def number_of_ways_2(n, x):
    """
    Returns the number of unique ways to climb a staircase with n steps,
    taking steps from the set x with each stride.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    count = 0
    for num_steps in x:
        count += number_of_ways_2(n - num_steps, x)
    return count

def number_of_ways_3(n, x):
    """
    Returns the number of unique ways to climb a staircase with n steps,
    taking steps from the set x with each stride. Uses memoization for
    improved efficiency.
    """
    table = dict()
    def helper(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n in table:
            return table[n]
        count = 0
        for num_steps in x:
            count += helper(n - num_steps)
        table[n] = count
        return count
    return helper(n)