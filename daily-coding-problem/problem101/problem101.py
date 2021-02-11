"""
Given an even number (greater than 2), return two prime numbers whose sum will
be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically
smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with
c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""

from typing import List, Tuple

def sieve(n: int) -> List[bool]:
    """Return a list bools indicating if each index, from 0 through n,
    is prime.
    """
    is_prime = [True] * n
    is_prime[0], is_prime[1] = False, False
    i = 2
    while i * i <= n:
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
        i += 1
    return is_prime

def prime_sum(n: int) -> Tuple[int, int]:
    """Return two prime numbers whose sum is equal to n.
    A solution will always be found for an integer n > 2.
    """
    if not isinstance(n, int):
        raise TypeError()
    if n <= 2:
        raise ValueError()
    is_prime = sieve(n)
    for i in range(2, n/2+1):
        if is_prime[i] and is_prime[n - i]:
            return (i, n-i)