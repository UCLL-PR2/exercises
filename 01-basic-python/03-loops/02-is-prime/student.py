# Write your code here
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False

    return n > 1