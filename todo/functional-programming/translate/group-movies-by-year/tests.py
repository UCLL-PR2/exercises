import sys
sys.path.append('..')
import pytest
from movie import *
import solution
import student
import starter


@pytest.mark.parametrize('module', [solution, student])
def test_titles(module):
    function_name = 'group_movies_by_year'

    if not hasattr(module, function_name):
        pytest.skip()

    imperative_function = getattr(starter, function_name)
    functional_function = getattr(module, function_name)

    imperative_result = imperative_function(movies)
    functional_result = functional_function(movies)

    assert functional_result == imperative_result
