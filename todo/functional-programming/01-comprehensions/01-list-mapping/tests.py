import sys
sys.path.append('..')
import pytest
from movie import *
import solution
import student


@pytest.mark.parametrize('function_name', [
    'titles',
    'titles_and_years',
    'titles_and_actor_counts',
])
@pytest.mark.parametrize("movie_count", [1, 2, 5, 10, len(movies)])
def test_function(function_name, movie_count):
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    movie_selection = movies[:movie_count]

    solution_result = solution_function(movie_selection)
    student_result = student_function(movie_selection)

    assert student_result == solution_result


@pytest.mark.parametrize('sentence', [
    "",
    "hello",
    "hello world",
    "This is a Test",
])
def test_reverse_words(sentence):
    function_name = 'reverse_words'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    solution_result = solution_function(sentence)
    student_result = student_function(sentence)

    assert student_result == solution_result
