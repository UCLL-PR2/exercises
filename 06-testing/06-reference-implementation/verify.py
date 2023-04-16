import pytest
import search


class Student:
    def __init__(self, id):
        self.id = id


def binary_search(students, id):
    left = 0
    right = len(students)

    while left < right:
        middle = (left + right) // 2
        middle_id = students[middle].id
        if id < middle_id:
            right = middle
        elif id > middle_id:
            left = middle + 1
        else:
            return students[middle]
    return None


@pytest.mark.parametrize('students', [
    [],
    [Student(id) for id in range(0, 100)],
    [Student(id) for id in [4, 5, 6, 11, 15, 16, 17, 18, 25, 27, 55, 56, 59, 70]],
])
@pytest.mark.parametrize('id', range(0, 100))
def test_search(students, id):
    expected = binary_search(students, id)
    actual = search.binary_search(students, id)
    assert expected == actual, f"Failed when looking for id={id}"
