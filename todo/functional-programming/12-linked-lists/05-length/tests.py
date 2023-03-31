import pytest
import student
import solution


@pytest.mark.parametrize('elts', [
    *(tuple(range(k)) for k in range(50)),
    ['a', 'b', 'c', 'd'],
])
def test_length(elts):
    solution_linked_list = solution.Node.from_iterable(elts)
    student_linked_list = student.Node.from_iterable(elts)
    expected = len(solution_linked_list)
    actual = len(student_linked_list)

    assert expected == actual, f'len({elts}) should return {expected}'
