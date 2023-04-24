import sys
sys.path.append('..')
import pytest
from movie import *
import solution
import student


def test_titles():
    module = student
    function_name = 'group_movies_by_year'

    if not hasattr(module, function_name):
        pytest.skip()

    reference_function = getattr(solution, function_name)
    actual_function = getattr(module, function_name)

    reference_result = reference_function(movies)
    actual_result = actual_function(movies)

    assert actual_result == reference_result
