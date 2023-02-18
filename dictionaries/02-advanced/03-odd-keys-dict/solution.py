def odd_keys_dict(dictionary):
    result = {}
    for k, v in dictionary.items():
        if k % 2 != 0:
            result[k] = v
    return result


# Using a comprehension
def odd_keys_dict(dictionary):
    return {
        k: v
        for k, v in dictionary.items()
        if k % 2 != 0
    }
