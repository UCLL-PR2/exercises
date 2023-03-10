def indices_of(xs, condition):
    return [index for index in range(len(xs)) if condition(xs[index])]
