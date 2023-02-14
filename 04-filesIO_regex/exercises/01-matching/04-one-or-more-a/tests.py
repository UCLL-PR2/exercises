import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    "",
    "a",
    "aa",
    "aaaaa",
    "aaaaab",
])
def test_function(string):
    assert bool(student.one_or_more_a(string)) == bool(solution.one_or_more_a(string))
