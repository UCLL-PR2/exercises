import pytest



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
