import pytest
import student
import solution


@pytest.mark.parametrize('xs', [
    (),
    (1,),
    (1, 2, 3),
    (5, 4, 3, 2, 1),
    tuple([*'abcde']),
])
def test_create_list(xs):
    expected = solution.create_linked_list(iter(xs))
    actual = student.create_linked_list(iter(xs))

    assert expected == actual
