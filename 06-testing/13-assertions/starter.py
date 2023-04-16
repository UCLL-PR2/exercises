def split_in_two(ns):
    middle = len(ns) // 2
    left = ns[:middle]
    right = ns[middle:]
    return (left, right)


def merge_sorted(ks, ns):
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
    return result


def merge_sort(ns):
    if len(ns) <= 1:
        result = ns
    else:
        left, right = split_in_two(ns)
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        result = merge_sorted(sorted_left, sorted_right)
    return result
