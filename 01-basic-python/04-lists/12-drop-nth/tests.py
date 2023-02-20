import pytest
import student
import solution


@pytest.mark.parametrize("xs, n", [
    ([1], 0),
    ([1, 2], 0),
    ([1, 2], 1),
    ([1, 2, 3], 0),
    ([1, 2, 3], 1),
    ([1, 2, 3], 2),
    (['a', 'b', 'c', 'd', 'e'], 0),
    (['a', 'b', 'c', 'd', 'e'], 1),
    (['a', 'b', 'c', 'd', 'e'], 2),
    (['a', 'b', 'c', 'd', 'e'], 3),
    (['a', 'b', 'c', 'd', 'e'], 4),
])
def test_function(xs, n):
    function_name = 'drop_nth'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(xs, n)
    expected = solution_function(xs, n)

    assert expected == actual, f"Wrong result for {(xs, n)}, expected {expected}, received {actual}"
