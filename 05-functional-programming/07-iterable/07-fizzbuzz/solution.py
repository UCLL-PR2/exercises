def fizzbuzz():
    current = 1
    while True:
        result = ''
        if current % 3 == 0:
            result += 'fizz'
        if current % 5 == 0:
            result += 'buzz'
        # If result is still empty, set it to str(current)
        result = result or str(current)
        yield result
        current += 1
