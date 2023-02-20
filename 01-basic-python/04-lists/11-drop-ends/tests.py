import pytest
import student
import solution


@pytest.mark.parametrize("xs", [
    [1, 2],
    [1, 2, 3],
    [1, 3, 2],
    [3, 2, 1],
    [2, 1, 3],
    [4, 2, 6, 5, 4, 1, 2, 7, 6, 4, 5],
])
def test_function(xs):
    function_name = 'drop_ends'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(xs)
    expected = solution_function(xs)

    assert expected == actual, f"Wrong result for {xs}, expected {expected}, received {actual}"
