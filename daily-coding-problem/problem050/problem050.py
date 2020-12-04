__author__ = 'Sean Moore'

r'''
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an
integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
'''
'''
The tree structure makes evaluation straightforward using a post-order
traversal.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def eval_tree(root):
    '''
    Returns the evaluation of arithmetic expression represented by the given
    tree. The expression is restricted to the binary operators +, -, *, /.
    '''
    ops = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y}

    def helper(node):
        if not node.left or not node.right:
            return node.val
        left = helper(node.left)
        right = helper(node.right)
        return ops[node.val](left, right)
    
    return helper(root)