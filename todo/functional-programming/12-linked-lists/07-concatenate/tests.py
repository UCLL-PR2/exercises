import pytest
from student import Node


@pytest.mark.parametrize('xs', [
    (1,),
    (1, 2, 3),
    (5, 4, 3, 2, 1),
    tuple([*'abcde']),
])
@pytest.mark.parametrize('ys', [
    (1,),
    (1, 2, 3),
    (5, 4, 3, 2, 1),
    tuple([*'abcde']),
])
def test_concatenation(xs, ys):
    linked_xs = Node.from_iterable(xs)
    linked_ys = Node.from_iterable(ys)
    expected = Node.from_iterable(list(xs) + list(ys))
    actual = linked_xs + linked_ys

    assert expected == actual


def test_concatenation_reuses_list():
    xs = Node.from_iterable([1])
    ys = Node.from_iterable([2, 3])
    zs = xs + ys

    assert zs.next is ys