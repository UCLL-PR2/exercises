from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('create_word_dict') as testcase:
        testcase("example.txt")
    with reference_based_test('get_top_10_words') as testcase:
        d = {'the': 13, 'quick': 3, 'brown': 3, 'fox': 4, 'jumps': 1, 'over': 2, 'lazy': 2, 'dog': 4, 'snoozes': 1, 'lazily': 1, 'in': 1, 'sun': 2, 'is': 1, 'and': 6, 'chases': 1, 'they': 2, 'run': 1, 'through': 1, 'fields': 1, 'hills': 1, 'sets': 1, 'sky': 1, 'turns': 1, 'pink': 1, 'orange': 1, 'are': 1, 'tired': 1, 'but': 1, 'happy': 1, 'curl': 1, 'up': 1, 'together': 1, 'fall': 1, 'asleep': 1}
        testcase(d)
        
        

        
       