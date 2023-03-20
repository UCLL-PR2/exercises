import pytest
from student import *


@pytest.mark.parametrize("xs, key_function, expected", [
    (
        range(0, 100),
        lambda x: x % 2,
        {0: list(range(0, 100, 2)), 1: list(range(1, 100, 2))}
    ),
    (
        range(0, 100),
        lambda x: x % 3,
        {0: list(range(0, 100, 3)), 1: list(range(1, 100, 3)), 2: list(range(2, 100, 3))}
    ),
    (
        range(0, 100),
        lambda x: x % 3,
        {0: list(range(0, 100, 3)), 1: list(range(1, 100, 3)), 2: list(range(2, 100, 3))}
    ),
    (
        ['a', 'A', 'aa', 'Aa', 'aA', 'AA', 'ab', 'AB'],
        lambda x: x.lower(),
        {'a': ['a', 'A'], 'aa': ['aa', 'Aa', 'aA', 'AA'], 'ab': ['ab', 'AB'] }
    ),
    (
        ['', 'a', 'b', 'ab', 'ba', 'abc', 'xyz'],
        len,
        {0: [''], 1: ['a', 'b'], 2: ['ab', 'ba'], 3: ['abc', 'xyz']}
    )
])
def test_group_by(xs, key_function, expected):
    actual = group_by(xs, key_function)
    assert expected == actual
