def last_digit(n):
    return n % 10


def remove_last_digit(n):
    return n // 10


def digit_sum(n):
    result = 0
    while n > 0:
        result += last_digit(n)
        n = remove_last_digit(n)
    return result