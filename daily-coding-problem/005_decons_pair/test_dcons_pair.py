__author__ = "Sean Moore"

from decons_pair import *

def test_car():
    assert car(cons(3, 4)) == 3

def test_cdr():
    assert cdr(cons(3, 4)) == 4