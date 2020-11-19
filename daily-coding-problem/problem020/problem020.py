__author__ = "Sean Moore"

"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the
intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the
node with value 8.

In this example, assume nodes with the same value are the exact same node
objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and
constant space.

---

The lists are not ordered, so my initial thought is to maintian a set while
marching through the two lists, stopping when a duplicate is found. But this
approach doesn't use constant space.

Because there are no cycles and the lists do not diverge at any point, we know
that any difference in length of the two lists must occur before the lists
intersect. We can calculate the lengths of the linked lists in O(M + N) time
and then traverse the longer list until the remaining lengths are equal. Then
we can traverse both lists in parallel until the intersecting node is found.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return '{} -> {}'.format(self.value, repr(self.next))

def find_intersection(node1, node2):
    """Returns the intersecting node in linked lists a and b."""
    def length(node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count
    def skip(node, n):
        for _ in range(n):
            node = node.next
        return node
    node1_len = length(node1)
    node2_len = length(node2)
    diff = abs(node1_len - node2_len)
    if node1_len > node2_len:
        node1 = skip(node1, diff)
    else:
        node2 = skip(node2, diff)
    while node1 and node2 and node1 != node2:
        node1 = node1.next
        node2 = node2.next
    if node1 == node2:
        return node1
    return None