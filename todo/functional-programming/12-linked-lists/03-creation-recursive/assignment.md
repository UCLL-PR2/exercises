# Recursive Creation

At the point of this writing, we have no clue as to what your solution to the previous exercise looks like, so we'll just have to go with our solution:

```python
def create_linked_list(xs):
    result = None
    for x in reversed(xs):
        result = Node(x, result)
    return result
```

In this code, `result` is being assigned to multiple times.
This counts as mutation.
Can't have that, can we now?

> Note: in reality, it's not really necessary to always be this strict.
> It just makes a good exercise.

## Task

Write a new version of `create_linked_list(xs)` that uses _no_ mutation whatsoever.
We suggest you use recursion.

We guarantee that `xs` is either a `list` or a `tuple`.
It's definitely possible to implement it for iterables in general, but it adds some complications.
We'd rather you focus on a clean recursive algorithm.

### Hint

Recursion is always finding a way to delegate most of the work.
Say you receive `[1, 2, 3, 4]` and need to convert it to a linked list.

We could say, let's someone else create the linked list for `[1, 2, 3]`, then we only need to add `4` at the end.
However, adding an extra `Node` to a linked list requires mutation: we would need to modify the `next` of the `Node` carrying `3`.

Another approach would be to delegate the creation of `[2, 3, 4]`.
Then we only need to add `1` in front.
This is easy to do using `Node`.

So, a recursive algorithm would operate as follows (we take `[1, 2, 3, 4]` as example, it's up to you to generalize):

* We take the first element (`1`) and store it in a variable, let's say `head`.
* We take the remaining elements (`[2, 3, 4]`), and store it in a variable `tail`.
* We want to delegate the work on `[2, 3, 4]`.
  This is done using a recursive call: we call `create_linked_list` on `tail`, giving us a linked list containing `2`, `3` and `4`.
* Finally, we only need to create an extra `Node` carrying `1`.

With recursion, there must always be a case where no delegation is necessary, lest we end up with infinite recursion.
For what value of `xs` is it trivial to create a linked list?
Intercept this case with an `if` and have it return the correct value directly.
