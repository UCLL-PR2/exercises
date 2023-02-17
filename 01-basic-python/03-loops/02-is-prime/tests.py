import pytest
import student
import solution


@pytest.mark.parametrize("n", range(0, 1000))
def test_function(n):
    function_name = 'is_prime'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(n)
    expected = solution_function(n)

    assert expected == actual, f"Wrong result for {n}, expected {expected}, received {actual}"
