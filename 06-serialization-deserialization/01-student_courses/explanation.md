# Exercise Serialization/deserialization Student
Work in the student.py file.

Define a class called Person with the following attributes:
- **name**: a string representing the person's name
- **age**: an integer representing the person's age
- **gender**: a string representing the person's gender (either "male" or "female")

Define a method called **greet** on the Person class that returns a string greeting the person by name, such as *"Hello, John!"*

Define a subclass of Person called Student with the following additional attributes:

- **id**: an integer representing the student's ID number
- **courses**: a list of strings representing the courses the student is enrolled in
- Define a method called **enroll** on the Student class that allows a student to enroll in a new course. This method should accept a string representing the course name and add it to the student's list of courses.

Create a few instances of both the Person and Student class, and store them in a list called people. Use the pickle module to serialize the people list and write it to a file called **people.pickle**. For example:
```Python
# Create a few people and students

people = [
    Person("John", 30, "male"),
    Person("Sarah", 25, "female"),
    Student("Mike", 22, "male", 123, ["Calculus", "Linear Algebra"]),
    Student("Emily", 21, "female", 456)
]
```

Read the serialized data from the **people.pickle** file and deserialize it back into a list of Person and Student objects.
```Python

# Serialize the people list and write it to a file
with open("people.pickle", "wb") as f:
    ...
# Read the serialized data from the file and deserialize it
with open("people.pickle", "rb") as f:
    ...
```
Iterate over the list of deserialized objects and call the greet method on each one to ensure that the deserialization was successful.