import pytest
import student
import solution


@pytest.mark.parametrize('ns, target', [
    *[([1], target) for target in range(0, 10)],
    *[([1, 2], target) for target in range(0, 10)],
    *[([1, 2, 3], target) for target in range(0, 10)],
    *[([1, 2, 4, 8], target) for target in range(0, 50)],
    *[([2, 5, 19], target) for target in range(0, 50)],
    *[([1, 2, 3, 8], target) for target in range(0, 50)],
    *[([1, 2, 2, 3, 3, 3, 8, 8], target) for target in range(0, 50)],
])
def test_function(ns, target):
    function_name = 'target_sum'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(ns=ns, target=target)
    expected = solution_function(ns=ns, target=target)

    assert expected == actual, f"Wrong result for {(ns, target)}, expected {expected}, received {actual}"
