# Assignment

Write a function `remove_duplicates(xs)` that returns a new array equal to `xs` but with duplicated elements removed.
The elements in the result must appear in the same order as in `xs`.

Since the order of the elements in the result is of importance, you can't simply put the elements in a set: this effectively throws away all information regarding order.

This exercise contains two kinds of tests:

* There are tests that check that your implementation produces the right results.
* There is a test that checks whether your implementation runs fast enough.

If this latter test fails, you'll get a timeout error message.
You'll have to think of how you can harness sets to make your code fast.
