import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    "",
    "abc",
    "xyz",
    "abcxyz",
    "xyzabc",
    "axyz",
    "axbc",
    "axbycz",
])
def test_function(string):
    function_name = 'abc_or_xyz'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
