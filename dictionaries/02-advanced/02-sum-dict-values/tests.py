import pytest
import student
import solution


@pytest.mark.parametrize("dictionary", [
    {},
    {'a': 1},
    {'a': 1, 'b': 2},
    {'a': 4, 'b': 2, 'c': 8},
])
def test_function(dictionary):
    function_name = 'sum_dict_values'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(dictionary)
    expected = solution_function(dictionary)

    assert expected == actual, f"Wrong result for {dictionary}, expected {expected}, received {actual}"
