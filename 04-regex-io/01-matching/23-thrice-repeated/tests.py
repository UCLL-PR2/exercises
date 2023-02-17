import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '',
    'a',
    'aa',
    'aaa',
    'abab',
    'ababab',
    '123123',
    '123123123',
    '1111',
    '123123123123',
    '111111',
    '  ',
    '   ',
])
def test_function(string):
    function_name = 'thrice_repeated'
    assert hasattr(student, function_name), f"Missing function {function_name}"

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
