def repeat_and_collect(function, n):
    return [function() for _ in range(n)]


def collect_while(function):
    result = [function()]
    while result[-1]:
        result.append(function())
    return result
