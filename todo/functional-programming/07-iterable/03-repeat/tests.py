import pytest
from student import Repeat


@pytest.mark.parametrize("value", [0, 1, False, True, "abc"])
def test_repeat(value):
    xs = Repeat(value)
    for _ in range(1000):
        assert next(xs) == value
