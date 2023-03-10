from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('sum_squared_numbers') as testcase:
        testcase(5)
        testcase(1)
        testcase(10)
    with reference_based_test('sum_squared_numbers2') as testcase:
        testcase(5)
        testcase(1)
        testcase(10)

        
       