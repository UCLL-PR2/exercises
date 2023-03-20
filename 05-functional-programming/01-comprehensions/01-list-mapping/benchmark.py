def squares_loop(ns):
    result = []
    for n in ns:
        result.append(n**2)
    return result


def squares_loop2(ns):
    # Ensures that the right amount of memory is allocated straight away
    result = list(ns)
    for i in range(len(result)):
        result[i] = result[i]**2
    return result


def squares_comprehension(ns):
    return [n**2 for n in ns]



from timeit import timeit

def benchmark(function):
    time_needed = timeit(f"squares(range(1000000))", globals={'squares': function}, number=10)
    print(f"{function.__name__} used {time_needed:.3} seconds")


for function in [squares_loop, squares_loop2, squares_comprehension]:
    benchmark(function)
