import unittest
from student import *

class TestPersonAndStudent(unittest.TestCase):

    def setUp(self):
        self.person = Person("Alice", 25)
        self.student = Student("Bob", 20, 12345)

    def test_person_greet(self):
        self.assertEqual(self.person.greet(), "Hello, my name is Alice")

    def test_student_enroll(self):
        self.assertEqual(self.student.enroll(), "Student Bob with ID 12345 has enrolled in a course.")

    def test_student_inherits_from_person(self):
        self.assertIsInstance(self.student, Person)

if __name__ == '__main__':
    unittest.main()
