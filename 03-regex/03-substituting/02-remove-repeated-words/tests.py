import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '',
    'a',
    'aa',
    'aa aa',
    'aa a',
    'a a b b',
    'aaa aaa bb bb c c',
    'a b a b',
    'a a a a b',
])
def test_function(string):
    function_name = 'remove_repeated_words'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(string)
    expected = solution_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
