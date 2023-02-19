import pytest
import student
import solution


@pytest.mark.parametrize("x, lower, upper", [
    (x, lower, upper)
    for x in [-5, 0, 1, 3]
    for lower in [-6, 4, 1, 3, 8]
    for upper in [-6, 4, 1, 3, 8]
])
def test_function(x, lower, upper):
    function_name = 'between'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(x=x, lower=lower, upper=upper)
    expected = solution_function(x=x, lower=lower, upper=upper)

    assert expected == actual, f"Wrong result for x={x}, lower={lower}, upper={upper}, expected {expected}, received {actual}"
