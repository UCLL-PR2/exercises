import pytest
import student


def if_defined(function_name):
    return pytest.mark.skipif(function_name not in dir(student), reason=f'{function_name} has not been defined')



@if_defined('is_prime')
@pytest.mark.parametrize('n', [2, 3, 5, 7, 11, 13, 97])
def test_is_prime_on_primes(n):
    assert student.is_prime(n)


@if_defined('is_prime')
@pytest.mark.parametrize('n', [0, 1, 4, 6, 8, 9, 10, 100])
def test_is_prime_on_nonprimes(n):
    assert not student.is_prime(n)


@if_defined('primes')
def test_primes():
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    actual = student.primes()
    assert all(x == y for x, y in zip(expected, actual))
