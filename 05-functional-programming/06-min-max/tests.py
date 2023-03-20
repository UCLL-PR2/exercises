import pytest
import solution
import student


@pytest.mark.skipif('closest' not in dir(student), reason='closest not ')
@pytest.mark.parametrize("points", [
    [(0, 0)],
    [(8, 0), (0, 8)],
    [(1, 4), (2, 3), (4, 7), (9, 1), (5, 5)],
])
@pytest.mark.parametrize("target_point", [
    (x, y)
    for x in range(0, 11)
    for y in range(0, 11)
])
def test_closest(points, target_point):
    expected = solution.closest(points, target_point)
    actual = student.closest(points, target_point)

    assert expected == actual
