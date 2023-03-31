import pytest
import student
import solution


def create_linked_list(xs, module):
    Empty = getattr(solution, 'Empty')
    Node = getattr(solution, 'Node')
    result = Empty()
    for x in reversed(xs):
        result = Node(x, result)
    return result


@pytest.mark.parametrize('elts', [
    *(tuple(range(k)) for k in range(50)),
    ['a', 'b', 'c', 'd'],
])
def test_length(elts):
    solution_linked_list = create_linked_list(elts, solution)
    student_linked_list = create_linked_list(elts, student)
    expected = len(solution_linked_list)
    actual = len(student_linked_list)

    assert expected == actual, f'len({elts}) should return {expected}'
