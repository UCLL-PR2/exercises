import pytest
import student
import solution
from linkedlist import Node


def create_linked_list(xs):
    result = None
    for x in reversed(xs):
        result = Node(x, result)
    return result



@pytest.mark.parametrize('linked_list', [
    create_linked_list(xs)
    for xs in [
        (1,),
        (1, 2, 3),
        (5, 4, 3, 2, 1),
        tuple([*'abcde']),
    ]
])
@pytest.mark.parametrize('new_value', [
    1,
    5,
    True,
    'xyz',
])
def test_replace_head(linked_list, new_value):
    expected = solution.replace_head(linked_list, new_value)
    actual = student.replace_head(linked_list, new_value)

    assert expected == actual
