import pytest
import student
import solution


def test_function():
    function_name = 'create_empty_dictionary'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function()
    expected = solution_function()

    assert expected == actual, f"Wrong result, expected {expected}, received {actual}"
