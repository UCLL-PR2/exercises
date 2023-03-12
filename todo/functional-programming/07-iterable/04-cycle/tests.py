import pytest
import itertools
from student import Cycle


@pytest.mark.parametrize("values", [
    [1],
    'abc',
    [1, 2, 3],
    [1, 2, 3, False, 4, True, 'xyz'],
])
def test_cycle(values):
    expected = itertools.cycle(values)
    actual = Cycle(values)
    assert list(itertools.islice(expected, 1000)) == list(itertools.islice(actual, 1000))
