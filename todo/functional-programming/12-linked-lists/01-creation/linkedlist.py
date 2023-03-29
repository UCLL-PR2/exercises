import itertools


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __iter__(self):
        current = self
        while current:
            yield current.value
            current = current.next

    def __eq__(self, other):
        if isinstance(other, Node):
            return all(x == y for x, y in itertools.zip_longest(self, other, fillvalue=object()))
        else:
            return NotImplemented
