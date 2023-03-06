# Assignment

Write a Python function `keys(dictionary)` that returns all keys as a list.
The order is unimportant.

For example,

```python
>>> keys({})
[]

>>> keys({'a': 1})
['a']

>>> keys({'a': 1, 'b': 2})
['a', 'b']
```

> Technical detail, mentioned for completeness: in order to get the `keys` of a dictionary, you will need to call a certain method.
> This method will not return an actual list, but something "list-like".
> If it were to return the values as an actual list, it would have to allocate extra memory for a new list of keys.
> If the dictionary were to contain many keys, that would be a waste of memory.
> Instead, the "list-like" object cheats by only keeping a reference to the dictionary itself.
> When you iterate over this "list" of keys, it will simply look for them in the original dictionary object.
> This way no extra memory is needed.
