import sys
sys.path.append('..')
import pytest
from movie import *
import solution
import student


@pytest.mark.parametrize('movie_count', [0, 1, 5, 10, len(movies)])
def test_genres(movie_count):
    function_name = 'genres'

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    movie_selection = movies[:movie_count]

    solution_result = solution_function(movie_selection)
    student_result = student_function(movie_selection)

    assert student_result == solution_result


@pytest.mark.parametrize('movie_count', [0, 1, 5, 10, len(movies)])
def test_actors(movie_count):
    function_name = 'actors'

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    movie_selection = movies[:movie_count]

    solution_result = solution_function(movie_selection)
    student_result = student_function(movie_selection)

    assert student_result == solution_result


@pytest.mark.parametrize('xs', [
    [],
    [1, 2, 3],
    'abcd',
])
@pytest.mark.parametrize('n', range(1, 6))
def test_repeat_consecutive(xs, n):
    function_name = 'repeat_consecutive'
    args = [xs, n]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize('xs', [
    [],
    [1, 2, 3],
    'abcd',
])
@pytest.mark.parametrize('n', range(1, 6))
def test_repeat_alternating(xs, n):
    function_name = 'repeat_alternating'
    args = [xs, n]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize('values', [
    [],
    [2, 3],
    [2, 5, 9, 10, 'queen']
])
@pytest.mark.parametrize('suits', [
    [],
    ['hearts'],
    ['spades'],
    ['diamonds', 'spades'],
    ['diamonds', 'spades', 'hearts', 'clubs'],
])
def test_cards(values, suits):
    function_name = 'cards'
    args = [values, suits]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result
