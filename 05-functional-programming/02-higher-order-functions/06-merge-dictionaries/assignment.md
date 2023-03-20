# Merge Dictionaries

Say we represent orders as dictionaries, where keys are items and values are amounts.

```python
>>> order1 = {'banana': 4, 'coke': 12}
>>> order2 = {'mustard': 1, 'chocolate': 7}
```

We'd like to combine both orders into a single dictionary.
The easiest way to achieve this in Python is to use the `**` operator:

```python
>>> combined = {**order1, **order2}
{'banana': 4, 'coke': 12, 'mustard': 1, 'chocolate': 7}
```

However, what happens if the dictionaries share keys?

```python
>>> order1 = {'banana': 4, 'coke': 12, 'chocolate': 3}
>>> order2 = {'mustard': 1, 'chocolate': 7}
>>> combined = {**order1, **order2}
{'banana': 4, 'coke': 12, 'mustard': 1, 'chocolate': 7}
```

As you can see, `order2` "wins": the three chocolates from `order1` completely disappear.
We would like a smarter dictionary merge, one that takes the sum of the values:

```python
>>> order1 = {'banana': 4, 'coke': 12, 'chocolate': 3}
>>> order2 = {'mustard': 1, 'chocolate': 7}
>>> combined = merge_dictionaries(order1, order2)
{'banana': 4, 'coke': 12, 'mustard': 1, 'chocolate': 10}
```

However, sometimes the sum is not what we want.
Say the dictionaries represent grades:

```python
>>> january_exams = {'P1': 9, 'FE': 15}
>>> august_exams = {'P1': 7}
```

Combining `january_exams` and `august_exams` should yield the final grades, but taking the sum, while it sounds very inviting, is not the right way to deal with shared keys.
Rather, the rule is that the combination must contain the _maximum_ of the grades:

```python
>>> final_grades = merge_dictionaries(january_exams, august_exams)
{'P1': 9, 'FE': 15}
```

`merge_dictionaries` cannot know whether it should take the sum, or the maximum, or something else altogether.
We therefore need to supply this information using a parameter, namely a function that decides what to do when two values vie for a place in the final dictionary.

Write a function `merge_dictionaries(d1, d2, merge_function)` that returns a new dictionary using the following rules:

* If a key only appears in `d1`, simply copy it and its corresponding value to the resulting dictionary.
* Same for `d2`.
* If a key `k` appears both in `d1` and `d2`, then the corresponding values `d1[k]` and `d2[k]` are fed to `merge_function`.
  This becomes the value for `k` in the resulting dictionary.
