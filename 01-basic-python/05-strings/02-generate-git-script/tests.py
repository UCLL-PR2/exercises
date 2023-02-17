import pytest
import student
import solution


@pytest.mark.parametrize("id", [
    'x',
    'xyz',
    'abcdef'
])
def test_function(id):
    function_name = 'generate_git_script'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(id)
    expected = solution_function(id)

    assert expected == actual, f"Wrong result for {id}, expected {expected}, received {actual}"
