# Repeat

An iterator can also represent infinite collections.
Write a class `Repeat` that keeps producing the same element:

```python
>>> xs = Repeat(5)
>>> next(xs)
5

>>> next(xs)
5

>>> next(xs)
5
```

You should of course be careful with this iterator, lest you end up in an infinite loop:

```python
>>> list(Repeat(5))
# takes a very long time
```

> This functionality [already exists](https://docs.python.org/3/library/itertools.html#itertools.repeat) in Python's standard library.
  The reason we give it as an exercise is because it's easy to implement.
