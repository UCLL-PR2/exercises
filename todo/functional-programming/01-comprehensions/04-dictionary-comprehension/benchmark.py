import random
import string


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


def random_name():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10)).capitalize()


class SlowStudentFinder:
    def __init__(self, students):
        self.__students = students

    def find(self, id):
        for student in self.__students:
            if student.id == id:
                return student


class FastStudentFinder:
    def __init__(self, students):
        self.__students = {student.id: student for student in students}

    def find(self, id):
        return self.__students[id]



from timeit import timeit

student_count = 10000
students= [Student(id, random_name()) for id in range(student_count)]

slow_finder = SlowStudentFinder(students)
fast_finder = FastStudentFinder(students)


print(timeit(f"[finder.find(id) for id in range({student_count})]", globals={'finder': slow_finder}, number=10))
print(timeit(f"[finder.find(id) for id in range({student_count})]", globals={'finder': fast_finder}, number=10))
