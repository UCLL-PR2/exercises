from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file

dic = {"Name": "John", "Age": 30, "City": "New York"}
dic2 = {"Name": "Jane", "Age": 25, "City": "San Francisco"}
with reference_file('solution.py'):
    with reference_based_test('create_dict') as testcase:
        testcase()        
    with reference_based_test('add_country') as testcase:
        testcase(dic)        
    with reference_based_test('get_age') as testcase:
        testcase(dic)        
    with reference_based_test('update_age') as testcase:
        testcase(dic,35)        
        testcase(dic,21)        
    with reference_based_test('remove_city') as testcase:
        testcase(dic)     
    with reference_based_test('check_country') as testcase:
        testcase(dic)    
    with reference_based_test('get_keys') as testcase:
        testcase(dic)
    with reference_based_test('get_values') as testcase:
        testcase(dic)
    with reference_based_test('create_dict2') as testcase:
        testcase()
    with reference_based_test('merge_dicts') as testcase:
        testcase(dic,dic2)