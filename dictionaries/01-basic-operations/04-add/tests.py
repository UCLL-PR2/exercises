from copy import copy
import pytest
import student
import solution


@pytest.mark.parametrize("dictionary, key, value", [
    ({}, 'a', 1),
    ({'a': 1}, 'a', 2),
    ({'a': 1}, 'a', 2),
])
def test_function(dictionary, key, value):
    function_name = 'add'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual_dictionary = copy(dictionary)
    student_function(actual_dictionary, key, value)

    expected_dictionary = copy(dictionary)
    solution_function(expected_dictionary, key, value)

    assert expected_dictionary == actual_dictionary, f"Wrong result for {(dictionary, key, value)}, expected {expected_dictionary}, received {actual_dictionary}"
