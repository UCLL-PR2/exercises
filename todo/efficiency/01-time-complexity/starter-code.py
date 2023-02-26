from timeit import timeit


def benchmark(function, lst):
    time = timeit("find_duplicates(ns)", globals={
        "ns": lst,
        "find_duplicates": function
    }, number=10)

    return f'{function.__name__} took {time:.3}s on [{", ".join(str(x) for x in lst[:10])}, ...] ({len(lst)} elements)'
