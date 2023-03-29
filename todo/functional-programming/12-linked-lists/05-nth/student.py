def nth(linked_list, index):
    current = linked_list
    for _ in range(index):
        current = current.next
    return current.value
