__author__ = "Sean Moore"

"""
For each element x in the array a, return the product of all elements in
a except for x.

Initial brute force approach. O(n^2).
"""
def excluded_products(a):
    products = [1] * len(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if (i != j):
                products[i] *= a[j]
    return products

"""
For each element x in the array a, return the product of all elements in
a except for x.

More efficient approach for large arrays, by precomputing a common product and
dividing each element. O(n).
"""
def excluded_products_div(a):
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

"""
The brute force approach satisfies the bonus. There may be
an approach yielding better runtime complexity using memoization with tables
pivoted on the left and right side around each element.
"""
def excluded_products_bonus(a):
    return excluded_products(a)