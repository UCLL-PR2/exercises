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

## Implementation

The goal of this exercise is to define the `AssocList` class.

We know `AssocList` needs to keep track of the key/value associations, meaning we need a way to store them.
There are many ways to do this, and you are free to pick your own.
Here, we will discuss how to use a list of pairs.

The idea is very simple: each `key`/`value` pair association is stored in a pair `[key, value]`.
Typically pairs are represented using tuples, but here we'll use a list so that we can modify them when needed (see later.)
All these pairs need to be stored somewhere, so we'll just dump them in a list: `[[key1, value1], [key2, value2], ...]`.

For example, the English to French dictionary above would be represented using

```python
[
    ['cat', 'chat'],
    ['dog', 'chien'],
    ['cheese', 'fromage']
]
```

### Empty AssocList

Let's start with defining the class `AssocList`.
Initially, an `AssocList` should be empty, which we can represent using the empty list `[]`.

```python
class AssocList:
    def __init__(self):
        self.__items = []
```

### Adding New Key/Value Pairs

Say we want to add a new association `key`/`value` to the `AssocList`.

```python
>>> assoc_list = AssocList()

>>> assoc_list['cat'] = 'chat'
```

First, we need to determine which method to define in order to make this assignment possible.
In this case, this is dunder method `__setitem__(self, key, value)`:

```python
class AssocList:
    # ...

    def __setitem__(self, key, value):
        # ???
```

As explained in a previous section, `assoc_list['cat'] = 'chat'` is translated into `assoc_list.__setitem__('cat', 'chat')`.

Adding a new key/value pair should be straightforward: we can simply `append` the pair to the list:

```python
class AssocList:
    # ...

    def __setitem__(self, key, value):
        # append [key, value] to __items
```

However, what what if a `key` already exists in our `AssocList`?
In this case, we want the new value to overwrite the old one.

```python
>>> assoc_list = AssocList()

>>> assoc_list['cat'] = 'chot'
# 'cat' is associated with 'chot'

>>> assoc_list['cat'] = 'chat'
# Now 'cat' should be associated with 'chat' instead
```

To achieve this, we need to refine our logic somewhat:

```python
class AssocList:
    # ...

    def __setitem__(self, key, value):
        # find pair in __items that has pair[0] == key
        # if no such pair can be found
        #   append [key, value] to __items
        # else
        #   overwrite pair[1] with value
```

### Looking Up

Given a key, we want to be able to ask the `AssocList` what value is associated with it:

```python
>>> assoc_list = AssocList()
>>> assoc_list['cat'] = 'chat'

# Ask what's associated with cat
>>> assoc_list['cat']
'chat'
```

To allow this `assoc_list[key]` syntax, we need to define `__getitem__(self, key)`.
The above lookup `assoc_list['cat']` corresponds to `assoc_list.__getitem__('cat')`.

```python
class AssocList:
    # ...

    def __getitem__(self, key):
        # ???
```

Here, we need to write code that goes through `__items__` and looks for the `pair` for which `pair[0] == key`.
When it finds such a pair, `__getitem__` should return the corresponding value.
If no such pair can be found, raise an error (`raise KeyError()`).

## Task

Define a class `AssocList` with the following members:

* A constructor that creates an empty `AssocList`.
* `assoc_list[key] = value` associates `key` with `value`.
  If `assoc_list` already associates `key` with something, it is overwritten by `value`.
* `key in assoc_list` checks if `key` appears in `assoc_list`. Hint: `__contains__`.
* `assoc_list[key]` returns the `value` associates with `key`.
* `len(assoc_list)` returns the number of key/value pairs.
* `assoc_list.keys` returns a list of keys.
* `assoc_list.values` returns a list of values.
