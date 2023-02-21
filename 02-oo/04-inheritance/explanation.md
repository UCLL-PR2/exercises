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

You are given a class `Position` (see the file `position.py`).
Rely on it to represent, well, positions.

### Pawn

Create a `Pawn` class that has the following members:

* A `Pawn` has a readonly position and readonly color.
  Both these are set using the constructor.
* The `position` is valid if its `x` and `y` coordinates range from `0` to and including `7`.
* The `color` must be either `black` or `white`.
* If we try to create an `Pawn` with invalid `position` or `color`, a `ValueError` should be thrown.

Also add a `move(self, new_position)` method moves the piece to the given `new_position`.
However, it must only do so if the move is legal, otherwise it must throw a `ValueError`.

The rules are as follows:

* If the pawn is white, it can only move 'upwards' from `(x, y)` to `(x, y+1)`.
* If the pawn is black, it can only move 'downwards' from `(x, y)` to `(x, y-1)`.
* The destination should still be valid.
  For example, if a white pawn has position `(2, 7)`, there are no legal moves for it since `(2, 8)` falls outside the chess board.
  Similarly, a black pawn with position `(3, 0)` is also stuck.

Run the tests to make sure your implementation of `Pawn` is correct.
Some tests will be skipped since you haven't implemented everything yet.

### King

Create a `King` class that has the following members:

* A `King` has a readonly position and readonly color.
  Both these are set using the constructor.
* The `position` is valid if its `x` and `y` coordinates range from `0` to and including `7`.
* The `color` must be either `black` or `white`.
* If we try to create an `King` with invalid `position` or `color`, a `ValueError` should be thrown.

Also add a `move(self, new_position)` method moves the piece to the given `new_position`.
However, it must only do so if the move is legal, otherwise it must throw a `ValueError`.

The rules are as follows:

* A king can move one step in all 8 directions.
* Of course, the king must end up on the chess board, so if the king is located in a corner, it has only 3 valid moves.

Run the tests again to check your implementation.
All tests should pass.

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
When a class inherits from another class, it "copies" all of its base class members.
It can add extra members, or even _override_ its base class members by redefining them.

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
