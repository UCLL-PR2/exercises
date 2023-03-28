def remove_first(xs):
    return xs[1:]


def repeat(xs):
    return (*xs, *xs)


def double(ns):
    return tuple(2 * n for n in ns)


def swap(xs, i, j):
    if i == j:
        return xs

    i, j = min(i, j), max(i, j)

    return (
        *xs[:i],
        xs[j],
        *xs[i+1:j],
        xs[i],
        *xs[j+1:]
    )
