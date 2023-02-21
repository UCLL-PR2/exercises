# Inheritance

## Duplication in Functions

Say you have the following two functions:

```python
def smallest_sum(ns):
    sums = (
        x + y
        for x in ns
        for y in ns
    )
    return min(sums)


def greatest_sum(ns):
    sums = (
        x + y
        for x in ns
        for y in ns
    )
    return max(sums)
```

As you can see, they both compute the same `sums`.
Generally, you should really avoid duplication.
Shared code should be factored out as follows:

```python
def compute_sums(ns):
    return (
        x + y
        for x in ns
        for y in ns
    )


def smallest_sum(ns):
    return min(compute_sums(ns))


def greatest_sum(ns):
    return max(compute_sums(ns))
```

## Duplication in Classes

Duplication can also occur on the level of classes.
To demonstrate this, let's implement a (very small) part of a chess game.

You are given a file `startercode.py`.


## Factoring Out the Common Code

The `Pawn` and `King` classes have a lot in common: they both have a `color` and `position` on which the same restrictions apply.
The only difference between both classes is how legal moves are determined.

Create a new class `ChessPiece`.
Move all common logic in this class.
In other words, a `ChessPiece` has a `color` and `position`, but of which have to obey the same rules as in `Pawn` and `King`.

Now you can remove all the shared members from `Pawn` and `King`.
Of course, they do still need all `color` and `position` related functionality, but we can say they have to _inherit_ them from `ChessPiece`.

```python
class ChessPiece:
    ...

class Pawn(ChessPiece):
    ...

class King(ChessPiece):
    ...
```

Here, `ChessPiece` is called the _base class_ for `Pawn` and `King`.
When one class inherits from another class, it essentially "copies" all of its base class's members.
It can then add extra members of its own, or even redefine some members in case it's not happy with its base class's implementation of that member.

Run the tests again.
Everything should still work exactly the same.

## Final Touches

Try to identify all shared functionality between `Pawn` and `King` and move as much as you can to `ChessPiece`.
Then compare your code with the solution.

Notice how the `move` method in `ChessPiece` calls `is_legal_move` while that method does not even exist in `ChessPiece`.
This is perfectly okay: this hole will be filled by `Pawn` and `King`.

What would happen if you create a `ChessPiece` object?

```python
piece = ChessPiece(
    position=Position(0, 0),
    color='white'
)
```
