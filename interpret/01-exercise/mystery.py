def mystery(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    result = []
    i = 2
    while i < len(sieve):
        if sieve[i]:
            result.append(i)
            j = i * 2
            while j < len(sieve):
                sieve[j] = False
                j += i
        i += 1
    return result
