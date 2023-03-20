import pytest
from student import *


@pytest.mark.parametrize("xs, condition, expected", [
    (
        [1, 2, 3, 4, 5, 6],
        lambda x: x % 2 == 0,
        [1, 3, 5]
    ),
    (
        [-1, 1, -2, -3, 3, 4, 5],
        lambda x: x < 0,
        [0, 2, 3]
    ),
    (
        [-1, 1, -2, -3, 3, 4, 5],
        lambda x: x > 0,
        [1, 4, 5, 6]
    ),
])
def test_indices_of(xs, condition, expected):
    actual = indices_of(xs, condition)
    assert expected == actual
