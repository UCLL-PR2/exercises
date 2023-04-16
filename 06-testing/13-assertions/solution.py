from collections import Counter


def is_sorted(ns):
    return all(x <= y for x, y in zip(ns, ns[1:]))


def contain_same_elements(xs, ys):
    return Counter(xs) == Counter(ys)


def split_in_two(ns):
    middle = len(ns) // 2
    left = ns[:middle]
    right = ns[middle:]
    assert left + right == ns
    assert abs(len(left)  - len(right)) <= 1
    return (left, right)


def merge_sorted(ks, ns):
    # Whether to use assert or exceptions can be debated over
    # Our arguments for using assert in this case:
    # * This function is meant to be used privately, and it is a bug if ks or ns are not sorted
    #   Exceptions are more "user friendly", but this function should not have any external users
    # * The check is relatively expensive to perform, so we'd like it to be turned off in release builds
    assert is_sorted(ks)
    assert is_sorted(ns)

    result = []
    i = 0
    j = 0
    while i < len(ks) and j < len(ns):
        if ks[i] < ns[j]:
            result.append(ks[i])
            i += 1
        else:
            result.append(ns[j])
            j += 1
    result.extend(ks[i:])
    result.extend(ns[j:])

    assert is_sorted(result)
    assert contain_same_elements(ks + ns, result)
    return result


def merge_sort(ns):
    if len(ns) <= 1:
        result = ns
    else:
        left, right = split_in_two(ns)
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        result = merge_sorted(sorted_left, sorted_right)

    assert is_sorted(result)
    assert contain_same_elements(result, ns)
    return result
