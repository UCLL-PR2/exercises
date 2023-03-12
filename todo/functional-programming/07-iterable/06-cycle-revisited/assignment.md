# Cycle Revisited

Write a generator function `cycle(xs)` that repeats the elements from `xs` endlessly.

```python
>>> xs = cycle('abcd')
>>> itertools.islice(xs, 10)  # Take 10 first elements
['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
```
