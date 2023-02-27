import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    "",
    "a",
    "aa",
    "b",
])
def test_function(string):
    function_name = 'equals_a'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
