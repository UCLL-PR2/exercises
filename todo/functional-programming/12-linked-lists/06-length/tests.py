import pytest
import student
import solution
from linkedlist import Node


def create_linked_list(xs):
    result = None
    for x in reversed(xs):
        result = Node(x, result)
    return result


@pytest.mark.parametrize('elts', [
    *(tuple(range(k)) for k in range(50)),
    ['a', 'b', 'c', 'd'],
])
def test_length(elts):
    linked_list = create_linked_list(elts)
    expected = solution.length(linked_list)
    actual = student.length(linked_list)

    assert expected == actual, f'length({elts}) should return {expected}'
