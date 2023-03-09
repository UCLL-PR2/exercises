import pytest
from student import *


def if_defined(name):
    return pytest.mark.skipif(name not in globals(), reason=f'{name} not found in student module')


@if_defined('repeat_and_collect')
def test_repeat_and_collect():
    counter = 1

    def function():
        nonlocal counter
        counter *= 2
        return counter

    actual = repeat_and_collect(function, 5)
    expected = [2, 4, 8, 16, 32]

    assert actual == expected


@if_defined('collect_while')
def test_collect_while():
    counter = 5

    def function():
        nonlocal counter
        counter -= 1
        return counter

    actual = collect_while(function)
    expected = [4, 3, 2, 1, 0]

    assert actual == expected
