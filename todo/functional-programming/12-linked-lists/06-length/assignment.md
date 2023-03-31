# Length

Being able to determine the length of a linked list seems useful.
We would like the syntax to remain idiomatic, meaning we want to be able to write `len(linked_list)` to compute the number of `Node`s in `linked_list`.
There's a small snag: the empty linked list is represented by `None`, so `len(None)` should evaluate to `0`.
However, `None` is built-in and we can't change its behavior.

Instead of using `None`, we'll have to introduce a new object that represents the empty list:

```python
class Empty:
    pass
```

For now, `Empty` has no members.
[`pass`](https://docs.python.org/3/tutorial/controlflow.html#pass-statements) does nothing: Python mandates it because it wants you to make "emptiness" explicit.
For example, `while True: pass` is a endless loop that does nothing but loop around.

We used to represent `[1, 2, 3]` as

```text
Node[1] --> Node[2] --> Node[3] --> None
```

Now, we replace the last component by `Empty`:

```text
Node[1] --> Node[2] --> Node[3] --> Empty
```

Technically, we should ask you to rewrite `create_linked_list` one more time, but we'll spare you that.
A possible implementation would be

```python
def create_linked_list(xs):
    result = Empty()
    for x in reversed(xs):
        result = Node(x, result)
    return result
```

So now we have two classes to represent linked lists: `Node` and `Empty`.

## Implementing `len`

To allow users to determine the length of a linked list using `len(linked_list)`, we need to implement the [`__len__` dunder method](https://docs.python.org/3/reference/datamodel.html#object.__len__).

Copy the code for `Node` and `Empty` from `linkedlist.py` to `student.py`.
Add a member `__len__` to both classes.
Don't rely on a loop to implement `Node.__len__`.
Instead, use recursion: ask the tail (the linked list pointed to by `next`) for its length and add `1` to it.
