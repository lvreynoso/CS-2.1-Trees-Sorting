#!python

from binaryheap import BinaryMinHeap


class PriorityQueue(object):
    """PriorityQueue: a partially ordered queue with methods to enqueue items
    in priority order and to access and dequeue its highest priority item.
    Item pairs are stored in a binary min heap for its efficient operations."""

    def __init__(self):
        """Initialize this priority queue."""
        # Initialize new binary min heap to store items in this priority queue
        self.heap = BinaryMinHeap()

    def __repr__(self):
        """Return a string representation of this priority queue."""
        return 'PriorityQueue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this priority queue is empty, or False otherwise."""
        return self.heap.is_empty()

    def length(self):
        """Return the number of items in this priority queue."""
        return self.heap.size()

    def enqueue(self, item, priority):
        """Insert the given item into this priority queue in order according to
        the given priority."""
        # Insert given item into heap in order according to given priority
        self.heap.insert((priority, item))

    def front(self):
        """Return the item at the front of this priority queue without removing
        it, or None if this priority queue is empty."""
        if self.length() == 0:
            return None
        # Return minimum item from heap
        return self.heap.get_min()[1]

    def dequeue(self):
        """Remove and return the item at the front of this priority queue,
        or raise ValueError if this priority queue is empty."""
        if self.length() == 0:
            raise ValueError('Priority queue is empty and has no front item')
        # Remove and return minimum item from heap
        return self.heap.delete_min()[1]

    def push_pop(self, item, priority):
        """Remove and return the item at the front of this priority queue,
        and insert the given item in order according to the given priority.
        This method is more efficient than calling dequeue and then enqueue."""
        if self.length() == 0:
            raise ValueError('Priority queue is empty and has no front item')
        # Replace and return minimum item from heap
        return self.heap.replace_min((priority, item))[1]


def test_priority_queue():
    pq = PriorityQueue()
    import random
    min_unicode = ord('¡')
    max_unicode = ord('ʯ')
    jumbled = [random.randint(min_unicode, max_unicode) for _ in range(50)]
    tests = map(lambda x: (chr(x), x), jumbled)
    for test in tests:
        print(f'enqueing {test}')
        pq.enqueue(test[0], test[1])

    print(repr(pq))

    assert pq.front() == chr(min(jumbled))
    unjumbled = sorted(jumbled)
    for priority in unjumbled:
        assert chr(priority) == pq.dequeue()

if __name__ == '__main__':
    test_priority_queue()
