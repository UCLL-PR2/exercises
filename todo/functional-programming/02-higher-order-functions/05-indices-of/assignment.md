# Indices Of

Write a function `indices_of(xs, condition)` that returns the indices of all the elements for which `condition` returns a truthy value.

```python
def is_odd(x):
    return x % 2 != 0

>>> indices_of([1, 2, 3, 4, 5, 6, 7, 8], is_odd)
[0, 2, 4, 6]
```
