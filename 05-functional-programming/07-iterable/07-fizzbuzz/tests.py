from itertools import islice
import student
import solution


def test_fizzbuzz():
    expected = islice(solution.fizzbuzz(), 1000)
    actual = islice(student.fizzbuzz(), 1000)
    assert expected == actual
