# Assignment

Given a list of dictionaries representing a group of students, write a function **filter_students** that filters the students based on their age and returns a new list. The given age represents that the functions should return all students with a higher age.

```python
students = [
    {'name': 'Alice', 'age': 22},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 21},
    {'name': 'David', 'age': 19},
    {'name': 'Eve', 'age': 23}
]

def filter_students(students, age):
    pass #write your code here


# Example usage
print(filter_students(students, 21))
```
The output of the above example should be:

```output
[{'name': 'Alice', 'age': 22}, {'name': 'Eve', 'age': 23}]
```

