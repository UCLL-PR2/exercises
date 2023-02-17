import pytest
import student
import solution


@pytest.mark.parametrize("eggs, butter, flour", [
    (0, 0, 0),
    (10, 0, 0),
    (10, 250, 0),
    (10, 250, 250),
    (10, 250, 500),
    (10, 1000, 500),
    (18, 1000, 800),
])
def test_function(eggs, butter, flour):
    function_name = 'cakes'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(eggs=eggs, butter=butter, flour=flour)
    expected = solution_function(eggs=eggs, butter=butter, flour=flour)

    assert expected == actual, f"Wrong result for eggs={eggs}, butter={butter}, flour={flour}, expected {expected}, received {actual}"
