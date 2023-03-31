import pytest
from solution import Node


@pytest.mark.parametrize('xs', [
    (1,),
    (1, 2, 3),
    (5, 4, 3, 2, 1),
    tuple([*'abcde']),
])
def test_reversed(xs):
    original = Node.from_iterable(xs)
    expected = Node.from_iterable(list(reversed(xs)))
    actual = reversed(original)

    assert expected == actual
