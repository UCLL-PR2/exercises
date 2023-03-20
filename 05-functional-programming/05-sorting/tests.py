import pytest
import solution
import student


def if_defined(name):
    return pytest.mark.skipif(name not in dir(student), reason=f'{name} not defined in student module')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@if_defined('sort_by_age')
@pytest.mark.parametrize("people", [
    [],
    [
        Person('John', 18),
        Person('Peter', 20),
        Person('Sarah', 19),
    ],
    [
        Person('John', 18),
        Person('Peter', 42),
        Person('Sarah', 19),
        Person('Kim', 17),
        Person('Chris', 35),
    ],
])
def test_sort_by_age(people):
    function_name = 'sort_by_age'
    expected = getattr(solution, function_name)(people)
    actual = getattr(student, function_name)(people)
    assert expected == actual


@if_defined('sort_by_decreasing_age')
@pytest.mark.parametrize("people", [
    [],
    [
        Person('John', 18),
        Person('Peter', 20),
        Person('Sarah', 19),
    ],
    [
        Person('John', 18),
        Person('Peter', 42),
        Person('Sarah', 19),
        Person('Kim', 17),
        Person('Chris', 35),
    ],
])
def test_sort_by_decreasing_age(people):
    function_name = 'sort_by_decreasing_age'
    expected = getattr(solution, function_name)(people)
    actual = getattr(student, function_name)(people)
    assert expected == actual


@if_defined('sort_by_name')
@pytest.mark.parametrize("people", [
    [],
    [
        Person('John', 18),
        Person('Peter', 20),
        Person('Sarah', 19),
    ],
    [
        Person('John', 18),
        Person('Peter', 42),
        Person('Sarah', 19),
        Person('Kim', 17),
        Person('Chris', 35),
    ],
])
def test_sort_by_name(people):
    function_name = 'sort_by_name'
    expected = getattr(solution, function_name)(people)
    actual = getattr(student, function_name)(people)
    assert expected == actual


@if_defined('sort_by_name_then_age')
@pytest.mark.parametrize("people", [
    [],
    [
        Person('John', 18),
        Person('Sarah', 19),
        Person('Peter', 19),
        Person('John', 20),
    ],
    [
        Person('John', 18),
        Person('Sarah', 19),
        Person('Peter', 19),
        Person('John', 20),
        Person('Kim', 17),
        Person('Kim', 18),
        Person('Kim', 19),
    ],
])
def test_sort_by_name_then_age(people):
    function_name = 'test_sort_by_name_then_age'
    expected = getattr(solution, function_name)(people)
    actual = getattr(student, function_name)(people)
    assert expected == actual


@if_defined('sort_by_name_then_decreasing_age')
@pytest.mark.parametrize("people", [
    [],
    [
        Person('John', 18),
        Person('Sarah', 19),
        Person('Peter', 19),
        Person('John', 20),
    ],
    [
        Person('John', 18),
        Person('Sarah', 19),
        Person('Peter', 19),
        Person('John', 20),
        Person('Kim', 17),
        Person('Kim', 18),
        Person('Kim', 19),
    ],
])
def test_sort_by_name_then_decreasing_age(people):
    function_name = 'sort_by_name_then_decreasing_age'
    expected = getattr(solution, function_name)(people)
    actual = getattr(student, function_name)(people)
    assert expected == actual
