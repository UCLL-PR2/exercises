import pytest
import student
import solution


@pytest.mark.parametrize("xs", [
    [],
    [1],
    [1, 2],
    [1, 1],
    [1, 1, 2, 2, 3, 3],
    [1, 2, 3, 2, 1],
    [1, 2, 3, 4, 5, 6],
    [1, 5, 2, 3, 6, 4, 2, 6, 1, 4, 7, 9, 0, 4, 4, 4]
])

def test_functionality(xs):
    function_name = 'remove_duplicates'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(xs)
    expected = solution_function(xs)

    assert expected == actual, f"Wrong result for {xs}, expected {expected}, received {actual}"



@pytest.mark.timeout(2)
def test_speed():
    function_name = 'remove_duplicates'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    xs = [
        x
        for x in range(1, 10000)
        for _ in range(1000)
    ]

    assert getattr(student, function_name)(xs)
