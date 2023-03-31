import itertools


class Node:
    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next

    @property
    def value(self):
        return self.__value

    @property
    def next(self):
        return self.__next

    def __eq__(self, other):
        if isinstance(other, Node):
            return all(x == y for x, y in itertools.zip_longest(self, other, fillvalue=object()))
        else:
            return NotImplemented


class Empty:
    pass
