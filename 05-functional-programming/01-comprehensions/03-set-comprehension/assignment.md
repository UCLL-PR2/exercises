# Set Comprehension

A list comprehensions constructs a list, no big surprise there.
If instead we want a set, this is also possible: we need only change the brackets.

```python
def squares(ns):
    return {n**2 for n in ns}
```

Using a set instead of a list will cause duplicates to disappear from the end result:

```python
>>> [n**2 for n in range(-10, 10)]
[100, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> {n**2 for n in range(-10, 10)}
{64, 1, 0, 100, 36, 4, 9, 16, 81, 49, 25}
```

Also note how the order of the items is not preserved.

## Tasks

Write the following functions:

* `directors(movies)` collects all directors in a set.
* `common_elements(xs, ys)` should return the set of values that occur both in `xs` and `ys`.
