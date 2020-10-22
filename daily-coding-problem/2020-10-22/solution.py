__author__ = "Sean Moore"

"""
Every leaf node counts as a unival subtree, and every node with only children
that are unival subtree with the same value is a unival subtree. So we could
recursively traverse the left and right subtrees of each node and compare their
subtrees to evaluate the current root node.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root):
    """
    Returns the number of unival subtrees within the given tree.
    """
    def helper(root):
        if not root:
            return 0, True
        left_count, left_is_unival = helper(root.left)
        right_count, right_is_unival = helper(root.right)
        count = left_count + right_count
        if (    not left_is_unival or
                not right_is_unival or
                root.left and root.left.val != root.val or
                root.right and root.right.val != root.val ):
            return count, False
        return count + 1, True
        
    count, _ = helper(root)
    return count