from student import total_distance
import operator


def test_total_distance1():
    path = [0, 1, 2, 3, 4, 5]
    expected = 1 + 3 + 5 + 7 + 9
    actual = total_distance(iter(path), operator.add)
    assert expected == actual


def test_total_distance2():
    path = [1, 5, 3, 4, 2, 6]
    expected = 6 + 8 + 7 + 6 + 8
    actual = total_distance(iter(path), operator.add)
    assert expected == actual


def test_total_distance3():
    path = [1, 5, 3, 4, 2, 6]
    expected = 5 + 5 + 4 + 4 + 6
    actual = total_distance(iter(path), max)
    assert expected == actual


def test_total_distance4():
    path = [1, 5, 3, 4, 2, 6]
    expected = 1 + 3 + 3 + 2 + 2
    actual = total_distance(iter(path), min)
    assert expected == actual
