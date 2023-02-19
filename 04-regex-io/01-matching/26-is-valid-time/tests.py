import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '',
    '00:00:00',
    '00:00:00.000',
    '12:34:56.888',
    '2:34:56.888',
    '123:34:56.888',
    '12:4:56.888',
    '12:345:56.888',
    '12:34:6.888',
    '12:34:567.888',
    '12:34:56.88',
    '12:34:56.8888',
    'ab:00:00',
])
def test_function(string):
    function_name = 'is_valid_time'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
