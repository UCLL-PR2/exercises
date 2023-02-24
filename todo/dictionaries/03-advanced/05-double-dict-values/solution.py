def double_dict_values(dictionary):
    doubled_dict = {}
    for k, v in dictionary.items():
        doubled_dict[k] = v * 2
    return doubled_dict


# Using a comprehension
def double_dict_values(dictionary):
    return {k: v * 2 for k, v in dictionary.items()}
