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
The brute force approach also satisfies the bonus. This approach is more
efficient on larger arrays, yielding better runtime complexity by using
memoization with tables pivoted on the left and right side around each element.
O(n).
"""
def excluded_products_bonus(a):
    left_table = { -1: 1 }
    right_table = { len(a): 1 }
    b = [1] * len(a)
    for i in range(len(a)):
        b[i] = left(a, left_table, i - 1) * right(a, right_table, i + 1)
    return b

def left(a, table, i):
    if i not in table:
        table[i] = a[i] * left(a, table, i - 1)
    return table[i]

def right(a, table, i):
    if i not in table:
        table[i] = a[i] * right(a, table, i + 1)
    return table[i]