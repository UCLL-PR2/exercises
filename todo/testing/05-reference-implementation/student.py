def binary_search(students, id):
    return next((student for student in students if student.id == id), None)
