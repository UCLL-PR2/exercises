def average(ns):
    return sum(ns) / len(ns)


import pytest


@pytest.mark.parametrize('ns, expected', [
    ([1], 1),
    ([1, 3], 2),
    ([.1, .1, .1], .1),
])
def test_average(ns, expected):
    assert pytest.approx(expected) == average(ns)