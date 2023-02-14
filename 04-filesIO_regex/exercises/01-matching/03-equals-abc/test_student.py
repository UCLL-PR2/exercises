import pytest
from student import equals_abc


@pytest.mark.parametrize("string,expected", [
    ("", False),
    ("a", False),
    ("aa", False),
    ("b", False),
    ("bb", False),
    ("abc", True),
    ("abcd", False),
])
def test_function(string, expected):
    assert bool(equals_abc(string)) == expected
