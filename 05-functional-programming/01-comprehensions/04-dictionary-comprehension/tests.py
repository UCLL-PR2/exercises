import sys
sys.path.append('..')
import pytest
from movie import *
import solution
import student


@pytest.mark.parametrize('movie_count', [0, 1, 5, 10, len(movies)])
def test_title_to_director(movie_count):
    function_name = 'title_to_director'

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    movie_selection = movies[:movie_count]

    solution_result = solution_function(movie_selection)
    student_result = student_function(movie_selection)

    assert student_result == solution_result


@pytest.mark.parametrize('movie_count', [0, 1, 5, 10, len(movies)])
def test_director_to_titles(movie_count):
    function_name = 'director_to_titles'

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    movie_selection = movies[:movie_count]

    solution_result = solution_function(movie_selection)
    student_result = student_function(movie_selection)

    assert student_result == solution_result
