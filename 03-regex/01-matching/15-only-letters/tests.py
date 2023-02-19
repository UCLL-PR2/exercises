import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '',
    *'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'abc',
    'ABC',
    'ab cd',
    'aBcD',
    '163',
])
def test_function(string):
    function_name = 'only_letters'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
