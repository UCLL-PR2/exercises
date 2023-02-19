from copy import copy
import pytest
import student
import solution


@pytest.mark.parametrize("ns", [
    [],
    [1],
    [-1],
    [1, -1],
    [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],
    [1, -2, -3, 4, 5],
    [-1, -2, -3, -4],
    [-5, -3, -6, 2, 4, 5, -1, -2, -1, -1],
])
def test_functionality(ns):
    actual_ns = copy(ns)
    expected_ns = copy(ns)

    assert student.remove_negatives(actual_ns) == solution.remove_negatives(expected_ns)

    assert expected_ns == actual_ns, f"Failed on {ns}"
