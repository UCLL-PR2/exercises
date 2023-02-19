from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file

def read_data(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        data = [line.split(",") for line in lines]
        return data

d = {'Tom': (32, 'Male'), 'Jane': (25, 'Female'), 'John': (28, 'Male'), 'Mary': (36, 'Female'), 'Bob': (44, 'Male'), 'Sue': (19, 'Female')}

with reference_file('solution.py'):
    with reference_based_test('create_dictionary') as testcase:
        testcase(read_data("example.txt"))

    with reference_based_test('older_than_30') as testcase:
        testcase(d)  
    
    with reference_based_test('all_ages') as testcase:
        testcase(d) 
         
    with reference_based_test('gender_totals') as testcase:
        testcase(d)  