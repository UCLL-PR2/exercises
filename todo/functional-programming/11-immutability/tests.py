import pytest
import starter
import student


def if_defined(function_name):
    return pytest.mark.skipif(function_name not in dir(student), reason=f'{function_name} is not defined')


@if_defined('remove_first')
@pytest.mark.parametrize('xs', [
    (1,),
    (1, 2),
    (1, 2, 3, 4),
    tuple([*'abcd']),
])
def test_remove_first(xs):
    function_name = 'remove_first'
    imperative = getattr(starter, function_name)
    functional = getattr(student, function_name)

    imperative_result = list(xs)
    imperative(imperative_result)

    functional_result = functional(xs)

    assert tuple(imperative_result) == functional_result


@if_defined('repeat')
@pytest.mark.parametrize('xs', [
    (),
    (1,),
    (1, 2),
    (1, 2, 3, 4),
    tuple([*'abcd']),
])
def test_repeat(xs):
    function_name = 'repeat'
    imperative = getattr(starter, function_name)
    functional = getattr(student, function_name)

    imperative_result = list(xs)
    imperative(imperative_result)

    functional_result = functional(xs)

    assert tuple(imperative_result) == functional_result


@if_defined('double')
@pytest.mark.parametrize('xs', [
    (),
    (1,),
    (1, 2),
    (1, 2, 3, 4),
    (5, 8, 4, 3, 2, 6),
])
def test_double(xs):
    function_name = 'double'
    imperative = getattr(starter, function_name)
    functional = getattr(student, function_name)

    imperative_result = list(xs)
    imperative(imperative_result)

    functional_result = functional(xs)

    assert tuple(imperative_result) == functional_result



@if_defined('swap')
@pytest.mark.parametrize('xs, i, j', (
    (xs, i, j)
    for xs in [
        (),
        (1,),
        (1, 2),
        (1, 2, 3, 4),
        (5, 8, 4, 3, 2, 6),
    ]
    for i in range(len(xs))
    for j in range(len(xs))
))
def test_swap(xs, i, j):
    function_name = 'swap'
    imperative = getattr(starter, function_name)
    functional = getattr(student, function_name)

    imperative_result = list(xs)
    imperative(imperative_result, i, j)

    functional_result = functional(xs, i, j)

    assert tuple(imperative_result) == functional_result
