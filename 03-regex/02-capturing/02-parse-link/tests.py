import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    '<a href="xxx">lalala</a>',
    '<a href="url">caption</a>',
    '<a>caption</a>',
    '<a href="url">caption<a>',
    '<a href=url>caption</a>',
    '<a href="ajflk">iojfgkld</a>',
    '<a href="xxx">lalala',
    'href="xxx">lalala<',
])
def test_function(string):
    function_name = 'parse_link'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(string)
    expected = solution_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"