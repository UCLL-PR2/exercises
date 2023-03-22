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
        return ns
    left, right = split_in_two(ns)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge_sorted(sorted_left, sorted_right)



import pytest
import itertools


@pytest.mark.parametrize('ns', [
    list(range(k)) for k in range(101)
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns
    assert abs(len(left) - len(right)) <= 1


@pytest.mark.parametrize('left', [
    [],
    [0, 1, 2, 3],
    [0, 2, 4, 6],
    [1, 3, 5, 7],
    [5, 5, 5],
    [3, 7, 7, 11, 15],
])
@pytest.mark.parametrize('right', [
    [],
    [0, 1, 2, 3],
    [0, 2, 4, 6],
    [1, 3, 5, 7],
    [5, 5, 5],
    [3, 7, 7, 11, 15],
])
def test_merge_sorted(left, right):
    actual = merge_sorted(left, right)
    expected = sorted(left + right)
    assert expected == actual


@pytest.mark.parametrize('expected, ns', [
    (ns, list(permutation))
    for ns in [[], [1], [1, 2], [1, 4, 4, 6], [1, 2, 2, 4, 6, 9]]
    for permutation in itertools.permutations(ns)
])
def test_merge_sort(expected, ns):
    assert merge_sort(ns) == expected
