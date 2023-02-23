from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file

students = [
    {'name': 'Alice', 'age': 22},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 21},
    {'name': 'David', 'age': 19},
    {'name': 'Eve', 'age': 23}
]


with reference_file('solution.py'):
    with reference_based_test('filter_students') as testcase:
        testcase(students,21)
        testcase(students,19)
        testcase(students,22)
       