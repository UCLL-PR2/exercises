from linkedlist import Node


def create_linked_list(xs):
    nodes = [Node(x) for x in xs]
    for i in range(1, len(nodes)):
        nodes[i-1].next = nodes[i]
    if nodes:
        return nodes[0]
    else:
        return None