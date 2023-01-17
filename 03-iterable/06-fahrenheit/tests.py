from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


celsius_temps = [0, 10, 20, 30, 40]

with reference_file('solution.py'):
    with reference_based_test('list_celsius_to_fahrenheit') as testcase:
        testcase(celsius_temps)
        
       