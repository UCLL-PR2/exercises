import pytest
import student
import solution


@pytest.mark.parametrize("one, two, five, goal", [
    (0, 0, 0, 0),
    (0, 0, 0, 1),
    (1, 0, 0, 1),
    (1, 0, 0, 2),
    (2, 0, 0, 2),
    (0, 1, 0, 2),
    (0, 1, 0, 5),
    (0, 0, 1, 5),
    (2, 0, 1, 5),
    (2, 0, 1, 6),
    (2, 0, 1, 7),
    (2, 0, 1, 8),
    (2, 1, 1, 8),
    (0, 0, 1, 4),
    (0, 1, 1, 6),
])
def test_function(one, two, five, goal):
    function_name = 'coins'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(one=one, two=two, five=five, goal=goal)
    expected = solution_function(one=one, two=two, five=five, goal=goal)

    assert expected == actual, f"Wrong result for {(one, two, five, goal)}, expected {expected}, received {actual}"
