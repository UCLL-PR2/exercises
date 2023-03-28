def remove_first(xs):
    """
    >>> xs = [1, 2, 3]
    >>> remove_first(xs)
    >>> xs
    [2, 3]
    """
    del xs[0]


def repeat(xs):
    """
    >>> xs = [1, 2, 3]
    >>> repeat(xs)
    >>> xs
    [1, 2, 3, 1, 2, 3]
    """
    xs.extend(xs)


def double(ns):
    """
    >>> xs = [1, 2, 3]
    >>> double(xs)
    >>> xs
    [2, 4, 6]
    """
    for i in range(len(ns)):
        ns[i] *= 2


def swap(xs, i, j):
    """
    >>> xs = ['a', 'b', 'c', 'd', 'e']
    >>> swap(xs, 1, 3)
    >>> xs
    ['a', 'd', 'c', 'b', 'e']
    """
    xs[i], xs[j] = xs[j], xs[i]
