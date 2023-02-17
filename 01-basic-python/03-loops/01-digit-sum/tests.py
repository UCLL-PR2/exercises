import pytest
import student
import solution


@pytest.mark.parametrize("n", [0, 1, 4, 9, 10, 19, 231, 849, 23892380, 380928390185])
def test_function(n):
    function_name = 'digit_sum'
    assert hasattr(student, function_name), f"Missing function {function_name}"

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(n)
    expected = solution_function(n)

    assert expected == actual, f"Wrong result for {n}, expected {expected}, received {actual}"
