import pytest
import student
import solution


@pytest.mark.parametrize("xs", [
    [],
    ['a'],
    ['a', 'b', 'c'],
    ['abc', 'def', 'xyz'],
    ['abc', 'def', 'xyz', 'aaaa', 'foo'],
])
def test_function(xs):
    function_name = 'add_indices'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(xs)
    expected = solution_function(xs)

    assert expected == actual, f"Wrong result for {xs}, expected {expected}, received {actual}"
