import pytest


class Student:
    def __init__(self, id):
        self.id = id


def linear_search(students, id):
    return next((student for student in students if student.id == id), None)


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
    linear_result = linear_search(students, id)
    binary_result = binary_search(students, id)
    assert linear_result is binary_result, f"Failed when looking for id={id}"
