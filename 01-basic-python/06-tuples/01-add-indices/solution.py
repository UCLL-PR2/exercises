def add_indices(xs):
    indices = range(len(xs))
    return list(zip(indices, xs))

# Better: relying on existing functionality
def add_indices(xs):
    return list(enumerate(xs))
