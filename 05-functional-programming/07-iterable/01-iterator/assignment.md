# Iterable

You've encountered multiple collections:

* Lists
* Tuples
* Strings
* Sets
* Dictionaries

Each collection supports a number of operations:

* Each of the four above implements `__len__`, meaning you can use `len(collection)` to determine how many elements it contains.
* Lists, tuples and dictionaries implement `__getitem__`, allowing you to use `collection[k]` to fetch elements.
* Lists offer `append`, while sets have `add` to add values to the container.
  Tuple, being readonly, has no member to add extra elements.

One important operation these collections share may not be so apparent: each of them allow to be _iterated_.
Consider the following pieces of code:

```python
for x in collection:
    # ...

min(collection)

max(collection)

sum(collection)

all(collection)

any(collection)

[expr for x in collection]

" ".join(collection)
```

All of these need to visit each element of `collection` in turn.
They want to be able to operate on any type of collection (set, tuple, list, whatever), but they don't want to have specialized implementations for each such type of collection.
The best way to achieve this is to agree on some standard, uniform way of getting access to all elements of a collection.

For example, one option would be to have each collection type offer a `copy_to_list` method that copies all its items to a list.
This way, no matter what type of collection (set, list, tuple, ...) we receive, we can always rely on `copy_to_list` to get the elements in a list and be on our way.
However, copying everything to a list takes time and memory.
Fortunately, there is a better alternative: _iterators_.

## Iterators

An iterator is an object that can be used to enumerate all elements of a collection.
Say we create such an iterator for lists.
We want to use it as follows:

```python
>>> iterator = ListIterator([1, 2, 3])

>>> iterator.next()
1

>>> iterator.next()
2

>>> iterator.next()
3

>>> iterator.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

As you can see, each call to `next` gives an element of the list.
Let's implement this `ListIterator` class:

```python
class ListIterator:
    def __init__(self, lst):
        self.__list = lst
        self.__current_index = 0

    def next(self):
        # Check if we reached the end
        if self.__current_index == len(self.__list):
            # Raise StopIteration to notify user end of list has been reached
            raise StopIteration()
        # Fetch current element
        result = self.__list[self.__current_index]
        # Move over to next element in list
        self.__current_index += 1
        # Return fetched element
        return result
```

## The Iterator Protocol

Python knows about the concept of iterators.
For example, the `for` loop internally relies on iterators.

Now, in order for Python to recognize an object as an iterator, it expects the object to implement two methods: `__iter__` and `__next__`.
We can adapt our `ListIterator` above to conform to this rule:

```python
class ListIterator:
    def __init__(self, lst):
        self.__elts = lst
        self.__current_index = 0

    def __next__(self):
        # Check if we reached the end
        if self.__current_index == len(self.__elts):
            # Raise StopIteration to notify user end of list has been reached
            raise StopIteration()
        # Fetch current element
        result = self.__elts[self.__current_index]
        # Move over to next element in list
        self.__current_index += 1
        # Return fetched element
        return result

    # Ignore this method for now
    def __iter__(self):
        return self
```

As always, a dunder method should not be called directly.
Using this `ListIterator` goes as follows:

```python
>>> iterator = ListIterator([1, 2, 3])

>>> next(iterator)   # Calls __next__ internally
1

>>> next(iterator)
2

>>> next(iterator)
3

>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

As you can see, this `ListIterator` consumes little memory: it does not copy the list, but merely keeps a reference to it.
No matter how long the list, a `ListIterator` will always occupy the same small amount of memory.

## `iter`

Now, this `ListIterator` class actually already exists.
There was no need for us to implement it.
Given a list, we can ask it for an iterator as follows:

```python
>>> xs = [1, 2, 3]
>>> iterator = iter(xs)      # Actually calls xs.__iter__() internally

>>> next(iterator)
1

>>> next(iterator)
2

>>> next(iterator)
3

>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

In general, given a `collection`, we are able to call `iter(collection)` on it and get an iterator specialized in that collection.

Note that an iterator is a single-use object: once the end of the collection has been reached, the iterator ceases to be useful.

## Summary

There are two classes two consider: on the one hand we have the the collection or _iterable_ class, on the other we have the corresponding _iterator_ class.

The iterable (collection) class implements `__iter__`.
Examples are `list`, `str`, `tuple`, `set` and `dict`.
This `__iter__` method should return an _iterator_ object.

An iterator object must have these two methods:

* `__iter__`: which simply returns itself.
* `__next__`: which, when called repeatedly, returns the elements of the collection.

An iterator object is single use: it goes through its elements once, after which it ceases to be useful.
If you need to go through the same elements again, you'll have to ask the _iterable_ object for a new iterator.

Following this convention has two advantages:

* On the one hand, functions that operate on a collection (`min`, `max`, `sum`, `any`, etc.) have a uniform, standardized way of accessing all types of collections.
  No specialized code for each collection type is required.
* If you create a new collection class of your own, equipping it with `__iter__` makes is compatible with all existing code that relies on iterators.

This is a recurring concept in software development: conventions make it possible to define new functions/classes/... that fit in a greater whole.
In certain programming languages, it is actually possible to make this intention explicit and ask the language "Did I implement this class correctly? I want it to be iterable."
This is the case with Python: you can _optionally_ make your intention known and ask Python to check your code.
Other languages such as C++, C#, Java, TypeScript _demand_ that you make such intentions clear and will refuse to run your code if you don't.

## Task

You probably have encountered `range` before.
In older versions of Python (pre 3.0), `range` would simply return a list:

```python
# pre Python 3.0
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

However, for large ranges, creating this list would take time and memory.
From Python 3.0 on, `range` is actually a class.

Say you iterate over a `range` object:

```python
for i in range(10):
  # ...
```

Here, `range(10)` creates a `range`-object.
This object is _iterable_, but not an _iterator_.
The `for`-loop needs an _iterator_`, so it uses `iter` to have the iterable create an iterator.
Calling `next` on this iterator produces all the elements of the range.

Create your own `InclusiveRange` (= iterable) and accompanying `InclusiveRangeIterator` (=iterator) class.
It should be usable as follows:

```python
>>> for i in InclusiveRange(1, 5)
...     print(i)
1
2
3
4
5
```

For this to work, `InclusiveRange` needs an `__iter__` method that returns a `InclusiveRangeIterator` object.
`InclusiveRangeIterator` should implement `__iter__` (just have it return `self`) and `__next__`.

Note that `InclusiveRange` should be reusable, but `InclusiveRangeIterator` should be single use:

```python
>>> r = InclusiveRange(1, 5)
>>> list(r)
[1, 2, 3, 4, 5]

>>> list(r)
[1, 2, 3, 4, 5]


>>> iterator = iter(r)
>>> list(iterator)
[1, 2, 3, 4, 5]

# We've used up the iterator, so no more elements are generated by it
>>> list(iterator)
[]
```
