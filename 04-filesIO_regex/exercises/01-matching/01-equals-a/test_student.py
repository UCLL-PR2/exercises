import pytest
from student import equals_a


@pytest.mark.parametrize("string,expected", [
    ("", False),
    ("a", True),
    ("aa", False),
    ("b", False),
])
def test_equals_a(string, expected):
    assert bool(equals_a(string)) == expected
