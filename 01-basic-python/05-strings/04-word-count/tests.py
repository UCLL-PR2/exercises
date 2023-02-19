import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    "",
    "abc",
    "abc def",
    "once upon a time",
    "a " * 1000 + "b",
])
def test_function(string):
    function_name = 'word_count'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(string)
    expected = solution_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
