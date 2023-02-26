from timeit import timeit


def benchmark(function, lst):
    time = timeit("find_duplicates(ns)", globals={
        "ns": lst,
        "find_duplicates": function
    }, number=10)

    return f'{function.__name__} took {time:.3}s on [{", ".join(str(x) for x in lst[:10])}, ...] ({len(lst)} elements)'


def contains_duplicates1(ns):
    found_duplicates = False
    for i in range(len(ns)):
        for j in range(len(ns)):
            if i != j and ns[i] == ns[j]:
                found_duplicates = True
    return found_duplicates


def contains_duplicates2(ns):
    for i in range(len(ns)):
        for j in range(len(ns)):
            if i != j and ns[i] == ns[j]:
                return True
    return False


def contains_duplicates3(ns):
    for i in range(len(ns)):
        # j goes from i+1 to end instead of 0 to end
        for j in range(i + 1, len(ns)):
            if ns[i] == ns[j]:
                return True
    return False


def contains_duplicates4(ns):
    ns = sorted(ns)  # We sort the list
    for i in range(1, len(ns)):
        if ns[i-1] == ns[i]:
            return True
    return False


def contains_duplicates5(ns):
    previously_seen = set()
    for i in range(0, len(ns)):
        if ns[i] in previously_seen:
            return True
        else:
            previously_seen.add(ns[i])
    return False


import random

print(benchmark(contains_duplicates1, list(range(1000))))
print(benchmark(contains_duplicates1, list(range(2000))))
print(benchmark(contains_duplicates1, list(range(4000))))
print()
print(benchmark(contains_duplicates2, list(range(1000))))
print(benchmark(contains_duplicates2, list(range(2000))))
print(benchmark(contains_duplicates2, list(range(4000))))
print()
print(benchmark(contains_duplicates3, list(range(1000))))
print(benchmark(contains_duplicates3, list(range(2000))))
print(benchmark(contains_duplicates3, list(range(4000))))
print()
lst = list(range(5000))
print(benchmark(contains_duplicates1, lst))
print(benchmark(contains_duplicates2, lst))
print(benchmark(contains_duplicates3, lst))
print(benchmark(contains_duplicates4, lst))
print(benchmark(contains_duplicates5, lst))
print()
print('Shuffling lst')
random.shuffle(lst)
print(benchmark(contains_duplicates1, lst))
print(benchmark(contains_duplicates2, lst))
print(benchmark(contains_duplicates3, lst))
print(benchmark(contains_duplicates4, lst))
print(benchmark(contains_duplicates5, lst))
