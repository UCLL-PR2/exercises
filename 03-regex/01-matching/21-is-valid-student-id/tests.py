import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '',
    'r1234567',
    'r123456',
    'r12345678',
    's12345678',
    's1234567',
    's123456',
    'q1234567',
    'R1234567',
    'R123456',
    'R12345678',
    'S12345678',
    'S1234567',
    'S123456',
    'Q1234567',
    ' r1234567 ',
    'r4545458',
    'rabcdefg',
])
def test_function(string):
    function_name = 'is_valid_student_id'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
