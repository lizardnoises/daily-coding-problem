__author__ = "Sean Moore"

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Serializes a binary tree into a string.
"""
def serialize(root):
    if not root:
        return repr(None)
    return ('Node(' +
        repr(root.val) + ',' +
        serialize(root.left) + ',' +
        serialize(root.right) + ')')

"""
Deserializes a string into a binary tree. Obviously this approach is vulnerable 
to injection the same way that eval is.
"""
def deserialize(s):
    return eval(s)