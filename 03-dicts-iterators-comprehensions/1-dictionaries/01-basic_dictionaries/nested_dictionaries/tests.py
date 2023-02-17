from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('key_values') as testcase:
        dic = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F"}
        testcase(dic)        
    with reference_based_test('key_check') as testcase:
        dic = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F"}
        testcase(dic,3)
        testcase(dic,4)
        testcase(dic,7)
    with reference_based_test('value_check') as testcase:
        dic = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F"}
        testcase(dic,"A")
        testcase(dic,"B")
        testcase(dic,"C")
        testcase(dic,"R")
    with reference_based_test('nested_dict') as testcase:
        d = {
                "A" : {1:"Z",2:"C"},
                "B" : {3:"E",5:"V"},
                "C" : {4:"R",6:"G"},
            }
        testcase(d)

    