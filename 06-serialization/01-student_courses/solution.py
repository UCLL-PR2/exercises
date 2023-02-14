import pickle

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hello, {self.name}!"

class Student(Person):
    def __init__(self, name, age, gender, student_id, courses=[]):
        super().__init__(name, age, gender)
        self.id = student_id
        self.courses = courses

    def enroll(self, course):
        self.courses.append(course)

# Create a few people and students
people = [
    Person("John", 30, "male"),
    Person("Sarah", 25, "female"),
    Student("Mike", 22, "male", 123, ["Calculus", "Linear Algebra"]),
    Student("Emily", 21, "female", 456)
]

# Serialize the people list and write it to a file
with open("people.pickle", "wb") as f:
    pickle.dump(people, f)

# Read the serialized data from the file and deserialize it
with open("people.pickle", "rb") as f:
    deserialized_people = pickle.load(f)

# Iterate over the deserialized objects and greet each one
for person in deserialized_people:
    print(person.greet())
