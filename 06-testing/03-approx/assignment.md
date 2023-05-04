# Approx

In a file `mystatistics.py`, write a function `average(ns)` that given a list `ns` of numbers, computes the average.
The average equals the sum of `ns` divided by the length of `ns`.

In `tests.py`, write a parametrized test with two parameters: `ns` and `expected`.
Make sure to include the case `([0.1, 0.1, 0.1], 0.1)`.

Run your tests.
We expect them to fail.

## Floating Points

Real numbers can be infinitely long: think of &pi;, or even just 1/3 = 0.333333...
A machine can't afford to represent infinitely long numbers, so they cut them off after a certain number of digits.
However, this causes a loss of precision.

Say, for example, that a machine works in decimal and that it can only store 3 digits.
We expect 1 / 3 * 3 to be equal to 1.

If we divide 1 by 3, we should get 0.33333333... but it will be cut off after 3 digits: 0.333.
When we multiply this by 3, we get 0.999, which is not equal to 1.

These kinds of rounding errors happen all the time.
In applications involving many numerical computations (e.g., physics engines in games), it is crucial to take these errors into account.
There's even a [separate field of mathematics](https://en.wikipedia.org/wiki/Numerical_analysis) that specializes in finding ways of keeping the impact of rounding errors to a minimum.

A computer works in binary.
Values that seem okay in decimal (such as `0.1`) cannot be represented exactly in binary.
For example,

```python
>>> sum([0.1] * 10)
0.9999999999999999

>>> sum([0.1] * 10) == 1
False

>>> 1 - sum([0.1] * 10)
1.1102230246251565e-16
```

So, if we are to write tests involving floating point numbers, we have to take into account that the results might be a bit off.
Luckily, this is easy to solve.
If we expect a specific value `expected` and have a certain result `actual`:

```python
# Troublesome: we expect exact results
assert expected == actual

# Allows for an error margin
assert abs(expected - actual) < 0.0001
```

`abs(expected - actual) < 0.0001` expresses that `expected` and `actual` should be "more or less equal": we tolerate differences up to `0.0001`.

Pytest offers a [helper function](https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest.approx) to make this even easier:

```python
from pytest import approx

assert approx(expected) == actual
```

If needed, you can specify a custom tolerance:

```python
assert approx(expected, abs=0.1) == actual
```

Here we allow for a large margin of error: `expected` and `actual` can differ up to `0.1`.
This might come in handy for tests, where we are typically not interested in specifying values of up to 7 digits:

```python
# Urgh, so many digits
assert approx(3.14159265) == pi

# Good enough for our purposes
assert approx(3.14, abs=0.01) == pi
```

Now, rely on `approx` to make your tests pass.
Go for a precision of `abs=0.01`.
