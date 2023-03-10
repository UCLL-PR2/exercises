import pytest
from student import merge_dictionaries
import operator


@pytest.mark.parametrize("dict1, dict2, merge_function, expected", [
    (
        {},
        {},
        lambda x, y: x,
        {}
    ),
    (
        {'a': 1},
        {'b': 2},
        lambda x, y: x,
        {'a': 1, 'b': 2}
    ),
    (
        {'a': 1},
        {'a': 2},
        lambda x, y: x + y,
        {'a': 3}
    ),
    (
        {'a': 1},
        {'a': 2},
        max,
        {'a': 2}
    ),
    (
        {'a': 1, 'b': 4},
        {'a': 2, 'c': 8},
        max,
        {'a': 2, 'b': 4, 'c': 8}
    ),
    (
        {'a': 1, 'b': 4, 'c': 5},
        {'a': 2, 'c': 8},
        max,
        {'a': 2, 'b': 4, 'c': 8}
    ),
    (
        {'a': 1, 'b': 4, 'c': 5},
        {'a': 2, 'c': 8},
        min,
        {'a': 1, 'b': 4, 'c': 5}
    ),
    (
        {'a': 5, 'b': 4, 'c': 5},
        {'a': 2, 'c': 8},
        min,
        {'a': 2, 'b': 4, 'c': 5}
    ),
    (
        {1: 'a', 2: 'b', 3: 'c'},
        {1: 'x', 2: 'b', 4: 'z'},
        operator.add,
        {1: 'ax', 2: 'bb', 3: 'c', 4: 'z'},
    ),
])
def test_merge_dictionaries(dict1, dict2, merge_function, expected):
    actual = merge_dictionaries(dict1, dict2, merge_function)
    assert expected == actual