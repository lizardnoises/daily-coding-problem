__author__ = "Sean Moore"

"""
Problem:

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the
first and last element of that pair. For example, `car(cons(3, 4))` returns
`3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement `car` and `cdr`.
"""

def cons(a, b):
    """Return a closure on a and b. When the closure is invoked with a
    function argument, apply that function to a and b.
    """
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    """Return the first element of the pair."""
    return pair(lambda a, b: a)

def cdr(pair):
    """Return the second element of the pair."""
    return pair(lambda a, b: b)