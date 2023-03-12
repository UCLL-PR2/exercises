# Zip

As explained before, `zip` is a built-in function that pairs up corresponding elements in two or more iterables:

```python
>>> list(zip('abcd', [1, 2, 3, 4]))
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]

>>> list(zip('abcd', [1, 2, 3, 4], 'xyzw'))
[('a', 1, 'x'), ('b', 2, 'y'), ('c', 3, 'z'), ('d', 4, 'w')]
```

Note the surrounding call to `list`: this is necessary because `zip` returns an iterator:

```python
>>> zip('abcd', [1, 2, 3, 4])
<zip object at 0x00000273D6895BC8>
```

Adding `list` forces the iteration over all the elements and stores them in a list.

What happens when we call `zip` to iterables of unequal size?

```python
>>> list(zip('abcde', [1, 2, 3]))
[('a', 1), ('b', 2), ('c', 3)]
```

It seems that `zip` stops as soon as one of its arguments runs out of elements.

## Task

Write a class `PadZip` (and accompanying class `PadZipIterator`) that continues producing tuples as long as the _longest_ provided iterable is not empty.
Where values are missing, `None` is added:

```python
>>> list(PadZip('abcde', [1, 2, 3]))
[(a, 1), (b, 2), (c, 3), (d, None), (e, None)]
```

We want to be able to define our own padding value:

```python
>>> list(PadZip('abcde', [1, 2, 3], padding=0))
[(a, 1), (b, 2), (c, 3), (d, 0), (e, 0)]
```

`PadZip` needs exactly two collections to iterate over (we don't support three or more like `zip` does.)
Therefore `PadZip` must assume these collections are iterable, i.e., they must implement `__iter__`.
In other words, `PadZip` should work on lists, sets, strings, and so on.

This, however, also means that it must be able to deal with iterators (which also implement `__iter__`).
The tricky part about this is that iterators are _single use_.
To ensure consistency, we want `PadZip` to itself also be single use, regardless of the type of its arguments.

```python
# 'abc' and 'xyz' are both iterABLE collections, not single use iteratORS
>>> xs = PadZip('abc', 'xyz')

# First time works
>>> list(xs)
[('a', 'x'), ('b', 'y'), ('c', 'z')]

# Second time does not
>>> list(xs)
[]
```

The simplest way to achieve this is to have `PadZip`'s constructor use `iter` immediately:

* An iterable collection (list, set, ...) will return a single use iterator.
* An iterator will return itself.

In both cases, you end up with an iterator and consistency is guaranteed.
