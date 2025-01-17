__author__ = "Sean Moore"

"""
Problem:

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be
smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
"""
My initial thoughts here is to view the ids as a stream and the log as a
fragmented window sliding along the stream. After the Nth record, any new
records shifts the earliest record out of the log to make room. I think a
circular queue implemented with an array for random access would be an
appropriate foundation.
"""

class OrderIdLog:
    def __init__(self, n):
        self.n = n
        self.size = 0
        self.queue = [0] * n
        self.head = 0

    def record(self, order_id):
        self.queue[self.head] = order_id
        self.head += 1 % self.n
        if self.size < self.n:
            self.size += 1

    def get_last(self, i):
        assert 1 <= i <= self.size
        return self.queue[(self.head - i) % self.n]

"""
Or, if N is meant to be dynamic, a circular queue is unnecessary.
"""

class OrderIdLogDyn:
    def __init__(self):
        self.log = []
    
    def record(self, order_id):
        self.log.append(order_id)

    def get_last(self, i):
        assert 1 <= i <= len(self.log)
        return self.log[len(self.log) - i]