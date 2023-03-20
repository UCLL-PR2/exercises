def find(xs, condition):
    for x in xs:
        if condition(x):
            return x
    return None
