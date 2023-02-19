import pytest
import student
import solution
from textwrap import dedent


@pytest.mark.parametrize("string", [
    dedent(s.strip())
    for s in [
        """
        ....
        ....
        ....
        """,
        """
        ....
        .*..
        ....
        """,
        """
        .....
        .*...
        .....
        """,
        """
        .....
        .***.
        .....
        """,
        """
        ****.
        .*.*.
        .****
        """,
    ]
])
def test_function(string):
    function_name = 'add_bomb_counts'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = student_function(string)
    expected = solution_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
