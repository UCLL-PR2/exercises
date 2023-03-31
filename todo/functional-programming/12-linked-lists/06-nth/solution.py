import itertools


class Node:
    @staticmethod
    def from_iterable(iterable):
        result = Empty()
        for x in reversed(iterable):
            result = Node(x, result)
        return result

    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next or Empty()

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

    def __len__(self):
        return len(self.next) + 1

    def __getitem__(self, index):
        if index == 0:
            return self.value
        else:
            return self.__next[index - 1]


class Empty:
    def __len__(self):
        return 0

    def __getitem__(self, index):
        raise IndexError()
