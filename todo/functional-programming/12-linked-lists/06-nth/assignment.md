# Nth Element

We want to be able to get the `n`th item using `linked_list[n]`.

Implement the dunder method `__getitem__` on both `Node` and `Empty`.
If the index is invalid, raise a `IndexError`.

Again, rely on recursion.
Hint: the 3rd element of `[1, 2, 3, 4, 5]` is also the 2nd element of `[2, 3, 4, 5]`.
