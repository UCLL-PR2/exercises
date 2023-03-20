from itertools import pairwise


def total_distance(path, distance):
    return sum(distance(a, b) for a, b in pairwise(path))
