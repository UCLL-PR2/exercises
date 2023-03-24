import pytest
import solution
import student


class Student:
    def __init__(self, id):
        self.id = id


@pytest.mark.parametrize('students', [
    [],
    [Student(id) for id in range(0, 100)],
    [Student(id) for id in [4, 5, 6, 11, 15, 16, 17, 18, 25, 27, 55, 56, 59, 70]],
])
@pytest.mark.parametrize('id', range(0, 100))
def test_search(students, id):
    expected = solution.binary_search(students, id)
    actual = student.binary_search(students, id)
    assert expected == actual, f"Failed when looking for id={id}"
