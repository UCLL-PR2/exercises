from linkedlist import Node


def replace_head(linked_list, new_value):
    return Node(new_value, linked_list.next)
