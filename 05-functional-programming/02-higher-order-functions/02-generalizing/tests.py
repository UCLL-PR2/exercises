import pytest
from student import *


@pytest.mark.parametrize('xs, condition, expected', [
    (
        [1, 2, 3, 4, 5],
        lambda x: x >= 3,
        3
    ),
    (
        [1, 2, 3, 4, 5],
        lambda x: x < 3,
        1
    ),
    (
        'abcdef',
        lambda x: x == 'd',
        'd'
    ),
    (
        [1, 2, 3, 4, 5],
        lambda x: x < 0,
        None
    )
])
def test_find(xs, condition, expected):
    actual = find(xs, condition)
    assert expected == actual
