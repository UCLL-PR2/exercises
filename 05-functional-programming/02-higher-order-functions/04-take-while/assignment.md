# Take While

Write a function `take_while(xs, condition)` that looks for the first element in `xs` for which the function `condition` does not return a truthy value.
All values before this element should be put in one list, the remaining in another.
These two lists should be returned in a tuple.

```python
def is_negative(x):
    return x < 0

>>> take_while([-4, -2, 0, -1, 4, 6],is_negative)
([-4, -2], [0, -1, 4, 6])
```

The difference with `partition` is that `partition` goes through the entire list whereas `take_while` stops at the first element for which `condition` yields a falsey value.
