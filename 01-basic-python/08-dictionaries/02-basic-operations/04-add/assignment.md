# Assignment

Write a Python function `add(dictionary, key, value)` that adds a new `key`/`value` pair to the given dictionary.
If `dictionary` already contains an entry with key `key`, it should be overwritten.

```python
>>> d = {}

>>> add(d, 'a', 1)
>>> d
{'a': 1}

>>> add(d, 'b', 2)
>>> d
{'a': 1, 'b': 2}

>>> add(d, 'b', 3)
>>> d
{'a': 1, 'b': 3}
```
