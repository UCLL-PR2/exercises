class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grow_older(self):
        self.age += 1


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = set()

    def enroll(self, course):
        self.courses.add(course)
