__author__ = "Sean Moore"

"""
Problem:

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using
a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
"""
It's been a long time since I dealt with Monte Carlo methods, and I need to
review it before addressing the problem.
"""

import random

def estimate_pi(n):
    """Estimate pi using a Monte Carlo method with n uniformly distributed
    random samples.

    We can circumscribe a square around a unit circle and sample uniformly
    random points in the square. The ratio of points that lie in the
    circle to the total number of points approximates the ratio of the area of
    the unit circle to the area of the square.

    in_circle / in_square ~ pi*1^2 / 2^2 => pi ~ 4 * in_circle / in_square.
    A point (x, y) is within the unit circle if x^2 + y^2 < 1.
    """
    samples = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(n)]
    return (4 * 
            len([p for p in samples if p[0]*p[0] + p[1]*p[1] < 1]) /
            len(samples))

if __name__ == "__main__":
    for n in [100, 1000, 10000000]:
        print(round(estimate_pi(n), 3))