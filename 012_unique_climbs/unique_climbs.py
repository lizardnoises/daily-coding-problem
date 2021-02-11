__author__ = "Sean Moore"

"""
Problem:

There exists a staircase with N steps, and you can climb up either 1 or 2 steps
at a time. Given N, write a function that returns the number of unique ways you
can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb
any number from a set of positive integers X? For example, if X = {1, 3, 5},
you could climb 1, 3, or 5 steps at a time.
"""
"""
This looks like a combinitorics problem that I may be able to solve using a
recursive approach and then optimize with memoization.
"""

def number_of_ways_1(n):
    """Return the number of unique ways to climb a staircase with n steps,
    taking 1 or 2 steps with each stride.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return number_of_ways_1(n - 1) + number_of_ways_1(n - 2)

def number_of_ways_2(n, x):
    """Return the number of unique ways to climb a staircase with n steps,
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
    """Return the number of unique ways to climb a staircase with n steps,
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