import pytest
from intervals import overlapping_intervals


@pytest.mark.parametrize('left1', range(0, 10))
@pytest.mark.parametrize('right1', range(0, 10))
@pytest.mark.parametrize('left2', range(0, 10))
@pytest.mark.parametrize('right2', range(0, 10))
def test_overlapping_intervals(left1, right1, left2, right2):
    expected = any(x in range(left2, right2+1) for x in range(left1, right1+1))
    actual = overlapping_intervals((left1, right1), (left2, right2))
    assert expected == actual, f"overlapping_intervals(({left1}, {right1}), ({left2}, {right2})) should return {expected}"
