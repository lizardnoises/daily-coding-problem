__author__ = "Sean Moore"

"""
Problem:

Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
"""
"""
Initially I look for a brute-force solution to the problem.

When approaching this problem by hand, I would iterate through each character
in the string and build a substring rooted on that character. While building
each substring, I would create and reference a set of characters that have
appeared so far in the substring. When the size of the set > k, terminate the
substring.

Next I would look for ways to optimize the solution, usually prioritizing
runtime complexity.
"""

def length_k_substring(s, k):
    """Return the length of longest substring of s with at most k distinct
    characters.
    """
    max_length = 0
    for i in range(len(s)):
        distincts = set()
        ss = ""
        for j in range(i, len(s)):
            distincts.add(s[j])
            if len(distincts) > 2:
                break
            ss += s[j]
        max_length = max(max_length, len(ss))
    return max_length