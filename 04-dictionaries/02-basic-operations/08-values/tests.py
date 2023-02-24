import pytest
import student
import solution


@pytest.mark.parametrize("dictionary", [
    {},
    {'a': 1},
    {'a': 1, 'b': 2},
    {1: 2, 2: 3, 3: 4},
])
def test_function(dictionary):
    function_name = 'values'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = sorted(student_function(dictionary))
    expected = sorted(solution_function(dictionary))

    assert expected == actual, f"Wrong result for {(dictionary)}, expected {expected}, received {actual}"
