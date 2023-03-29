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
@pytest.mark.parametrize('converter, converter_name', [
    (lambda xs: tuple(xs), 'tuple'),
    (lambda xs: list(xs), 'list'),
])
def test_create_linked_list(xs, converter, converter_name):
    expected = solution.create_linked_list(converter(xs))
    actual = student.create_linked_list(converter(xs))

    assert expected == actual, f'Failed when {xs} was passed as {converter_name}'
