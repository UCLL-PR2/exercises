import pytest
import student
import solution


@pytest.mark.parametrize("xs, ys", [
    ([], []),
    ([2], []),
    ([2], [2]),
    ([2], [1]),
    ([1, 2, 3, 4], [1]),
    ([1, 2, 3, 4], [1, 2]),
    ([1, 2, 3, 4], [1, 2, 3]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([1, 2, 3, 4], [4, 1]),
    ([1, 2, 3, 4], [4, 4, 4, 4]),
])
def test_function(xs, ys):
    function_name = 'includes'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(xs, ys)
    expected = solution_function(xs, ys)

    assert expected == actual, f"Wrong result for {(xs, ys)}, expected {expected}, received {actual}"
