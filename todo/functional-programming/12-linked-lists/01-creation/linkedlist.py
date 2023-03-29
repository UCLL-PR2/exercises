class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.value, self.next) == (other.value, other.next)
        else:
            return NotImplemented
