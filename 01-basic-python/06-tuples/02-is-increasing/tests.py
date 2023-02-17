import pytest
import student
import solution


@pytest.mark.parametrize("ns", [
    [],
    [1],
    [1, 2],
    [1, 2, 2, 4, 6, 6, 10],
    [2, 1],
    [1, 2, 3, 4, 5, 4, 6],
])
def test_function(ns):
    function_name = 'is_increasing'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(ns)
    expected = solution_function(ns)

    assert expected == actual, f"Wrong result for {ns}, expected {expected}, received {actual}"
