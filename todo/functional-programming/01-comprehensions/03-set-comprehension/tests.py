import sys
sys.path.append('..')
import pytest
from movie import *
import solution
import student


@pytest.mark.parametrize('movie_count', [0, 1, 5, 10, len(movies)])
def test_directors(movie_count):
    function_name = 'directors'

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    movie_selection = movies[:movie_count]

    solution_result = solution_function(movie_selection)
    student_result = student_function(movie_selection)

    assert student_result == solution_result


@pytest.mark.parametrize('xs', [[], [1], [1, 2, 3], [2], [2, 3, 4]])
@pytest.mark.parametrize('ys', [[], [1], [1, 2, 3], [2], [2, 3, 4]])
def test_common_elements(xs, ys):
    function_name = 'common_elements'
    args = [xs, ys]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result
