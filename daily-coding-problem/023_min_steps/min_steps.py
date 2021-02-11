__author__ = 'Sean Moore'

"""
Problem:

You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you
can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the
minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down,
and right. You cannot move through walls. You cannot wrap around the edges of
the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum
number of steps required to reach the end is 7, since we would need to go
through (1, 2) because there is a wall everywhere else on the second row.
"""
"""
There are a number of path finding algorithms that could work well for this
sort of problem, including Dijkstra's and A*. This problem is specifically
simple because the edges are unweighted, so a breadth-first search will
do the job.
"""

from collections import deque

def min_steps(b, s, e):
    """Return the minimum number of steps needed to traverse the board b from
    the starting coordinate s to then ending coordinate e. Return -1 if no
    such path exists.
    """
    visited = set()
    def valid(coord):
        i, j, _ = coord
        return (0 <= i < len(b) and
                0 <= j < len(b[0]) and
                b[i][j] == False and
                (i, j) not in visited)

    q = deque([(*s, 0)])
    while q:
        i, j, steps = q.popleft()
        if (i, j) == e:
            return steps
        if (i, j) not in visited:
            visited.add((i, j))
            neighbors = ([(i, j+y, steps+1) for y in [-1, 1]] +
                         [(i+x, j, steps+1) for x in [-1, 1]])
            for neighbor in filter(valid, neighbors):
                q.append(neighbor)
    return -1