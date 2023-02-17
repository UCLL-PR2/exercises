def create_dictionary(keys, values):
    result = {}
    for key, value in zip(keys, values):
        result[key] = value
    return result


# Alternative
def create_dictionary(keys, values):
    return dict(zip(keys, values))
