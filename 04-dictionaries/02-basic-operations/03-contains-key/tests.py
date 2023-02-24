import pytest
import student
import solution


@pytest.mark.parametrize("dictionary, key", [
    ({1: '1'}, 1),
    *(
        ({'a', 1}, key) for key in ['a', 'b', 1]
    ),
    *(
        ({'a': 2, 'b': 5, 'c': 3}, key) for key in ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6]
    ),
])
def test_function(dictionary, key):
    function_name = 'contains_key'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(dictionary, key)
    expected = solution_function(dictionary, key)

    assert expected == actual, f"Wrong result for {(dictionary, key)}, expected {expected}, received {actual}"
