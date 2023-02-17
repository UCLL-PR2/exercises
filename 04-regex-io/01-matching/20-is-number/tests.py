import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '',
    *'0123456789',
    '12.34',
    '12.',
    '.23',
    '8394018',
    '38209.83491',
    '1111111,1111',
    '1111111a.1111',
])
def test_function(string):
    function_name = 'is_number'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
