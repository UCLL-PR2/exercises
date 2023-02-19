import pytest
import student
import solution


@pytest.mark.parametrize("x", list(range(-100, 100)))
def test_function(x):
    function_name = 'square'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(x)
    expected = solution_function(x)

    assert expected == actual, f"Wrong result for {x}, expected {expected}, received {actual}"
