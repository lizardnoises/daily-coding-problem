__author__ = "Sean Moore"

"""
Problem:

Given the root to a binary tree, implement `serialize(root)`, which serializes
the tree into a string, and `deserialize(s)`, which deserializes the string
back into the tree.

For example, given the following `Node` class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    """Serialize a binary tree into a string."""
    if not root:
        return repr(None)
    return ('Node(' +
        repr(root.val) + ',' +
        serialize(root.left) + ',' +
        serialize(root.right) + ')')

def deserialize(s):
    """Deserialize a string into a binary tree. Obviously this approach is vulnerable 
    to injection the same way that eval is.
    """
    return eval(s)