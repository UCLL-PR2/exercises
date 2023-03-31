# Concatenation

Concatenation refers to the operation of "chaining" two lists together.
For example, the concatenation of `[1, 2, 3]` and `[4, 5, 6]` is the _new_ list `[1, 2, 3, 4, 5, 6]`.

Let's compare the memory consumption of regular Python lists and linked lists.
Using regular Python lists, there are three distinct lists in memory: `[1, 2, 3]`, `[4, 5, 6]` and `[1, 2, 3, 4, 5, 6]`.
With linked lists, it's a different story.

```python
xs = Node.from_iterable([1, 2, 3])
ys = Node.from_iterable([4, 5, 6])
zs = xs + ys
```

We start off with two lists:

```text
xs
v
Node[1] --> Node[2] --> Node[3] --> Empty

Node[4] --> Node[5] --> Node[6] --> Empty
^
ys
```

Next, we want to end up with the list

```text
zs
v
Node[1] --> Node[2] --> Node[3] --> Node[4] --> Node[5] --> Node[6] --> Empty
```

However, the last three objects (`4`, `5`, `6` and `Empty`) already exist in memory.
It is safe to reuse them for our concatenation list, as we know they can't change.

```text
xs
v
Node[1] --> Node[2] --> Node[3] --> Empty

zs                                  ys
v                                   v
Node[1] --> Node[2] --> Node[3] --> Node[4] --> Node[5] --> Node[6] --> Empty
```

## Task

Implement the dunder method `__add__` so that `linked_list1 + linked_list2` evaluates to the concatenation of the operands.
