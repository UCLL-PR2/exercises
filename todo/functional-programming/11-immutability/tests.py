import pytest
import starter
import student


def if_defined(function_name):
    return pytest.mark.skipif(function_name not in dir(student), reason=f'{function_name} is not defined')


@if_defined('remove_first')
@pytest.mark.parametrize('xs', [
    [1],
    [1, 2],
    [1, 2, 3, 4],
    [*'abcd'],
])
def test_remove_first(xs):
    function_name = 'remove_first'
    expected = xs[:]
    copy = xs[:]
    getattr(starter, function_name)(expected)
    actual = getattr(student, function_name)(xs)
    assert expected == actual
    assert copy == xs


@if_defined('repeat')
@pytest.mark.parametrize('xs', [
    [],
    [1],
    [1, 2],
    [1, 2, 3, 4],
    [*'abcd'],
])
def test_repeat(xs):
    function_name = 'repeat'
    expected = xs[:]
    copy = xs[:]
    getattr(starter, function_name)(expected)
    actual = getattr(student, function_name)(xs)
    assert expected == actual
    assert copy == xs


@if_defined('double')
@pytest.mark.parametrize('xs', [
    [],
    [1],
    [1, 2],
    [1, 2, 3, 4],
    [5, 8, 4, 3, 2, 6],
])
def test_double(xs):
    function_name = 'double'
    expected = xs[:]
    copy = xs[:]
    getattr(starter, function_name)(expected)
    actual = getattr(student, function_name)(xs)
    assert expected == actual
    assert copy == xs



@if_defined('swap')
@pytest.mark.parametrize('xs, i, j', (
    (xs, i, j)
    for xs in [
        [],
        [1],
        [1, 2],
        [1, 2, 3, 4],
        [5, 8, 4, 3, 2, 6],
    ]
    for i in range(len(xs))
    for j in range(len(xs))
))
def test_swap(xs, i, j):
    function_name = 'swap'
    expected = xs[:]
    copy = xs[:]
    getattr(starter, function_name)(expected, i, j)
    actual = getattr(student, function_name)(xs, i, j)
    assert expected == actual
    assert copy == xs
