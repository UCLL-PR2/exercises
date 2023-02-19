import pytest
import student
import solution


@pytest.mark.parametrize("parts", [
    [],
    ['a'],
    ['a', 'b', 'c'],
    ['abc', 'def', 'xyz'],
    ['abc', 'def', 'xyz', 'aaaa', 'foo'],
])
def test_function(parts):
    function_name = 'make_path'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(parts)
    expected = solution_function(parts)

    assert expected == actual, f"Wrong result for {parts}, expected {expected}, received {actual}"
