__author__ = 'Sean Moore'

"""
Problem:
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there
are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no
elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""
"""
What makes this problem interesting is the need to keep track of the max value
after pop operations while requiring all operations to be constant time. My
naive approach here is to just parallel the stack with a stack of max values,
so that max operation can be 'undone' when the last value is popped.
"""

import math

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = [-math.inf]
    
    def push(self, val):
        self.stack.append(val)
        self.max_stack.append(max(val, self.max_stack[-1]))
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        self.max_stack.pop()
        return self.stack.pop()
    
    def max(self):
        if len(self.stack) == 0:
            return None
        return self.max_stack[-1]