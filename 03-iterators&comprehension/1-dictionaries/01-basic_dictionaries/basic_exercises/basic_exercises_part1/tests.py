from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file

with reference_file('solution.py'):
    with reference_based_test('sum_dict_values') as testcase:
        testcase({'a': 1, 'b': 2, 'c': 3})        
    with reference_based_test('odd_keys_dict') as testcase:
        testcase({1: 'a', 2: 'b', 3: 'c'})        
    with reference_based_test('keys_with_value') as testcase:
        testcase({'a': 1, 'b': 2, 'c': 1}, 1)        
    with reference_based_test('double_dict_values') as testcase:
        testcase({'a': 1, 'b': 2, 'c': 3})        
    with reference_based_test('merge_dicts') as testcase:
        testcase({'a': 1, 'b': 2}, {'b': 3, 'c': 4})     
  