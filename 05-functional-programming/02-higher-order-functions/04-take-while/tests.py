import pytest
from student import *


@pytest.mark.parametrize("xs, condition, expected", [
    (
        [1, 2, 3, 4, 5, 6],
        lambda x: x < 4,
        ([1, 2, 3], [4, 5, 6])
    ),
    (
        [1, 2, 3, 4, 5, 6],
        lambda x: x < 6,
        ([1, 2, 3, 4, 5], [6])
    ),
    (
        [1, 2, 3, 4, 5],
        lambda x: x == 1,
        ([1], [2, 3, 4, 5])
    ),
    (
        [1, 1, 1, 1, 2, 3, 4, 5],
        lambda x: x == 1,
        ([1, 1, 1, 1], [2, 3, 4, 5])
    ),
    (
        [2, 3, 4, 5],
        lambda x: x == 1,
        ([], [2, 3, 4, 5])
    ),
    (
        [1, 2, 3, 4, 5],
        lambda x: x == 2,
        ([], [1, 2, 3, 4, 5])
    ),
    (
        [],
        lambda x: x == 2,
        ([], [])
    ),
    (
        [2, 2, 2],
        lambda x: x == 2,
        ([2, 2, 2], [])
    ),
])
def test_group_by(xs, condition, expected):
    actual = take_while(xs, condition)
    assert expected == actual
