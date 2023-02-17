import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '',
    'a@ucll.be',
    'a.b@ucll.be',
    'a@student.ucll.be',
    '1@student.ucll.be',
    'a.b@student.ucll.be',
    'a1.b@student.ucll.be',
    '1.b@student.ucll.be',
    '1.5b@student.ucll.be',
    'abc.def@gmail.com',
    'abc.def ucll.be',
    '....@ucll.be',
])
def test_function(string):
    function_name = 'is_valid_email_address'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
