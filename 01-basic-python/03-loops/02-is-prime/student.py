# Write your code here

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0 and i != n:
            return False
    return True