# Recursive
def length(linked_list):
    if linked_list is not None:
        return 1 + length(linked_list.next)
    else:
        return 0
