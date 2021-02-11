__author__ = "Sean Moore"

"""
This is a reservoir sampling problem with k = 1, where we can't assume we know
the size of stream ahead of time and cannot capture the entire stream at once
for sampling.

I found this to be a great resource to understand the probability involved in
my implementation, verifying uniform sampling.
https://florian.github.io/reservoir-sampling/
"""

import random

def pick_uniform(s):
    """
    Samples an element from stream s with uniform probability for the elements
    seen so far.
    """
    e = enumerate(s)
    _, sample = next(e)
    for i, x in e:
        if random.randint(0, i) == 0:
            sample = x
        yield sample
