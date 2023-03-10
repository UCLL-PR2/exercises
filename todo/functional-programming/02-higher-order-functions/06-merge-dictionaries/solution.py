def merge_dictionaries(dict1, dict2, merge_function):
    result = dict(dict1)
    for k, v in dict2.items():
        if k in result:
            result[k] = merge_function(result[k], v)
        else:
            result[k] = v
    return result
