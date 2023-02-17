from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


my_list = [0, 10, 20, 30, 40]
my_list2 = [0, 1, -10, 2]

with reference_file('solution.py'):
    with reference_based_test('is_it_sorted') as testcase:
        testcase(my_list)
        testcase(my_list2)
        
       