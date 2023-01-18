def squared_numbers(n):
    for i in range(1, n+1):
        yield i**2

def sum_squared_numbers(n):
    return sum(squared_numbers(n))

def sum_squared_numbers2(n):
    return sum([x**2 for x in range(1,6)])
