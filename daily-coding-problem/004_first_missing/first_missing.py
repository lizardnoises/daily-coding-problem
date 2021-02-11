__author__ = "Sean Moore"

"""
Problem:

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.
"""

def first_missing_brute(input):
    """Brute force approach, ignoring the complexity constraints. Scan the array for
    existance of the lowest positive integer so far, restarting the scan with the
    next LPI when found. O(n^2) time, O(1) space.
    """
    lpi = 1
    while lpi in input:
        lpi += 1
    return lpi

def first_missing_sort(input):
    """Improvement on the brute force approach by sorting the array before scanning.
    O(n log n) time, O(1) space.
    """
    input.sort()
    lpi = 1
    for x in input:
        if x == lpi:
            lpi += 1
        elif x > lpi:
            break
    return lpi

def first_missing(input):
    """Set membership approach. Convert the input array, in-place, into a set. At
    each index, a corresponding value represents membership. The conversion is
    done by iterating over the input and swapping each value into its corresponding
    index. This is a linear time operation because no element is swapped more than
    once. O(n) time, O(1) space.
    """
    if not input:
        return 1
    for i in range(len(input)):
        while ( input[i] != i + 1 and
                input[i] > 0 and
                input[i] <= len(input) and
                input[i] != input[input[i] - 1] ):
            value = input[i]
            input[i], input[value - 1] = input[value - 1], value
    for i in range(len(input)):
        if input[i] != i + 1:
            return i + 1
    return i + 2