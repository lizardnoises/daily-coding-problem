__author__ = "Sean Moore"

"""
Problem:

Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
"""
My initial thought is a greedy approach maximizing the size of each set of
non-overlapping intervals.
"""

def find_min_num_rooms(lectures):
    """Return the minimum number of classrooms needed to support all given
    lecture intervals. Code is a little more convoluted than a more naive
    approach to achieve O(n log n) time complexity instead of O(n^2). A linked
    list could be used instead to simplify things.
    """
    if not lectures:
        return 0

    a = sorted(lectures, key=lambda x: x[1])
    b = []
    room_count = 1
    i = 0
    while True:
        for j in range(1, len(a)):
            if a[i][1] > a[j][0]:
                b.append(a[j])
            else:
                i = j
        if len(b) == 0:
            break
        room_count += 1
        if len(b) == 1:
            break
        c = a
        a = b
        b = c
        b.clear()
    return room_count