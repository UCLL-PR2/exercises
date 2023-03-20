def count(xs, predicate):
    return len([x for x in xs if predicate(x)])


def indices_of(xs, condition):
    return [index for index in range(len(xs)) if condition(xs[index])]
