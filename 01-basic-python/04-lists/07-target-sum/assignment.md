# Assignment

Write a function `target_sum(ns, target)` that checks whether it is possible to take two values from `ns` whose sum equals `target`.
The same item can be used twice.

```python
>>> target_sum([1, 2, 3], 5)
True    # it is possible to make 5 using `2` and `3`

>>> target_sum([1, 2, 3], 7)
False   # it is impossible to make 7

>>> target_sum([1, 2, 3], 6)
True    # it is possible to make 6 using 3 twice
```
