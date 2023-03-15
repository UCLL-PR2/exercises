# Sorting

Python comes with two standard ways of sorting lists:

```python
>>> ns = [1, 3, 9, 7, 8, 4, 6, 2, 5]

# sorted returns a *new* list
>>> sorted(ns)
[1, 2, 3, 4, 5, 6, 7, 8, 9]

# ns is left untouched by sorted
>>> ns
[1, 3, 9, 7, 8, 4, 6, 2, 5]

# You can also sort in-place
>>> ns.sort()
>>> ns
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Which one you need depends on your needs.

Now, how do `sort`/`sorted` decide what order to put the list's values in?
With numbers, it might seem intuitive to order them from smallest to greatest, but what about strings?
Alphabetically seems standard, but case sensitive or insensitive?
Should spaces count or be ignored?
And what if we sort `Person`s, `Item`s, `ChessPiece`s?

## `__lt__`

By default, sorting will rely on the `<` operator: if `x < y`, then `x` belongs to the left of `y` in the sorted list.
If you want to be able to sort a list of `Person`s, you will have to give meaning to `person1 < person2`.
You can achieve this by defining the `__lt__` method:

```python
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __lt__(self, other):
        return self.name < other.name
```

Here, we say that a `Person` is "less than" another `Person` is the former's name is "less than" the latter's name.
`<` on strings corresponds to alphabetical case sensitive order: for example, `A < B` and `Z < a`.

This approach is a rather constraining though: we can only define a single sorting order.
We can easily imagine wanting multiple sorting orders on `Person`s: by name, by age, by weight, etc.

## `key`

Both `sort` and `sorted` can take an extra [(keyword) parameter](https://docs.python.org/3/glossary.html#term-argument) `key`: you give it a function that for each element in the list returns the actual value to be used in the sorting process.
For example,

```python
cards.sort(key=lambda card: card.value)
```

Here, the `key` function returns a card's value.
This tells `sort` that the cards should be ordered by value.
If you wanted to sort them by suit, you could write

```python
cards.sort(key=lambda card: card.suit)
```

## Sorting by Two (or More) Values

Say you want to sort your cards by suit, but if they have the same suit, they should be ordered by value.
You can achieve this easily by relying on tuples.

Tuples come with a built-in order.
Consider how to determine if `(a, b) < (c, d)` evaluates `True`:

* First, the first elements are compared: if `a < c`, then `True` is returned.
  If `a > c`, `False` is returned.
* If, however, `a == c`, then the focus shifts on the second elements of the pairs.
  If `b < d`, then `True` is returned.
  If `b > d`, then `False` is returned.
* Since there are no third elements to look at, the comparison ends here and `False` is returned.
  If there had been third, fourth, ... elements, they would have been compared in turn.

So, if we construct a tuple `(card.suit, card.value)` we will get exactly what we desire: first the `suit`s will be compared and if they are equal, the `value`s will be considered.

```python
# Sorts first by suit, then by value
cards.sort(key=lambda card: (card.suit, card.value))
```

## `attrgetter`

In case you find yourself writing many `lambda obj: obj.member` methods, know that there's a quicker way:

```python
from operator import attrgetter


cards.sort(key=attrgetter('suit'))
```

`attrgetter(id)` constructs a function for you, one that takes a function and returns the value of its member called `id`.
In the code shown above, the cards will be sorted by their suit.
In other words

```python
attrgetter('foo')

# is the same as

lambda obj: obj.foo
```

## Task

Write the following functions.
Each function must leave its argument unmodified and return a new list.

* `sort_by_age(people)` orders the `Person`s by increasing `age`.
* `sort_by_decreasing_age(people)` orders the `Person`s by decreasing `age`.
* `sort_by_name(people)` orders the `Person`s by `name`, alphabetically.
* `sort_by_name_then_age(people)` orders the `Person`s by `name`, and in case of equal `name`s, by increasing `age`
* `sort_by_name_then_decreasing_age(people)` orders the `Person`s by `name`, and in case of equal `name`s, by decreasing `age`
