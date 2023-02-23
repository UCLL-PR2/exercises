from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('sort_dict_by_values') as testcase:
        d = {'a': 3, 'b': 1, 'c': 2}
        testcase(d)
        

        
       