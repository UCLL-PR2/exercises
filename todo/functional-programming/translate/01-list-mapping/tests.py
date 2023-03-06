import sys
sys.path.append('..')
import pytest
from movie import *
import solution
import student
import starter


@pytest.mark.parametrize('function_name', [
    'titles',
    'titles_and_years',
    'titles_and_actor_counts',
    'longest_runtime',
])
def test_titles(function_name):
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    imperative_function = getattr(starter, function_name)
    functional_solution = getattr(solution, function_name)
    functional_student = getattr(student, function_name)

    imperative_result = imperative_function(movies)
    functional_solution_result = functional_solution(movies)
    functional_student_result = functional_student(movies)

    assert functional_solution_result == imperative_result, "If this assertion fails, the solution is buggy. Should not happen"
    assert functional_student_result == imperative_result
