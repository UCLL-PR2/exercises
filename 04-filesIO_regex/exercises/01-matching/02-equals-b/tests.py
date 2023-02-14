import pytest
from student import equals_b


@pytest.mark.parametrize("string,expected", [
    ("", False),
    ("a", False),
    ("aa", False),
    ("b", True),
    ("bb", False),
])
def test_function(string, expected):
    assert bool(equals_b(string)) == expected
