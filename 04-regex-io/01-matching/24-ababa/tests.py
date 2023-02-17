import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '',
    'ababa',
    'xyxyx',
    'aabbaabbaa',
    'ababc',
    'babab',
    'ababax',
    'aaaaa',
    '12121',
    '23212',
])
def test_function(string):
    function_name = 'ababa'
    assert hasattr(student, function_name), f"Missing function {function_name}"

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
