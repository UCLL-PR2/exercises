def keys_with_value(dictionary, value):
    keys = []
    for k, v in dictionary.items():
        if v == value:
            keys.append(k)
    return keys


# Using a comprehension
def keys_with_value(dictionary, value):
    return [
        k
        for k, v in dictionary.items()
        if v == value
    ]
