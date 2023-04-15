# Setup

Take a look at the `tests.py` in the solutions folder of the *previous* exercise.
The Arrange sections have much in common:

* A `today` date is created.
* A new `CalendarStub` initialized on `today`.
* A `TaskList` is made in most.

We would like to factor out this common code.
One way to achieve this is to rely on the `setup_function` function.

When launced, Pytest will scan your `tests.py` for test functions (as configured in `pytest.ini`).
To determine whether a function is a test function, Pytest looks at the name: all functions whose name start with `test_` are identified as tests.
Pytest will then call each of these test functions in *some* order.

Now, Pytest also looks for a function named `setup_function`.
Before running a test, Pytest will call `setup_function`.
Similarly, you can also have a function named `teardown_function`.
This will be called *after* each test.

For example, say we have the following definitions in `tests.py`:

```python
def setup_function():
    # ...

def teardown_function():
    # ...

def test_1():
    # ...

def test_2():
    # ...

def test_3():
    # ...
```

Pytest will then call these functions in the following order:

* ``setup_function()``
* `test_1()`
* `teardown_function()`
* ``setup_function()``
* `test_2()`
* `teardown_function()`
* ``setup_function()``
* `test_3()`
* `teardown_function()`

The `setup_function` function can be used to gather all code common in all tests.
If you're wondering why `setup_function` is called before *each* test instead of just once: we want each test to start with fresh objects.
Nothing prevents a test from modifying these objects, meaning that a change made in `test_1` could affect the outcome of `test_2`.
This is something that must be avoided at all costs: remember the Test Isolation goal we set out for ourselves.

Conversely, `teardown_function` can be useful to perform clean up: delete files that were created by the tests, close database connections, etc.

## Implementing `setup_function`

As an example, we show how you can rely on `setup_function` to create the `today` date.

```python
def setup_function():
    global today
    today = date(2000, 1, 1)


def test_whatever():
    calendar = CalendarStub(today)
    # ...
```

Notice the `global` declaration in `setup_function`.
Without `global`, `today` would simply be a local variable and therefore not visible to `test_whatever`.

## Task

Clean up your own tests (or our own solution's tests if that's easier) by relying on `setup_function`.
Inside this `setup_function` function, create `today`, `tomorrow`, `yesterday`, `calendar` and `sut`.
Adapt your tests so as to make use of these shared variables.

Run the tests to make sure everything still works.
