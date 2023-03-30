# Imperative
def nth(linked_list, index):
    current = linked_list
    for _ in range(index):
        current = current.next
    return current.value


# Recursive
def nth_recursive(linked_list, index):
    if index == 0:
        return linked_list.value
    else:
        return nth(linked_list.next, index - 1)
