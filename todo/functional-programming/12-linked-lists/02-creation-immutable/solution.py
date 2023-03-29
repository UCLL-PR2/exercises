from linkedlist import Node


def create_linked_list(xs):
    result = None
    for x in reversed(xs):
        result = Node(x, result)
    return result
