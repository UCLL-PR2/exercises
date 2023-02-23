def sort_dict_by_values(d):
    return {k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)}
    
# d = {'a': 3, 'b': 1, 'c': 2}
# print(sort_dict_by_values(d)) # output: {'a': 3, 'c': 2, 'b': 1}
