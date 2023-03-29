# Linked Lists

As explained before, functional programming is about immutability.
Let's now explore what this means for our different collections.

By now you must be well acquainted with `list`, `set` and `dict`.
These collections can be used in a functional setting: you simply have to refrain from using destructive operations.

| Nondestructive | Destructive |
|:-:|:-:|
| `lst1 + lst2` | `lst1.extend(lst2)` |
| `len(lst)` | |
| `[*lst, elt]` | `lst.append(elt)` |
| `lst[:-1]` | `lst.pop(elt)` |
| `[*lst[:index], elt, *lst[index:]]` | `lst.insert(elt, index)` |
| `sorted(lst)` | `lst.sort()` |
| `reversed(lst)` | `lst.reverse()` |

Python offers immutable versions of lists: tuples.
Similarly, [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset) is a readonly `set`.
`dict`s don't really have a built-in immutable counterpart ([`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple) comes closest.)

However, these collections are not optimized for use in a functional setting.
For example, say we want to modify the first element of a long list:

```python
# Imperative
>>> lst[0] = new_value

# Functional
>>> updated_lst = [new_value, *lst[1:]]
```

The functional approach needs to copy all but one element from the original list.
This is inefficient both in time and space (i.e., memory).
We'll need some new ways of organizing our data if we want to keep our functional programs efficient.

## Train and Wagons

Let's talk trains.
At the front of a train, there's a locomotive.
Attached to the locomotive, we have a wagon.
And attached to this wagon, we have _another_ wagon.
We can continue attaching as many wagons as we want as long as the locomotive is powerful enough to pull them forward.

Let's see how we could model this:

```python
class Locomotive:
    def __init__(self):
        self.first_wagon = None


class Wagon:
    def __init__(self):
        self.next_wagon = None
```

Let's now create a train with three wagons:

```python
# Create objects
>>> locomotive = Locomotive()
>>> wagon1 = Wagon()
>>> wagon2 = Wagon()
>>> wagon3 = Wagon()

# Attach them into a train
>>> locomotive.first_wagon = wagon1
>>> wagon1.next_wagon = wagon2
>>> wagon2.next_wagon = wagon3
```

Make sure you understand how the objects are organized:

```text
locomotive -> wagon1 -> wagon2 -> wagon3
```

## Turning Trains into Lists

First, let's forget about the locomotive: we don't really need it here.
This leaves us with just the wagons.
Next, let's rename `Wagon` in something more generic, like `Node`.

```python
class Node:
    def __init__(self):
        self.next = None

>>> node1 = Node()
>>> node2 = Node()
>>> node3 = Node()

>>> node1.next = node2
>>> node2.next = node3
```

We have the same structure as a train, but we made it more abstract.

Right now, a `Node` feels a bit... empty.
Let's allow adding some data to a node:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

>>> node1 = Node('A')
>>> node2 = Node('B')
>>> node3 = Node('C')

>>> node1.next = node2
>>> node2.next = node3
```

If we represent this visually, we have

```text
Node(A) --> Node(B) --> Node(C)
```

This eerily resembles a list with elements `'A'`, `'B'` and `'C'`.

This new way of organizing data (i.e., having nodes that form a sort of train/chain) is called a _linked list_.

## Task

Write a function `create_linked_list(xs)` that receives an iterable `xs` and returns a linked list containing the same elements.
Returning a linked list is done by returning its first node.
An empty linked list is represented by `None`.

For example, `create_linked_list([1, 2, 3])` needs to create three `Node` objects, assign them the values `1`, `2` and `3`, chain the `Node`s together and return the first `Node`, i.e., the one whose `value` equals `1`.

The `Node` class is given in the `linkedlist.py` file.
Import it in your `student.py` file.
