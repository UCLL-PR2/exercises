def combine_lists_to_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# print(combine_lists_to_dict(keys, values)) # output: {'a': 1, 'b': 2, 'c': 3}