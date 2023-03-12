import pytest
from student import InclusiveRange, InclusiveRangeIterator


def test_inclusive_range_is_class():
    assert type(InclusiveRange) == type


def test_inclusive_range_implements_iter():
    assert hasattr(InclusiveRange, '__iter__')


def test_iter_returns_iterator():
    assert type(iter(InclusiveRange(1, 10))) == InclusiveRangeIterator


def test_iterator_implements_iterator_protocol():
    assert hasattr(InclusiveRangeIterator, '__iter__')
    assert hasattr(InclusiveRangeIterator, '__next__')


@pytest.mark.parametrize('start', range(-5, 5))
@pytest.mark.parametrize('end', range(-5, 5))
def test_inclusive_range(start, end):
    assert list(InclusiveRange(start, end)) == list(range(start, end+1))
