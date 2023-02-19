# Assignment

Write a function `is_increasing(ns)` that checks if each value in `ns` is not greater than its successor.
For example, `is_increasing([1, 2, 3, 4, 4, 7])` should return `True`, whereas `is_increasing([1, 3, 2, 4])` should return `False`.

There are many ways to implement this.
Normally we don't push for a specific implementation, but for this exercise we'll insist that you work a certain way.

* You start off with `ns`.
  Let's take `ns = [1, 2, 3]` as a working example.
* Construct a new list, say `ms`, equal to `ns`, except that the first element has been dropped.
  In the case of our working example, `ms` should be equal to `[2, 3]`].
* Pair up the elements of `ns` and `ms`.
  This gives us `[(1, 2), (2, 3)]`.
  As you can see, every element is teamed up with its successor.
* Go through this list and check that every element is not greater than its successor.
