import pytest
import student
import solution


@pytest.mark.parametrize("keys, values", [
    ([], []),
    (['a'], [1]),
    (['a', 'b'], [1, 2]),
    (['a', 'b', 'c'], [1, 2, 3]),
    (['a', 'b', 'c'], ['x', 'y', 'z']),
])
def test_function(keys, values):
    function_name = 'create_dictionary'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(keys, values)
    expected = solution_function(keys, values)

    assert expected == actual, f"Wrong result for {(keys, values)}, expected {expected}, received {actual}"
