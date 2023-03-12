import pytest
from student import PadZip


@pytest.mark.parametrize('left, right, expected', [
    (
        [],
        [],
        [],
    ),
    (
        'a',
        [],
        [('a', None)],
    ),
    (
        'ab',
        [],
        [('a', None), ('b', None)],
    ),
    (
        [],
        'a',
        [(None, 'a')],
    ),
    (
        [],
        'ab',
        [(None, 'a'), (None, 'b')],
    ),
    (
        [1],
        'a',
        [(1, 'a')],
    ),
    (
        [1, 2, 3],
        'a',
        [(1, 'a'), (2, None), (3, None)],
    ),
    (
        [1, 2, 3],
        'abcd',
        [(1, 'a'), (2, 'b'), (3, 'c'), (None, 'd')],
    ),
])
def test_padzip_with_default_padding(left, right, expected):
    actual = list(iter(PadZip(left, right)))
    assert expected == actual


@pytest.mark.parametrize('left, right, padding, expected', [
    (
        [],
        [],
        ...,
        [],
    ),
    (
        'a',
        [],
        ...,
        [('a', ...)],
    ),
    (
        'ab',
        [],
        ...,
        [('a', ...), ('b', ...)],
    ),
    (
        [],
        'a',
        'x',
        [('x', 'a')],
    ),
    (
        [],
        'ab',
        0,
        [(0, 'a'), (0, 'b')],
    ),
    (
        [1],
        'a',
        'padding',
        [(1, 'a')],
    ),
    (
        [1, 2, 3],
        'a',
        True,
        [(1, 'a'), (2, True), (3, True)],
    ),
    (
        [1, 2, 3],
        'abcd',
        False,
        [(1, 'a'), (2, 'b'), (3, 'c'), (False, 'd')],
    ),
])
def test_padzip_with_specified_padding(left, right, padding, expected):
    actual = list(PadZip(left, right, padding=padding))
    assert expected == actual


def test_padzip_is_single_use():
    xs = PadZip('a', 'x')
    assert list(xs) == [('a', 'x')]
    assert list(xs) == []
