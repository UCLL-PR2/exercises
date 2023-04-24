# Testing

When writing code, correctness should always be your primary concern.
Your code can be efficient, modular and elegant, but if it doesn't produce the right results, it's of little use to anyone.

Since correctness is so important, there are many tools that aid you in achieving it:

* Static typing
* Verification tools
* Assertions
* Correctness proofs
* Writing tests

Each of these approaches has its own strengths and weaknesses.
Combining them is often possible ([Swiss cheese model](https://en.wikipedia.org/wiki/Swiss_cheese_model)), allowing us to combine strengths and avoid weaknesses.
In this series of exercises we will focus on writing tests and assertions, as these methods are prevalent in the industry (together with static typing, but that's for another time.)

## Good Tests

How does one write _good_ tests?
What can make a test good anyway?
What would be the difference with a bad test?

There are many different opinions of how to write tests.
Many different approaches exist, and each approach has their zealots that claim that their approach is the best.

We won't advocate a specific approach here.
Instead, we will ask ourselves the question, what makes a good test?
What qualities should it have?
Once we know how that, we will be able to judge whether tests are well written and how to improve them if needed.

### Automation

Some people, when writing code, like to perform quick manual tests:

```python
def some_function(x):
    # ...

print(some_function(5))
print(some_function(77))
```

They run the code and see if the right values are being outputted.
If so, the `print`s are removed and their attention turns to the next function/class/...

This is a _horrible_ approach to testing.
Don't do it.

If you're going to write testing code, you might as well not remove it, because that actually requires extra effort.
Simply group your testing code in a separate file, and keep it there, ready to be run.

People who remove tests assume that

* their tests are exhaustive and that they've just shown their code is 100% bug free, so no need to ever test it again; and
* their code will never need to be modified in any way (e.g., an optimization, an extra optional parameter, etc.)

Those assumptions are more often than not wrong.
So keep your tests.

Another major weakness of the example above is that it requires manual checking: `some_function`'s return values are printed out but need to be checked each time.
Instead, include the expected value in the tests:

```python
assert some_function(5) == 100
assert some_function(77) == 678
```

This way, it becomes the machine's job to perform the checking.

In short, you want to be able to simply run the tests and get a 100% pass rate.
Testing should require no more work from you than that.

### Fine Grained Tests

An airplane is a complex piece of machinery.
In the cockpit, there's plenty of little screens and lights giving the pilots feedback on the airplane's current status.
When something goes wrong, it is crucial that pilots are made aware of the problem as quickly as possible: typically something will light up, probably also make some buzzing sound to attract attention.
Not only that, the pilot also needs to know _where_ the issue is located: are they low on kerosene?
Has the front fallen off?
Is there a gremlin on the wings?
By knowing what exactly is wrong, the pilot can take immediate action to rectify the situation, like... flying to the nearest kerosene station.
(The writer is not a trained pilot, he's doing the best he can, okay?)

Similarly, a piece of code often often has many ways to go wrong.
Running the tests should give us a clear overview of what went wrong, but also of what went right.
The more precise this overview, the easier it will be to identify the culprit.

A test should ideally only be able to fail for only one reason.
If a single test can fail for ten different reasons, then there's ten different things to investigate if that test fails.
Our goal will be to keep the "reasons for failure" of every test as low as possible, so that if a test fails, we know exactly where to look for the responsible code.

### Readable Tests

When a test fails, you'll want to be able what exactly was being tested:

* If objects are involved, what state were they in?
* What action was performed?
* What was the expected result and what was the actual result?

### Fast Running Tests

In practice, tests are run quite often:

* As will be explained in the section about regression testing, tests are run after every little code change.
* Tests can also be run live, i.e., continuously in the background as you write code.
* The development process is also often set up (using [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) or [GitHub actions](https://github.com/features/actions)) to automatically run tests before allowing you to commit your changes to the master/main branch.

Depending on the project, there can also be _many_ tests to run.
In other words, you want the tests to run fast.

### Isolated Tests

Tests should always be run in isolation.
By this we mean that tests should not be able to affect each other's results.
The order in which the tests are run should not matter, and tests should be able to be run in parallel without affecting the outcome.


## Pytest

Pytest is the testing framework we rely on in this course.
We briefly explain what it does, exactly.

As you know, running `pytest` will cause the tests defined in `tests.py` to be run.
We [configured](https://docs.pytest.org/en/7.1.x/reference/reference.html#confval-python_files) it that way: if you look at `pytest.ini` in your repository's root directory, you'll find

```text
python_files =
    tests.py
    *_tests.py
```

which tells Pytest which files to search for tests.

Inside these files, Pytest collects all functions that start with `test`.
This is the [default setting](https://docs.pytest.org/en/7.1.x/reference/reference.html#confval-python_functions).

Each test function is run.
A test function that returns normally (i.e., no exception) is considered to have passed.
Therefore, in order to tell Pytest a test failed, you need to throw an exception.

While you can throw an assertion manually, we strongly suggest to rely on `assert`:

```python
def test_something():
    assert condition
```

If `condition` evaluates to a falsey value, an `AssertionError` will be thrown.

If you rely on `assert`, Pytest will be able to recognize the checks and rewrite your code slightly to allow for better feedback.
For example, compare these two tests:

```python
def test_1():
    actual = [1, 2, 3]
    expected = [1, 2, 4]
    assert expected == actual


def test_2():
    actual = [1, 2, 3]
    expected = [1, 2, 4]
    if actual != expected:
        raise AssertionError()
```

Running the tests produces the following feedback:

```bash
$ pytest
FF                                                   [100%]
===================== FAILURES ============================
______________________ test_1 _____________________________

    def test_1():
        actual = [1, 2, 3]
        expected = [1, 2, 4]
>       assert expected == actual
E       assert [1, 2, 4] == [1, 2, 3]
E         At index 2 diff: 4 != 3
E         Use -v to get more diff

tests.py:4: AssertionError
______________________ test_2 _____________________________
    def test_2():
        actual = [1, 2, 3]
        expected = [1, 2, 4]
        if actual != expected:
>           raise AssertionError()
E           AssertionError

tests.py:11: AssertionError
============== short test summary info =====================
FAILED tests.py::test_1 - assert [1, 2, 4] == [1, 2, 3]
FAILED tests.py::test_2 - AssertionError
2 failed in 0.09s
```

As you can see, `test_1` provides useful information: it shows you the values of `actual` and `expected`.
Pytest even points out how exactly they differ: in our case, the elements with index 2 are unequal.

We'll discuss more of its capabilities as we progress.

## Task

Say we need to write a function `overlapping_intervals(interval1, interval2)` that checks whether the given intervals overlap.
We represent intervals using pairs.
The interval represented by the tuple `(left, right)` contains all values `x` for which `left <= x <= right`.
For example, the intervals `(2, 5)` and `(3, 8)` do overlap: they have `2` and `3` in common.
Conversely, `(0, 4)` and `(6, 9)` do not overlap.
Note that `(0, 4)` and `(4, 0)` do not overlap: the second interval is empty since there exist no `x` for which `4 <= x <= 0`.

Let's implement this function.
Create a file `ìntervals.py` and copy the code below into that file:

```python
def overlapping_intervals(interval1, interval2):
    # Unpack bounds
    left1, right1 = interval1
    left2, right2 = interval2

    # Check if one of interval2's bounds fall inside interval1
    return left1 <= left2 <= right1 or left1 <= right2 <= right1
```

This is a nontrivial function, so we better test it.
Create a file `tests.py` and copy this test into that file:

```python
from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
```

Run the tests using `pytest` as usual.
They should pass.

However, `overlapping_intervals`'s implementation is actually faulty: the tests are incomplete.
Your task is

* Add more `assert`s to the test.
  Try to think of as many cases as you can.
  Make sure to check cases where the expected result is `True` and cases where the expected result is `False`.
* Try to understand what's wrong with `overlapping_intervals`'s implementation.
* Fix `overlapping_intervals`.
* Run your own tests again and make sure they pass.
  If not, go back to fixing `overlapping_intervals`.
* Run our tests by using `pytest -x verify.py`.
  If these don't all pass, go back to step 1.

> You should always commit all files you were tasked to update.
> In the past, this was limited to `student.py`, but now you should add `intervals.py` and `tests.py`.
