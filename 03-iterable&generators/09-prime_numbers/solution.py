
def prime_numbers():
    primes = [x for x in range(2,100) if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))]
    return primes


# Solution without list comprehension 
# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True

# def prime_numbers():
#     primes = []
#     for x in range(2, 100):
#         if is_prime(x):
#             primes.append(x)
#     return primes