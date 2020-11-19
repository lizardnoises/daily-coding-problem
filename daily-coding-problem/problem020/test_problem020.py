__author__ = "Sean Moore"

import pytest
from problem020 import *

def test_find_intersection():
    intersection = Node(8, Node(10))
    ll1 = Node(3, Node(7, intersection))
    ll2 = Node(99, Node(1, intersection))
    assert find_intersection(ll1, ll2) == intersection