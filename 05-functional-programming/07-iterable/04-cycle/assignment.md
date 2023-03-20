# Cycle

Another example of an infinite sequence is `Cycle`:

```python
>>> xs = Cycle('abcd')
>>> itertools.islice(xs, 10)  # Take 10 first elements
['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
```

Implement `Cycle` as an iterator.

> This functionality also [already exists](https://docs.python.org/3/library/itertools.html#itertools.cycle).
> But again, good exercise.
