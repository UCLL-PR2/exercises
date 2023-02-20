# Assignment

Write a function `target_sum(ns, target)` that checks whether it is possible to take two values from `ns` whose sum equals `target`.
The same item cannot be used twice.

```python
# We are not allowed to use the third item twice
>>> target_sum([1, 2, 3], 6)
False

# If 3 actually occurs twice in the list, then it's okay
>>> target_sum([1, 2, 3, 3], 6)
True
```
