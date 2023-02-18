import pytest
import student
import solution


@pytest.mark.parametrize("dictionary, value", [
    ({}, 1),
    ({'a': 1}, 1),
    ({'a': 2}, 1),
    ({'a': 1, 'b': 1}, 1),
    ({'a': 1, 'b': 2}, 1),
    ({'a': 1, 'b': 2}, 2),
    ({'a': 1, 'b': 2, 'c': 3}, 2),
    ({'a': 1, 'b': 2, 'c': 3, 'd': 2}, 2),
    ({'a': 1, 'b': 2, 'c': 3, 'd': 2}, 3),
])
def test_function(dictionary, value):
    function_name = 'keys_with_value'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(dictionary, value)
    expected = solution_function(dictionary, value)

    assert expected == actual, f"Wrong result for {(dictionary, value)}, expected {expected}, received {actual}"
