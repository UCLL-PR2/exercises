# Inheritance
# Abstract Methods

Let's revisit the chess example from the previous exercise.
The end result looked a bit like this:

```python
class ChessPiece:
    # Some code (omitted)

    def move(self, new_position):
        if not is_legal_move(new_position):
            raise ValueError('invalid move')
        self.__position = new_position


class Pawn(ChessPiece):
    def is_legal_move(self, new_position):
        # Some code (omitted)


class King(ChessPiece):
    def is_legal_move(self, new_position):
        # Some code (omitted)
```

For this explanation, it is important to notice that `ChessPiece`'s code relies on the existence of a method named `is_legal_move`, which is only getting defined in the child classes.

## Abstract Classes

What happens if we do this?

```python
piece = ChessPiece(Position(0, 0), 'white')
```

This is kind of nonsensical: we create a chess piece, but we remain vague about which one it is.
Is it a king, a pawn, a queen, a rook, ...?
No, it's just ... _a piece_.
It's as if you go to a restaurant and ask the waiter for literally "a menu item".
It makes no sense; you need to be more specific.

Also, if you were to try to move this `piece`:

```python
piece = ChessPiece(Position(0, 0), 'white')
piece.move(Position(4, 4))
```

Again, utter nonsense: in order to check whether it's a valid move, you need to know what piece it is.
A queen or bishop would be allowed to make that move, but other pieces wouldn't be.

Python would also not be happy: `move` calls `is_legal_move`, but this method is not defined in `ChessPiece`.
You would simply get an `AttributeError` thrown at you.

We want to be able to express that `ChessPiece` on its own is merely an abstract concept, a "dummy" class that acts as a parent to other classes.
We do this as follows:

```python
from abc import ABC


class ChessPiece(ABC):
    # some code
```

Here, `ABC` stands for [_Abstract Base Class_](https://docs.python.org/3/library/abc.html).
Base class is a synonym for parent class.

Does this solve our problem?
If we try to create a `ChessPiece` object, no error is thrown, so it didn't really help much.
However, it is a required step towards our goal of forbidding `ChessPiece` to be instantiated.

## Abstract Methods

As mentioned earlier, `ChessPiece` relies on `is_legal_move`.
However, this is not immediately apparent: you have to sift through the code and notice that somewhere in there there's a call to a nonexistent method.
It'd be better to make it explicit that there's a "hole" in the class.

```python
from abc import ABC, abstractmethod


class ChessPiece(ABC):
    @abstractmethod
    def is_legal_move(self, new_position):
        ...
```

**Important**
> We wish to point out that `...` is literally the code that needs to be there.
It's not a way of omitting uninteresting details: the actual code contains three dots.

Using `@abstractmethod` we have made clear that `ChessPiece` needs `is_legal_move` to be implemented.
Let's now try to instantiate `ChessPiece`:

```text
>>> piece = ChessPiece(Position(0, 0), 'black')
TypeError: Can't instantiate abstract class ChessPiece with abstract method is_legal_move
```

Great!
This is exactly what we want.

## Task

The exercise is a bit of a puzzle and focuses on the actual rules regarding abstract classes and methods.
Copy the code from `startercode.py` to `student.py`.
Make the necessary classes and method abstract.

A summary of the rules to follow:

* If a class invokes methods on itself that it does not have, it must be abstract.
* If a class invokes a method `x` and the class does not have such a member, add a declaration for `x` to that class.
