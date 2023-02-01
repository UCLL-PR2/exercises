students = [
    {'name': 'Alice', 'age': 22},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 21},
    {'name': 'David', 'age': 19},
    {'name': 'Eve', 'age': 23}
]

def filter_students(students, age):
    return list(filter(lambda student: student['age'] > age, students))

# Example usage
print(filter_students(students, 21))