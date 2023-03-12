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
