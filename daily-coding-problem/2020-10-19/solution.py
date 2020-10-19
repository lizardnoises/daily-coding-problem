__author__ = "Sean Moore"

"""
This function returns a closure on a and b. When the closure is invoked with a
function argument, it will apply that function to a and b.
"""
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

"""
Returns the first element of the pair.
"""
def car(pair):
    return pair(lambda a, b: a)

"""
Returns the second element of the pair.
"""
def cdr(pair):
    return pair(lambda a, b: b)