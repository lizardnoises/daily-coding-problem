__author__ = "Sean Moore"

"""
Problem #33 [Easy]
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two
middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
print out:

2
1.5
2
3.5
2
2
2

---

To calculate the median of numbers seen so far, those numbers need to be
collected. That means we need to assume that we have enough space to store the
entire stream in the most general case. This solution makes that assumption.
If we maintain a sorted aggregation on the stream, then the median can be
calculated just by using the middle one or two numbers like this:

median = middle value if odd
         average of middle values if even.

So ideally, we need to be able to access the two middle elements efficently
each time an element is added to the collection, and also keep the collection
sorted. Using insertion sort on an array could work, but the runtime complexity
would be very poor with O(n^2). A more efficient approach could use two heaps,
one max heap of values smaller than the median and one min heap of values
equal to or larger than the median. In the odd case, pick the top element of
the min heap. In the even case, average the top elements of both heaps. Keep
the heaps balanced by poping and pushing to ensure the middle elements stay
on top. Insertion on a heap is O(log n).
"""

import heapq

def running_median(number_stream):
    left = [] # numbers less than the running median
    right = [] # numbers greater or equal to the running median
    for x in number_stream:
        # add the number
        if len(right) == 0 or x >= right[0]:
            heapq.heappush(right, x)
        else:
            heapq.heappush(left, -x)
        # balance the heaps
        if len(left) > len(right):
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left) + 1:
            heapq.heappush(left, -heapq.heappop(right))
        # calculate the median
        if (len(left) + len(right)) % 2 == 0:
            median = (-left[0] + right[0]) / 2.0
        else:
            median = right[0]
        yield median

def list_medians(numbers):
    return [median for median in running_median(numbers)]

def print_medians(numbers):
    for median in running_median(numbers):
        print(median)