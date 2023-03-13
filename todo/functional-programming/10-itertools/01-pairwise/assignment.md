# Pairwise

The [`itertools`](https://docs.python.org/3/library/itertools.html) module contains many iterator-centric functionality.
One of the functions in this module is [`pairwise`](https://docs.python.org/3/library/itertools.html#itertools.pairwise).

```python
>>> from itertools import pairwise
>>> list(pairwise(range(5)))
[(0, 1), (1, 2), (2, 3), (3, 4)]
```

Rely on it to solve the exercise below.

## Task

Say that you have a map with several cities.
To keep things simple, the cities are simply numbered: `0`, `1`, `2`, etc.

There is a road between every two cities.
You can query the distance between two cities `a` and `b` using `distance(a, b)`.

A _path_ is a sequence of cities, for example, `[0, 5, 3, 4]`.
The total distance of a path is the sum of all the lengths of the roads between the cities: `distance(0, 5) + distance(5, 3) + distance(3, 4)`.

We ask of you to write a function `total_distance(path, distance)` which computes the total distance of `path`.

* The `path` parameter is an iterator of cities.
* The `distance` parameter is a function that you can use to determine the distance between two cities.
