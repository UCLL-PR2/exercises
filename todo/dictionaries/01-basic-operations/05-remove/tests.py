from copy import copy
import pytest
import student
import solution


@pytest.mark.parametrize("dictionary, key", [
    ({'a': 1}, 'a'),
    ({'a': 1, 'b': 2}, 'a'),
    ({'a': 1, 'b': 2}, 'b'),
])
def test_function(dictionary, key):
    function_name = 'remove'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual_dictionary = copy(dictionary)
    student_function(actual_dictionary, key)

    expected_dictionary = copy(dictionary)
    solution_function(expected_dictionary, key)

    assert expected_dictionary == actual_dictionary, f"Wrong result for {(dictionary, key)}, expected {expected_dictionary}, received {actual_dictionary}"
