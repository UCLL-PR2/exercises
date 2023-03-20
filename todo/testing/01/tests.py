def overlapping_intervals(interval1, interval2):
    left1, right1 = interval1
    left2, right2 = interval2

    return left1 <= left2 <= right1 or left1 <= right2 <= right1



def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))


def test_overlapping_intervals2():
    assert overlapping_intervals((1, 5), (0, 8))
