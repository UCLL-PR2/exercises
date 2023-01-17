from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('process_data') as testcase:
        data = ['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry']
        testcase(data)

    with reference_based_test('avg_age') as testcase:
        data = {
                    'John Smith': {
                        'age': 20,
                        'courses': ['Math', 'Physics']
                    },
                    'Jane Doe': {
                        'age': 21,
                        'courses': ['Biology', 'Chemistry']
                    }
                }        
        testcase(data)        

    with reference_based_test('courses') as testcase:
        data = {
            'John Smith': {
                'age': 20,
                'courses': ['Math', 'Physics']
            },
            'Jane Doe': {
                'age': 21,
                'courses': ['Biology', 'Chemistry']
            }
        }
        testcase(data)  

    with reference_based_test('most_common_course') as testcase:
        data = {
            'John Smith': {
                'age': 20,
                'courses': ['Math', 'Physics']
            },
            'Jane Doe': {
                'age': 21,
                'courses': ['Biology', 'Chemistry']
            },
            'Bob Smith': {
                'age': 22,
                'courses': ['Biology', 'Chemistry']
            }
        }
        testcase(data)         
