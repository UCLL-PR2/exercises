import pytest
import student
import solution


@pytest.mark.parametrize("string", [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Ace', 'Jack', 'Queen', 'King' ])
def test_function(string):
    function_name = 'card_value'
    assert hasattr(student, function_name), f"Missing function {function_name}"

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(string)
    expected = solution_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
