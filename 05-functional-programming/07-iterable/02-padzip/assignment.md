# Zip

As explained before, `zip` is a built-in function that pairs up corresponding elements in two or more iterables:

```python
>>> list(zip('abcd', [1, 2, 3, 4]))
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]

>>> list(zip('abcd', [1, 2, 3, 4], 'xyzw'))
[('a', 1, 'x'), ('b', 2, 'y'), ('c', 3, 'z'), ('d', 4, 'w')]
```

Note the surrounding call to `list`: this is necessary because `zip` returns an iterator object.

```python
>>> zip('abcd', [1, 2, 3, 4])
<zip object at 0x00000273D6895BC8>
```

Adding `list` forces the iteration over all the elements and stores them in a list, allowing us to see the elements printed out.

What happens when we call `zip` to iterables of unequal size?

```python
>>> list(zip('abcde', [1, 2, 3]))
[('a', 1), ('b', 2), ('c', 3)]
```

It seems that `zip` stops as soon as one of its arguments runs out of elements.

## Task

Write a iterator class `PadZip` that continues producing tuples as long as the _longest_ provided iterable is not empty.
Where values are missing, `None` is added:

```python
>>> list(PadZip('abcde', [1, 2, 3]))
[(a, 1), (b, 2), (c, 3), (d, None), (e, None)]
```

We want to be able to define our own padding value:

```python
>>> list(PadZip('abcde', [1, 2, 3], padding=0))
[(a, 1), (b, 2), (c, 3), (d, 0), (e, 0)]
```

As you can see, the constructor's parameters are

* An iterable object `left`
* An iterable object `right`
* An optional `padding` that defaults to `None`

Note that a `PadZip` object will be an _iterator_, not an _iterable_, meaning it's single use (just like `zip` is):

```python
>>> xs = PadZip('abc', 'xyz')

# First time works
>>> list(xs)
[('a', 'x'), ('b', 'y'), ('c', 'z')]

# Second time does not
>>> list(xs)
[]
```

This means `PadZip` needs the following methods:

* `__iter__` simply returns `self`: for this exercise we don't make a separate iterable class, only an iterator class
* `__next__` returns the next pair

**Hint** You'll need to be able to detect whether an iterator has run out of elements.
For this, you'll have to catch the `StopIterator` exception:

```python
try:
    next_element = next(iterator)
except StopIterator:
    # no elements remain
```
