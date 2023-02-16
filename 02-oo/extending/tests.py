import pytest
from student import *


@pytest.fixture
def student():
    return Student(
        name='Peter',
        age=21,
        student_id='r1234567',
    )


def test_person():
    person = Person(
        name='John',
        age=18,
    )

    assert person.name == 'John'
    assert person.age == 18


def test_student():
    student = Student(
        name='Peter',
        age=21,
        student_id='r1234567',
    )

    assert student.name == 'Peter'
    assert student.age == 21
    assert student.student_id == 'r1234567'
    assert student.courses == set()


def test_enrolling(student):
    assert student.courses == set()
    student.enroll('P2')
    assert student.courses == { 'P2' }
    student.enroll('Intro')
    assert student.courses == { 'P2', 'Intro' }


def test_inheritance():
    student = Student(
        name='Peter',
        age=21,
        student_id='r1234567',
    )

    assert isinstance(student, Person)
