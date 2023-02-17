import pytest
import student
import solution


@pytest.mark.parametrize("d1, d2", [
    ({}, {}),
    ({1: 1}, {2: 2}),
    ({1: 1}, {1: 2}),
    ({'a': 1, 'b': 2, 'c': 3}, {'c': 33, 'd': 44, 'e': 55}),
])
def test_function(d1, d2):
    function_name = 'merge_dicts'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(d1, d2)
    expected = solution_function(d1, d2)

    assert expected == actual, f"Wrong result for {(d1, d2)}, expected {expected}, received {actual}"
