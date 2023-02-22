# Abstract Properties

Methods can be declared abstract, and so can properties.

```python
from abc import ABC, abstractmethod


class ParentClass(ABC):
    @property
    @abstractmethod
    def foo(self):
        ...
```

## Task

Write the following classes:

* Start with a `Shape` class.
  This class must demand that all its subclasses have two properties named `area` and `perimeter`.
  Since it makes no sense to implement these properties at this point, you should make them abstract.
* Create a `Rectangle` class as a subclass of `Shape`.
  It should have two attributes: `width` and `length`, both of which must be initialized using constructor parameters.
  Since `Shape` demands it, you must also implement the `area` and `perimeter` properties.
* Create a `Square` class as a subclass of `Rectangle`.
  Its constructor should have only one parameter named `side` and use it to call `Rectangle`'s constructor.
  You don't need to implement `area` and `perimeter` since `Square` already inherits implementations from `Rectangle`.
* Create a `Circle` class.
  Determine for yourself what it needs.

## Formulae

In case you forgot the formulae for area and perimeter:

| Shape | Perimeter | Area |
|-|-|-|
| Rectangle | 2 &times; (`width` + `height`) | `width` &times; `height` |
| Square | 4 &times; `side` | `side`<sup>2</sup> |
| Circle | 2 &times; &pi; &times; `radius` | &pi; &times; `radius`<sup>2</sup> |


