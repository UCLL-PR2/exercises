# FAQ

## Assertions

**Should I use `assert` to validate parameters?**

`assert` is meant for debugging, as explained on the [official site](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement).

Typically, programs can run in two modes:

* **Debug mode**: extra checks are performed, making the application run slower but making it easier to find bugs.
* **Release mode**: the code is optimized, making it run faster, but if something goes wrong, it's harder to know why.

An `assert`ion only runs in debug mode.
Therefore, your code should never depend on `assert` for important things, such as parameter validation.

---

**When should I use `assert`?**

`assert` is often used in tests: these run in debug mode (it wouldn't make any sense to run them in release mode) so we are certain that assertions will be checked.

You can also use `assert` for sanity checks.
Say you are writing a `sort` function.
Sorting is a nontrivial algorithm and things can easily go wrong.
It can therefore be helpful to have the `sort` function check its own results:

```python
def sort(lst):
    # Algorithm that sorts lst and stores it in result

    # Check result
    assert is_sorted(result)
    assert contain_same_elements(lst, result)

    # Return result
    return result
```

This way, every time you call `sort`, the code performs a "self check".
If your code fails to sort `lst` correctly, you'll immediately get a big `AssertionError` thrown at you.
This is A Good Thing: [Fail-Fast](https://en.wikipedia.org/wiki/Fail-fast) truly is your friend.

While these self-checks can slow down your program considerably, remember that you can turn off assertions by running your program in release mode.

Assertions work well because it turns out that _checking_ a solution is often much simpler than _finding_ a solution.
For example, we can implement the two checks as

```python
def is_sorted(xs):
    return all(x <= y for x, y in zip(xs, xs[1:]))

def contain_same_elements(xs, ys):
    return Counter(xs) == Counter(ys)
```

---

## Classes

**How should I implement `__eq__`?**

`__eq__` is the dunder method that corresponds to the `lhs == rhs` operator.
It is a binary operator, i.e., it takes two operands.

Since `__eq__` is always defined in class, say `C`, this means you always know something about the type of the left operand: it is an object of type `C`, or of a child class of `C`.

The right operand is trickier though: it can be _anything_.
The first thing you'll probably want to do is to determine its type.
When you're implementing a class `C`, you should have an idea which other object a `C` object could be equal to.
Generally, you'll only want to compare your `C` object with other `C` objects.
For example, a `Person` object can only be equal to other `Person` objects.

The first thing you'll do then is to check the type of the right operand:

```python
class C:
    def __eq__(self, rhs):
        if isinstance(rhs, C):
            # We know rhs has type C, we can use this information to compare self with rhs
        else:
            ???
```

Your `__eq__` could also be able to check equality with other types of objects, so feel free to go through a list of other types:

```python
class C:
    def __eq__(self, rhs):
        if isinstance(rhs, C):
            # ...
        elif isinstance(rhs, str):
            # ...
        elif isinstance(rhs, list):
            # ...
        else:
            ???
```

Don't overdo this, however.
The meaning of your `__eq__` should be intuitive and meaningful.
You should definitely not try to make it overly flexible by allowing comparison with all kinds of type.
Sometimes being strict and rigid is the best way to go.

What to do if `rhs` has a type you don't support?
For example, it makes little sense to compare a `Person` with a `list`.
You could simply return `False`.
There is a better solution though, and that is to return `NotImplemented`.

Let's do a little experiment:

```python
class Foo:
    def __eq__(self, rhs):
        if isinstance(rhs, Foo):
            return True
        else:
            return NotImplemented

>>> foo = Foo()
>>> foo == 5
False
```

This should surprise you: we compare a `Foo` object with `5`, for which your `__eq__` method returns `NotImplemented`, not `False`.
Why does `foo == 5` not evaluate to `NotImplemented`?

As explained [on the official Python pages](https://docs.python.org/3/library/constants.html#NotImplemented), when you evaluate `x == y`, Python will cann `x.__eq__(y)`.
If this returns `NotImplemented`, Python will instead try out `y.__eq__(x)`.
If this again returns `NotImplemented`, the `x == y` will evaluate to `False`.

> The documentation is not completely accurate: it claims that if both `x.__eq__(y)` and `y.__eq__(x)` return `NotImplemented`, an exception will be raised.
> This is not the case, as is pointed out by [this discussion](https://bugs.python.org/issue39111).
> It is true however for other binary operators.

Why does Python operate like this?
Why would `y.__eq__(x)` yield a different result?
Wouldn't that simply be inconsistent?

Consider the following code:

```python
class Foo:
    def __eq__(self, rhs):
        if isinstance(rhs, Foo):
            return True
        else:
            return NotImplemented


class Bar:
    def __eq__(self, rhs):
        if isinstance(rhs, Bar):
            return True
        if isinstance(rhs, Foo):
            return True
        return False
```

In this case, `Foo() == Bar()` would return `True`.
But if this is what we want, why doesn't `Foo.__eq__` simply return `True` instead of `NotImplemented` when comparing to a `Bar`?

The `Foo` and `Bar` classes are not necessarily defined at the same time.
At the time someone wrote `Foo`, `Bar` may not have existed, so there was no reason for it to add code for it in `Foo.__eq__`.
Maybe only much later, `Bar` was added and it was decided that `Foo`s and `Bar`s should be the same.

Maybe you're wondering if it wouldn't be better to simply update `Foo.__eq__` when `Bar` was added.
This would indeed be a cleaner solution and we wouldn't need this `NotImplemented` trickery, but updating `Foo` might not be an option.
Maybe it's part of a library, maybe the company doesn't like modifying well-tested code, etc.

Say you develop a `Fraction` class.
The fraction 2/3 would be written `Fraction(2, 3)` in Python code.
You would probably want to allow `Fraction`s to be compared to `int`s and `float`s.
For example, you would like `1` to be considered equal to `Fraction(2, 2)`.

Having `Fraction(2, 2) == 1` is easy to achieve, as this calls `Fraction.__eq__`, which is under your control.
However, for `1 == Fraction(2, 2)` to be `True`, you'd have to somehow be able to update `int.__eq__`, but that's not possible.
Thanks to `NotImplemented` however, this is not necessary: `1.__eq__(Fraction(1, 1))` will return `NotImplemented`, causing `Fraction(1, 1).__eq__(1)` to be evaluated next, which can return `True`.

---

**Should I check parameter types using `isinstance`?**

Short answer: no.

Now for the long answer...
Say we want to write our own `sum` function.
(Yes, we know it already exists, but it makes for a good example.)
A possible definition would be

```python
def sum(lst):
    result = lst[0]
    for elt in lst:
        result += elt
    return elt
```

Now, of course, it makes no sense to call `sum` on a string, so we can try to impose limitations on `lst`'s type.
We insist `lst` must a a `list`:

```python
def sum(lst):
    if not isinstance(lst, list):
        raise TypeError('lst must be a list')
    result = 0
    for elt in lst:
        result += elt
    return elt
```

Okay, this prevents us from passing `sum` strings, `Person`s or other weird things as argument.
However, we can still pass a list of, say, `Person`s...
Those are not particularly summable.
Maybe we should check the elements' type too.

```python
def sum(lst):
    if not isinstance(lst, list):
        raise TypeError('lst must be a list of ints')
    if not all(isinstance(elt, int) for elt in lst):
        raise TypeError('lst must be a list of ints')
    result = 0
    for elt in lst:
        result += elt
    return elt
```

There.
Now `sum` should be fool proof.
Only `list`s of `int`s.

But what if we have a _tuple_ of `int`s?
Should we really rewrite a separate `sum` function to deal with tuples?
It would be exactly the same code!

Okay, let's add some flexibility to our existing `sum`:

```python
def sum(lst):
    if not isinstance(lst, list) and not isinstance(lst, tuple):
        raise TypeError('lst must be a list or tuple of ints')
    if not all(isinstance(elt, int) for elt in lst):
        raise TypeError('lst must be a list or tuple of ints')
    result = 0
    for elt in lst:
        result += elt
    return elt
```

So, it can be a list or a tuple of `int`s.
But what about `set`s?
Okay, here we go again...

```python
def sum(lst):
    if not isinstance(lst, list) and not isinstance(lst, tuple) and not isinstance(lst, set):
        raise TypeError('lst must be a list or tuple or set of ints')
    if not all(isinstance(elt, int) for elt in lst):
        raise TypeError('lst must be a list or tuple or set of ints')
    result = 0
    for elt in lst:
        result += elt
    return elt
```

Surely we're done now.
Well, not really.
What about a list of `float`s?

```python
def sum(lst):
    if not isinstance(lst, list) and not isinstance(lst, tuple) and not isinstance(lst, set):
        raise TypeError('lst must be a list or tuple or set of ints or floats')
    if not all(isinstance(elt, int) or isinstance(elt, float) for elt in lst):
        raise TypeError('lst must be a list or tuple or set of ints or floats')
    result = 0
    for elt in lst:
        result += elt
    return elt
```

But then there's also `Fraction`s that are addable.
And `complex`s.
And vectors.
And matrices.
And quaternions!

This is becoming ridiculous.
We need something... saner.

Right now we are checking that our arguments have specific *types*, but this is actually the wrong approach.
We want to focus on the _operations_ available on the arguments instead of their types.

For example, we need to be able to _iterate_ over `lst` using a `for` loop.
We don't care if it's a list, or a set, or a tuple, or anything else: we just want it to be iterable.
Something can be looped over if it has a `__iter__` method, so that's what we need to look for.

```python
def sum(lst):
    if not hasattr(lst, '__iter__'):
        raise TypeError()
    if not all(isinstance(elt, int) or isinstance(elt, float) for elt in lst):
        raise TypeError()
    result = 0
    for elt in lst:
        result += elt
    return elt
```

The elements of `lst` should be addable, so they need a `__add__` method.

```python
def sum(lst):
    if not hasattr(lst, '__iter__'):
        raise TypeError()
    if not all(hasattr(elt, '__add__') for elt in lst):
        raise TypeError()
    result = 0
    for elt in lst:
        result += elt
    return elt
```

But what if `lst` contains a mix of matrices and `int`s?
Both have an `__add__` method, but it will not be happy with its argument types: matrices only want to be added to matrices, not with `int`s.

As you can see, it becomes quite complex.
We need many checks, which makes the code both unwieldy and inefficient.
Added to this, if we didn't check, we'd still be receiving an error message down the road.
For example, using a `for` loop on `lst` will call `__iter__`, so the check does happen, just a little bit later.
It's not perfect (e.g., it's not [fail-fast](https://en.wikipedia.org/wiki/Fail-fast)), but it's something.

There are actually programming language that support [static type checking](https://en.wikipedia.org/wiki/Type_system#Type_checking).
These languages do check all types, and they do so at zero efficiency cost.
However, Python is a dynamically typed language.
It's less robust, but more flexible.
It's a choice.

There is actually a [way](https://peps.python.org/pep-0484/) to add static type checking to Python.
It's not perfect and sometimes clumsy, but it does help.

**How should I build strings?**

**What's the difference between `__str__` and `__repr__`?**
