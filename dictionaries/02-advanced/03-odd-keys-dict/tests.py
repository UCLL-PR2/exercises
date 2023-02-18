import pytest
import student
import solution


@pytest.mark.parametrize("dictionary", [
    {},
    {0: 'a'},
    {1: 'a'},
    {1: 'a', 2: 'b'},
    {1: 'a', 2: 'b', 3: 'c'},
    {1: 'a', 2: 'b', 3: 'c', 4: 'd'},
    {1: 'a', 2: 'x', 3: 'z', 4: 'y'},
    {111: 111, 555: 555, 444: 444},
])
def test_function(dictionary):
    function_name = 'odd_keys_dict'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(dictionary)
    expected = solution_function(dictionary)

    assert expected == actual, f"Wrong result for {dictionary}, expected {expected}, received {actual}"
