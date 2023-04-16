# Verification

Tests typically have the form "if I give this input, then I expect this output".
This basically means that you are actually first solving the problem yourself and then expect the algorithm to agree with you.
Solving the problem yourself is not necessarily easy, so you will limit yourself to simple cases where manual solving requires little effort from your part.
This can be a bit risky: maybe your algorithm contains a bug that only shows up in more complex cases.
In this case, your tests will not catch this bug.

But maybe there are ways to avoid having to solve the problem yourself.

## Turning Things Around

Consider a function that computes the square root of a number.
Of course, you can simply use `x**0.5`, but let's pretend for the moment we're working on a platform that does not have a built-in square root operation.
We could write tests as follows:

```python
@pytest.mark.parametrize('n, expected', [
    (1, 1),
    (4, 2),
    (9, 3),
    (16, 4),
    (100, 10),
    (2, 1.41421356),
    (5785, 76.059187)
])
def test_sqrt(n, expected):
    actual = sqrt(n)
    assert approx(expected) == actual
```

However, we can easily generate this data.
We may not have `sqrt` built-in, but surely we have multiplication.
We could start off with the expected value (say `7`), square it (`49`) and then specify that `sqrt(49)` should return `7`.

```python
@pytest.mark.parametrize('n, expected', [
    (x * x, x) for x in [1, 2, 3, 4, 10, 1.41421356, 76.059187]
])
def test_sqrt(n, expected):
    actual = sqrt(n)
    assert approx(expected) == actual
```

We can make easily increase the number of inputs:

```python
@pytest.mark.parametrize('n, expected', [
    (x * x, x) for x in range(1000)
])
def test_sqrt(n, expected):
    actual = sqrt(n)
    assert approx(expected) == actual
```

Now we only consider integers.
We add some extra computation to it so as to also test using floating point numbers.
In the code below we picked `0.73` at random.

```python
@pytest.mark.parametrize('n, expected', [
    (x * x, x) for x in (x * 0.73 for x in range(1000))
])
def test_sqrt(n, expected):
    actual = sqrt(n)
    assert approx(expected) == actual
```

> You might wonder why we don't actually generate random numbers using the `random` class?
> You should never have any randomness to your tests: tests need to be reproducible.
> Once you have a failing test, you need to be able to rerun that exact same test.
> You don't want to allow it to spontaneously disappear.

## Slow Solving, Fast Verification

Some problems are hard to solve, but easy to verify.
This is the case with our square root example: we can easily check the result of `sqrt(x)` by squaring it and comparing it to `x`:

```python
@pytest.mark.parametrize('n', [
    n for n in range(1000)
])
def test_sqrt(n, expected):
    actual = sqrt(n)
    assert approx(actual * actual) == n
```

Again we can generate many tests without having to do much work.

## Tasks

Let's implement our own sorting function: you'll implement an algorithm known as [merge sort](https://en.wikipedia.org/wiki/Merge_sort).
It involves three steps.

### `split_in_two`

First, we'll need a function `split_in_two(ns)` that splits a list `ns` halfway.

```python
>>> split_in_two([1, 2, 3, 4, 5, 6])
([1, 2, 3], [4, 5, 6])
```

If the input list has an odd number of elements, one of the halves will have to contain one more element than the other half.
You are free to choose with half.
Implement this function in `mergesort.py`.

In `tests.py`, write a parametrized test function `test_split_in_two`:

* `test_split_in_two` should have one parameter, namely the list to be split.
* Use `@parametrized` to pass it lists whose length range from 0 to, say, 100.
* These input lists should contain distinct elements.
  For example, say your implementation of `split_in_two` contains a bug and splits `[a, b, c, d]` into `([a, b], [a, b])`.
  If your test uses `[0, 0, 0, 0]` as input, you'll get back (`[0, 0], [0, 0]`), which is correct.
  The bug remained unnoticed.
  However, if instead you use `[0, 1, 2, 3]`, then the bug will become apparent as you'll get `([0, 1], [0, 1])` instead of `([0, 1], [2, 3])`.
* Please don't hardcode a hundred lists.
  It is trivial to generate a hundred lists with distinct elements.
* Don't hardcode expected results either.
  Instead, have the test check two things:
  * If `split_in_two(ns)` returns `(left, right)`, then `left + right` should be equal to `ns`.
  * `left` and `right`'s lengths should differ maximally by one.

### `merge_sorted`

`merge_sorted(left, right)` expects two parameters.
Both `left` and `right` are guaranteed to be _sorted_ lists.
`merge_sorted` must efficiently combine the two lists into one big sorted list:

```text
# Pseudocode
# Warning: might be incomplete!
result = []
i = points to start of left
j = points to start of right

while i has not reached end of left and j has not reached end of right
    if left[i] < right[j]:
        add left[i] to result
        move i one position to the right
    else:
        add right[j] to result
        move j one position to the right
```

Elements are added one by one to `result`.
At each step, we need to determine which is the next element to add.
Since `result` itself must be sorted, we must find the next smallest element.
Since `left` and `right` are sorted, we know that we can find the smallest element at the start of each list.
We compare `left[0]` with `right[0]`.
Say `left[0]` is the smaller of the two values, we then copy that value to `result`.
We also need to remember that in the following iteration, we need to look at `left[1]` instead of `left[0]`.

Implement `merge_sorted` based on the explanation above.
Write a parametrized test `test_merge_sorted`.
The test should have two parameters: `left` and `right`.
You can use multiple `@parametrize` decorators:

```python
@pytest.mark.parametrize('left', [
    [],
    [1],
    # ...
])
@pytest.mark.parametrize('right', [
    [],
    [1],
    # ...
])
def test_merge_sorted(left, right):
    # ...
```

Pytest will then call `test_merge_sorted` with all possible combinations of values for `left` and `right`.

* You can hardcode values for `left` and `right`.
* Remember to only specify _sorted_ lists.
* Try to think of special cases:
  * The empty list.
  * A list with gaps in it (e.g. `[4, 10, 15]`.)
  * A list containing the same value more than once (e.g. `[2, 5, 5, 9]`).
* Specify at least 5 possible values for both `left` and `right`, so that it total there are at least 25 combinations in total.

Have the test check the result by asserting that `test_merge_sorted(left, right) == sorted(left + right)`.

> If you're wondering why not simply use `sorted(left + right)` as implementation for `test_merge_sorted`: you could, but it wouldn't work as fast.
  Here we are actually comparing results of a slow algorithm with that of a fast algorithm.
  This idea will be revisited in a later exercise.

### `merge_sort`

`merge_sort(ns)` receives a list and returns the same list, but with its elements sorted.
It does not modify `ns` in any way.

It works as follows:

* It splits `ns` in two, say `left` and `right`.
* It recursively sorts `left` and `right`.
  Let's call the results `sorted_left` and `sorted_right`.
* `sorted_left` and `sorted_right` are merged using `merge_sorted_lists`.

As always with recursion, you also need to know when to stop.
Ask yourself the question which cases are trivially solved.
Hint: what should happen if `merge_sort` receives the empty list?

Implement `merge_sort` as described above.
Write a parametrized test named `test_merge_sort`.
The test function should have two parameters:

* `expected`, a sorted list.
* `ns`, an unsorted permutation of `expected`, i.e., it contains the same elements but not necessarily in the same order.

Use `@parametrized` to feed it pairs of `expected` and `ns`:

* Start by manually picking an arbitrary sorted list.
  This will be used as value for `expected`.
* Use `itertools.permutations` to generate all permutations.
  These will be used as values for `ns`.

For example, you can pick `[1, 2, 3]` as `expected`.
Then, rely on `itertools.permutations` to generate `[1, 2, 3]`, `[1, 3, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[3, 1, 2]` and `[3, 2, 1]`.
`@parametrized` can then be used to have `test_merge_sort` called six times:

```python
test_merge_sort(expected=[1, 2, 3], ns=[1, 2, 3])
test_merge_sort(expected=[1, 2, 3], ns=[1, 3, 2])
test_merge_sort(expected=[1, 2, 3], ns=[2, 1, 3])
test_merge_sort(expected=[1, 2, 3], ns=[2, 3, 1])
test_merge_sort(expected=[1, 2, 3], ns=[3, 1, 2])
test_merge_sort(expected=[1, 2, 3], ns=[3, 2, 1])
```

Use multiple sorted starting lists: use the empty list, a list with the same element occurring more than once, etc.
For each of these lists, generate all permutations and feed them to `test_merge_sort`.
Make sure not to make these lists too long as otherwise the number of permutations will grow too large.
Six elements should be a good maximum length.

The test will be trivial to implement: it receives `expected` and `ns`, so it only needs to sort `ns` using `merge_sort` and compare the result to `expected`.

### Final Step

Run our tests to thoroughly check that your functions are implemented correctly.

```bash
$ pytest -x verify.py
```
