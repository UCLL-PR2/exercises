from linkedlist import Node


def create_linked_list(xs):
    if len(xs) == 0:
        return None
    head, *tail = xs
    return Node(head, create_linked_list(tail))
