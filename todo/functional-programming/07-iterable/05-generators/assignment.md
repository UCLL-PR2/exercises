# Generators

Say we want to have a "list" of all numbers starting from 0.
A naive approach would be

```python
def integers():
    result = []
    current = 0
    while True:
        result.append(current)
        current += 1
    return result
```

This of course doesn't work: the loop never ends.
In essence, running this function will just eat up your RAM at high speed.

But thanks to iterators, we can deal with infinite sequences!

```python
class Integers:
    def __init__(self):
        self.__current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__current += 1
        return self.__current
```

Implementing it as an iterator class is not straightforward, especially if the logic becomes more involved.
Since iterators are quite a common pattern in code, many programming languages, among which Python, provide an easier way to implement iterators.
Python offers help in the form of _generator functions_, or _generators_.

To better understand generators, think of what iterators actually do: they're nothing more than objects that return a "list" one element at a time.
It's like having a function, but which instead of returning one value, it should be able to return many.
And that is exactly what generators do.

```python
def integers():
    current = 0
    while True:
        yield current
        current += 1
```

This looks an awful lot like a function, but notice the `yield`.
The presence of this `yield` is what promotes this function to a generator function.

When a (regular) function `return`s a value, the function ends there and then, and all local variables are cleaned up.
Control goes back to the caller, who receives whatever value has been returned by the function.

`yield` works differently: it does also interrupt the function, but all local variables are still kept in memory.
What's more: the generator also remembers the exact location where the execution ended.
This allows a generator to be _resumed_, meaning that it will continue just after the `yield`.

The idea is that when we call a generator function, we get an iterator object.
When we call `next` on this iterator, the generator function's body is executed until the first `yield` is encountered.
Whatever is `yield`ed is used as the result of `next`.
Thus the generator generated the first element of the sequence.

In order to get the second element, we call `next` a second time on the iterator.
Execution of the generator's body _resumes_ and it will run until it encounters a second `yield`.
This produces the second value of the sequence and is returned by `next`.

## Example

Let's add some `print`s to make it clear what gets executed when.

```python
def integers():
    print("Init")
    current = 0
    print("Starting loop")
    while True:
        print(f"Yielding {current}")
        yield current
        print(f"Incrementing current from {current} to {current+1}")
        current += 1

>>> ns = integers()
# Nothing is printed! The body as NOT executed


# Let's see what ns contains
>>> ns
<generator object integers at 0x00000273D689F148>
# This is actually an iterator (i.e., it implements __iter__ and __next__)


# We ask for the first element in the sequence
>>> next(ns)
Init
Starting loop
Yielding 0
0
# The generator's body has only now actually started executing
# It ran until the first yield
# 0 is the value that it yielded and is what is returned by `next(ns)`
# Make sure to understand that the first three lines are printed,
# whereas the last (0) is the return value of next(ns)


# Let's ask for the second element
>>> next(ns)
Incrementing current from 0 to 1
Yielding 1
1
# As you can see, the execution has resumed immediately after the yield
# The local variable current is incremented
# Then it loops back and yields 1


>>> next(xs)
Incrementing current from 1 to 2
Yielding 2
2

>>> next(xs)
Incrementing current from 2 to 3
Yielding 3
3
```

## Finite Generator

In our example, the generator goes on forever.
But what would happen in this case?

```python
def foo():
    yield 1
    yield "deux"
    yield "three"
```

Here, the function only `yield`s three values.

```python
>>> iterator = foo()
>>> next(iterator)
1

>>> next(iterator)
"deux"

>>> next(iterator)
"three"

>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

The fourth time `next` is called, there are no more `yield`s in the generator function.
This is seen as the end of the sequence, and `StopIteration` is raised to signal this.

## Summary

The central idea behind generator is that they are used to define a sequence of values.
We distinguish two facets: _defining_ a generator and _using_ a generator.

### Defining

A generator is a function that `yield`s each value of the sequence.

### Usage

Calling a generator function produces an iterator object.
We can use `next` repeatedly to retrieve each value of the sequence in turn.

## Task

Define a generator `repeat(value)` that generates an infinite repetition of the same `value`.

```python
>>> iterator = repeat(5)
>>> next(iterator)
5

>>> next(iterator)
5

>>> next(iterator)
5

>>> next(iterator)
5
```
