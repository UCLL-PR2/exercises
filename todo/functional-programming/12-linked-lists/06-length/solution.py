# Imperative
def length(linked_list):
    result = 0
    current = linked_list
    while current is not None:
        result += 1
        current = current.next
    return result


# Recursive
def length(linked_list):
    if linked_list is not None:
        return 1 + length(linked_list.next)
    else:
        return 0
