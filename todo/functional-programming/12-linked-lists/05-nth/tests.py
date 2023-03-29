import pytest
import student
import solution
from linkedlist import Node


def create_linked_list(xs):
    result = None
    for x in reversed(xs):
        result = Node(x, result)
    return result



@pytest.mark.parametrize('elts, index', [
    (xs, index)
    for xs in [
        (1,),
        (1, 2, 3),
        (5, 4, 3, 2, 1),
        tuple([*'abcde']),
    ]
    for index in range(len(xs))
])
def test_nth(elts, index):
    linked_list = create_linked_list(elts)
    expected = solution.nth(linked_list, index)
    actual = student.nth(linked_list, index)

    assert expected == actual, f'{elts}[{index}] should return {expected}'
