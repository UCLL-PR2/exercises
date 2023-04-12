# Parametrized Tests

In the previous exercise, we instructed you to write tests for a function `overlapping_intervals` as a series of `assert`s in a test function:

```python
def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    # ...
```

We previously mentioned how a test should ideally only be able to fail for one single reason.
Here however, we bundled multiple `assert`s in one test, each of which can be a reason for failure.

Imagine we have ten such `assert`s in a single test.
If the first `assert` were to fail, it would throw an exception, causing the test to  be interrupted and the remaining `assert`s to get skipped.
This throws away potentially valuable information: it might be interesting to whether the other checks pass or fail.

We can easily remedy this by putting each `assert` in its own test:

```python
def test_overlapping_intervals1():
    assert overlapping_intervals((1, 5), (3, 6))

def test_overlapping_intervals2():
    assert not overlapping_intervals((2, 5), (7, 10))

# ...
```

## Improving Reporting

`pytest` generates a summary after having run all tests.
It gives you a nice overview of which tests have failed.
Let's run the tests with a faulty implementation of `overlapping_intervals`:

```python
[left out detailed reports]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals1 - assert False
FAILED tests.py::test_overlapping_intervals2 - assert not True
```

As you can see, the summary is not very useful.
Some people might suggest we give the tests better names:

```python
def test_overlapping_intervals_1_5_overlaps_with_3_6():
    assert overlapping_intervals((1, 5), (3, 6))

def test_overlapping_intervals_2_5_does_not_overlap_with_7_10():
    assert not overlapping_intervals((2, 5), (7, 10))

# ...
```

This way, when running the tests, you get a better overview of what failed:

```bash
$ pytest
[left out detailed reports]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals_1_5_overlaps_with_3_6 - assert False
FAILED tests.py::test_overlapping_intervals_2_5_does_not_overlap_with_7_10 - assert not True
```

There are some downsides to this approach though:

* Python (like most other languages) imposes many restrictions on how we can name our functions.
  For example, a test named `test that interval (1, 5) overlaps with interval (3, 6)` would be more readable, but it's disallowed due to it containing spaces, parentheses and commas.
* We add redundancy: both the test and the test's name contain the same information about the intervals' bounds.
* It prevents us from parameterizing our tests (see later.)

A better approach would be to equip the `assert` with an error message:

```python
def test_overlapping_intervals1():
    assert overlapping_intervals((1, 5), (3, 6)), "Interval (1, 5) overlaps with interval (3, 6)"

def test_overlapping_intervals2():
    assert not overlapping_intervals((2, 5), (7, 10)), "Interval (2, 5) does not overlap with interval (7, 10)"
```

Running the tests then gives

```bash
$ pytest
[left out detailed reports]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals1 - AssertionError: Interval (1, 5) overlaps with interval (3, 6)
FAILED tests.py::test_overlapping_intervals2 - AssertionError: Interval (2, 5) does not overlap with interval (7, 10)
```

This has not rid us from redundancy though.
Fortunately, this is easily fixed:

```python
def test_overlapping_intervals1():
    interval1 = (1, 5)
    interval2 = (3, 6)
    assert overlapping_intervals(interval1, interval2), f"Interval {interval1} overlaps with interval {interval2}"

def test_overlapping_intervals2():
    interval1 = (2, 5)
    interval2 = (7, 10)
    assert not overlapping_intervals(interval1, interval2), f"Interval {interval1} does not overlap with interval {interval2}"
```

## `@Parametrize`

Writing tests certainly seem to involve a lot of copy pasting: the tests shown above are near identical.
We would like to make the tests more compact.
Ideally, we would like to only have to write down what's essential to every test case and not have any kind of boilerplate code.

Pytest allows us to _parametrize_ tests.
Let's do this step by step.

First, notice the two local variables `interval1` and `interval2` we introduced to avoid redundancy.
Let's turn these into parameters:

```python
def test_overlapping_intervals1(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"Interval {interval1} overlaps with interval {interval2}"
```

Okay, the test has halved in size, but how does the test know what values to use for `interval1` and `interval2`?
We can reintroduce these as follows:

```python
import pytest


@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (3, 6)),
])
def test_overlapping_intervals1(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"Interval {interval1} overlaps with interval {interval2}"
```

The `parametrize` decorator takes two parameters:

* The first is a string with the parameter names.
  These _must_ be the same as the test function's parameters.
  It will become clear later why this is necessary.
* The second is a list of tuples of values to be assigned to the parameters.
  In the example, we tell Pytest to assign `(1, 5)` to `interval1` and `(3, 6)` to `interval2`.

We are not restricted to only one tuple of values:

```python
import pytest


@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (3, 6)),
    ((1, 5), (5, 6)),
    ((1, 10), (3, 6)),
    ((6, 8), (3, 6)),
    ((5, 7), (4, 8)),
])
def test_overlapping_intervals1(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"Interval {interval1} overlaps with interval {interval2}"
```

This generates five tests for you.
Running `pytest` produces

```bash
$ pytest
[left out detailed reports]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals1[interval10-interval20] - AssertionError: Interval (1, 5) overlaps with interval (3, 6)
FAILED tests.py::test_overlapping_intervals1[interval11-interval21] - AssertionError: Interval (1, 5) overlaps with interval (5, 6)
FAILED tests.py::test_overlapping_intervals1[interval12-interval22] - AssertionError: Interval (1, 10) overlaps with interval (3, 6)
FAILED tests.py::test_overlapping_intervals1[interval13-interval23] - AssertionError: Interval (6, 8) overlaps with interval (3, 6)
FAILED tests.py::test_overlapping_intervals1[interval14-interval24] - AssertionError: Interval (5, 7) overlaps with interval (4, 8)
```

Let's have two parametrized tests: one for overlapping intervals, one for nonoverlapping intervals:

```python
import pytest


@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (3, 6)),
    ((1, 5), (5, 6)),
    ((1, 10), (3, 6)),
    ((6, 8), (3, 6)),
    ((5, 7), (4, 8)),
])
def test_overlapping_intervals(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"Interval {interval1} overlaps with interval {interval2}"


@pytest.mark.parametrize('interval1, interval2', [
    ((1, 2), (3, 4)),
    ((1, 5), (5, 1)),
    ((8, 9), (6, 7)),
    ((8, 9), (6, 7)),
])
def test_nonoverlapping_intervals(interval1, interval2):
    assert not overlapping_intervals(interval1, interval2), f"Interval {interval1} does not overlap with interval {interval2}"
```

## Task

Copy the contents of `starter.py` to `parentheses.py`.
The function `matching_parentheses(string)` receives a string containing only parentheses (`'('` and `')'`).
It checks that all parentheses are matched, i.e., that every `(` has a matching `)`.

* Write two parametrized test functions in `tests.py`: one for cases where `True` should be returned, and one for `False`.
  Rely on `@parametrize` to specify inputs.
* Run your tests.
  They should fail as `matching_parentheses` contains bugs.
* Fix `matching_parentheses` in `parentheses.py`.
* Run your tests (`$ pytest`).
* Run our tests (`$ pytest verify.py`).
  If those fail, go back to step 1.
