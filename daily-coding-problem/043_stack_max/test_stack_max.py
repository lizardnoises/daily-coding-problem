__author__ = 'Sean Moore'

import pytest
from stack_max import Stack

@pytest.mark.parametrize('input', [
    (('push',1),('push',2),('max',2),('pop',2),('max',1),('pop',1),
     ('pop',None))
])
def test_stack(input):
    stack = Stack()
    for op, val in input:
        if op == 'push':
            stack.push(val)
        elif op == 'pop':
            top = stack.pop()
            assert top == val
        elif op == 'max':
            max_val = stack.max()
            assert max_val == val