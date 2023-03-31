import pytest
import student
import solution


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
def test_indexing_with_valid_index(elts, index):
    solution_linked_list = solution.Node.from_iterable(elts)
    student_linked_list = student.Node.from_iterable(elts)
    expected = solution_linked_list[index]
    actual = student_linked_list[index]

    assert expected == actual, f'{elts}[{index}] should return {expected}'


@pytest.mark.parametrize('elts, index', [
    (
        [1, 2, 3],
        3
    ),
    (
        [1, 2, 3],
        -1
    ),
])
def test_indexing_with_invalid_index(elts, index):
    linked_list = create_linked_list(elts, student)
    with pytest.raises(IndexError):
        linked_list[index]
