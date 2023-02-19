import pytest
import student
import solution


@pytest.mark.parametrize("hours", [0, 1, 4, 10, 19, 23])
@pytest.mark.parametrize("minutes", [0, 9, 15, 59])
@pytest.mark.parametrize("seconds", [0, 9, 15, 59])
def test_function(hours, minutes, seconds):
    function_name = 'format_time'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(hours=hours, minutes=minutes, seconds=seconds)
    expected = solution_function(hours=hours, minutes=minutes, seconds=seconds)

    assert expected == actual, f"Wrong result for {(hours, minutes, seconds)}, expected {expected}, received {actual}"
