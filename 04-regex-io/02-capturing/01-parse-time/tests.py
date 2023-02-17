import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '00:00:00',
    '12:34:56',
    '12:34:56.000',
    '12:34:56.001',
    '12:34:56.491',
    '21:51:48.111',
    '',
    '::',
    '0:00:00',
    '00:0:00',
    '00:00:0',
    '00:00:00.1',
    'aa:bb:cc',
])
def test_function(string):
    function_name = 'parse_time'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(string)
    expected = solution_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
