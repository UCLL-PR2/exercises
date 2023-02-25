import sys
sys.path.append('..')
import pytest
from movie import *
import solution
import student
import starter


@pytest.mark.parametrize('module', [solution, student])
@pytest.mark.parametrize('year', range(1950,2050))
def test_titles(module, year):
    function_name = 'movies_from_year'
    args = [year]

    if not hasattr(module, function_name):
        pytest.skip()

    imperative_function = getattr(starter, function_name)
    functional_function = getattr(module, function_name)

    imperative_result = imperative_function(movies, *args)
    functional_result = functional_function(movies, *args)

    assert functional_result == imperative_result
