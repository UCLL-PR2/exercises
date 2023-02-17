# Assignment

Python allows you to use the `+` operator to concatenate lists:

```python
[1, 2] + [3, 4] == [1, 2, 3, 4]
```

Alternatively, you can also use the unpack operator `*` to easily build lists.

```python
xs = [1, 2]
ys = [3, 4]

[xs, ys]     # == [[1, 2], [3, 4]]
[*xs, ys]    # == [1, 2, [3, 4]]
[xs, *ys]    # == [[1, 2], 3, 4]
[*xs, *ys]   # == [1, 2, 3, 4]
```
