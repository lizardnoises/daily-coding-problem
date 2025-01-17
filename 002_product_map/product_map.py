__author__ = "Sean Moore"

"""
Problem:

Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
"""

def excluded_products(a):
    """For each element x in the array a, return the product of all elements in
    a except for x.

    Initial brute force approach. O(n^2).
    """
    products = [1] * len(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if (i != j):
                products[i] *= a[j]
    return products

def excluded_products_div(a):
    """For each element x in the array a, return the product of all elements in
    a except for x.

    More efficient approach for large arrays, by precomputing a common product and
    dividing each element. O(n).
    """
    # Precompute the total product, considering 0s
    zero_index = -1
    product = 1
    for i in range(len(a)):
        if a[i] == 0 and zero_index == -1:
            zero_index = i
        elif a[i] == 0 and zero_index != -1:
            return [0] * len(a)
        else:
            product *= a[i]
    # Compute products, considering 0s
    if zero_index != -1:
        products = [0] * len(a)
        products[zero_index] = product
        return products
    products = [1] * len(a)
    for i in range(len(a)):
            products[i] = product / a[i]
    return products

def excluded_products_bonus(a):
    """The brute force approach also satisfies the bonus. This approach is more
    efficient on larger arrays, yielding better runtime complexity by using
    memoization with tables pivoted on the left and right side around each element.
    O(n).
    """
    left_table = { -1: 1 }
    right_table = { len(a): 1 }

    def left(i):
        if i not in left_table:
            left_table[i] = a[i] * left(i - 1)
        return left_table[i]

    def right(i):
        if i not in right_table:
            right_table[i] = a[i] * right(i + 1)
        return right_table[i]

    b = [1] * len(a)
    for i in range(len(a)):
        b[i] = left(i - 1) * right(i + 1)
    return b