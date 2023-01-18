
def prime_numbers():
    primes = [x for x in range(2,100) if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))]
    return primes
