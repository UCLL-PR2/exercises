import sys
sys.path.append('..')
import pytest
from movie import *
import solution
import student
import starter


@pytest.mark.parametrize('module', [solution, student])
@pytest.mark.parametrize('director', [
    'Coen Brothers',
    'Ridley Scott',
    'Christopher Nolan',
    'Sergio Leone',
    'Paul Thomas Anderson',
])
def test_titles(module, director):
    function_name = 'earliest_movie_of_director'
    args = [director]

    if not hasattr(module, function_name):
        pytest.skip()

    imperative_function = getattr(starter, function_name)
    functional_function = getattr(module, function_name)

    imperative_result = imperative_function(movies, *args)
    functional_result = functional_function(movies, *args)

    assert functional_result == imperative_result
