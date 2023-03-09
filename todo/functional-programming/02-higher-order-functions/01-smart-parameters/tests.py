import pytest
from student import repeat


@pytest.mark.parametrize("n", [0, 1, 5, 10])
def test_repeat(n):
    counter = 0

    def foo():
        nonlocal counter
        counter += 1

    repeat(foo, n)
    assert counter == n
