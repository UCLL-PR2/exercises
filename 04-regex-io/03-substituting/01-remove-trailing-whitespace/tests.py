import pytest
import student
import solution


@pytest.mark.parametrize("string", [
        'fdjfkld jfjs fjdslfk'.strip(),
        'fdjfkld jfjs fjdslfk ',
        'fdjfkld jfjs fjdslfk\t',
        'fdjfkld jfjs fjdslfk       ',
        'x  \ny   ',
        '''
        fdf qqip saofp k        \t\x20
        fjdklfj f sfjslkf     \x20
        fdjfkldjf      \x20'''
])
def test_function(string):
    function_name = 'remove_trailing_whitespace'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(string)
    expected = solution_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
