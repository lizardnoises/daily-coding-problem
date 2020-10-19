__author__ = "Sean Moore"

import solution

def test_car():
    assert solution.car(solution.cons(3, 4)) == 3

def test_cdr():
    assert solution.cdr(solution.cons(3, 4)) == 4