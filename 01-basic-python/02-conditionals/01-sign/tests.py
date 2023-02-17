import pytest
import student
import solution


@pytest.mark.parametrize("n", list(range(-100, 100)))
def test_function(n):
    function_name = 'sign'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(n=n)
    expected = solution_function(n=n)

    assert expected == actual, f"Wrong result for {n}, expected {expected}, received {actual}"
