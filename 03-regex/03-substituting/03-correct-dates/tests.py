import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '1/2/3',
    '12/11/2019',
    '12/11/2019 6/7/1899',
    '12/11/2019 fjklfjl 6/7/1899',
])
def test_function(string):
    function_name = 'correct_dates'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(string)
    expected = solution_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
