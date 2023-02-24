import contextlib
import pytest
import csv
import solution
import student



@contextlib.contextmanager
def survey_data():
    with open('survey.csv') as file:
        yield csv.DictReader(file)


# @if_function_exists('age_categories')
@pytest.mark.parametrize('function_name', solution.to_be_tested_function_names)
def test_find_age_categories(function_name):
    if function_name not in dir(student):
        pytest.skip()
    extra_args = []

    with survey_data() as data:
        actual = getattr(student, function_name)(data, *extra_args)

    with survey_data() as data:
        expected = getattr(solution, function_name)(data, *extra_args)

    assert actual == expected
