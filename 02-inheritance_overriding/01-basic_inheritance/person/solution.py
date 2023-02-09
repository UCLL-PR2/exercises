class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return "Hello, my name is " + self.name

class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)
        self.student_id = student_id
        
    def enroll(self):
        return "Student " + self.name + " with ID " + str(self.student_id) + " has enrolled in a course."
