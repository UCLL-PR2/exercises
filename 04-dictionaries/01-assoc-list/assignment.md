# AssocList

An _associative container_ is a container that, well, associates "keys" with "values".
Okay, that's pretty vague.
Maybe a few examples can help.

* A English-to-French dictionary associates English words with their French translation.
  Here, the _key_ is the English word and the _value_ is the French translation.
* An attendance sheet associates names (= key) with a boolean value (= value), indicating whether that particular someone is present or not.
* An item catalog associates items (= keys) with their prices (= values).

Notice how it typically only works well in one direction: given an English word, it is easy to look up the French translation in an English-to-French dictionary, but it'd take a lot more effort to do the opposite.

We want to create a class named `AssocList` that allows us to store such associations.
Here's an example of how we could use it:

```python
# Create an empty dictionary
>>> en_to_fr = AssocList()

# Populating our dictionary
>>> en_to_fr['cat'] = 'chat'
>>> en_to_fr['dog'] = 'chien'
>>> en_to_fr['cheese'] = 'fromage'

# Look up translations
>>> word = 'cat'
>>> f'The translation of {cat} is {en_to_fr(cat)}.'
'The translation of cat is chat.'
```

## Task

Define a class `AssocList` with the following members:

* A constructor that creates an empty `AssocList`.
* `assoclist[key] = value` associates `key` with `value`.
  If `assoclist` already associates `key` with something, it is overwritten by `value`.
  You might also want to look up [`__setitem__`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__).
* `key in assoclist` checks if `key` appears in `assoclist`. Hint: `__contains__`.
* `assoclist[key]` returns the `value` associates with `key`.
* `len(assoclist)` returns the number of key/value pairs.
* `assoclist.keys` returns a list of keys.
* `assoclist.values` returns a list of values.

An important question is: how will you store those key/value associations.
We suggest you introduce a private attribute `__items` that keeps track of a list of pairs:

```python
>>> al = AssocList()
# __items == []

>>> al[key] = value
# __items == [[key, value]]

>>> al[key2] = value2
# __items == [[key, value], [key2, value2]]
```
