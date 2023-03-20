import pytest
import itertools
from student import Repeat


@pytest.mark.parametrize("value", [0, 1, False, True, "abc"])
def test_repeat(value):
    expected = itertools.repeat(value)
    actual = Repeat(value)
    assert list(itertools.islice(expected, 1000)) == list(itertools.islice(actual, 1000))
