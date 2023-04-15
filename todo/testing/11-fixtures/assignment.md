# Fixtures

We used `setup_function` to factor out common code.
However, it has some serious shortcomings.

> But why did we bother explaining `setup_function` instead of immediately offering the better solution?
> Well, other testing frameworks only provide the `setup_function` approach, and you might always encounter tests that still rely on `setup_function` in older code.

One weakness of the `setup_function` is that it can quickly become a place where all Arrange stages of the tests are combined.
Ideally, `setup_function` should only create objects needed by *all* tests, but this rule is too rigid to follow in practice:
Following the rule strictly would prevent you from writing tests that don't use *all* objects created by `setup_function`, which is silly.
So instead, the `setup_function` will grow and, in the worst case, end up being the union of all Arrange stages of the tests.

Having a large `setup_function` has two major disadvantages:

* The more a `setup_function` does, the more chance it has to fail.
  If a single line of code raises an exception, *none* of the tests will be able to run.
  This kind of chain reaction has to be avoided at all costs.
* It slows things down unnecessarily.

A better solution is to rely on Pytest's `@fixture` functionality:

```python
import pytest


@pytest.fixture
def today():
    return date(2000, 1, 1)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def calendar(today):
    return CalendarStub(today)


def test_calendar_stuff(calendar):
    # do stuff with calendar
```

Here's how it works:

* Pytest identifies `test_calendar_stuff` as a test.
* It looks at the test function's parameter list and finds `calendar`.
  This is the test's way of saying "I require a `calendar` do perform my job."
* It looks for `@fixture`s with the same name.
* It finds the function `calendar` that has been tagged as a fixture.
  Just like with the test function, it uses parameters to convey what its dependencies are.
  `calednar` needs the fixture named `today`.
* Pytest will then look for a `@fixture` named `today`.
* It finds it, sees there are no parameters (hence no dependencies) and simply calls the function.
  This returns a `date` object.
* This `date` object is then passed as argument to the function `calendar`.
  This function uses it to create a new `CalendarStub`.
* Thhis `CalendarStub` is then passed to `test_calendar_stuff`, which can use it to perform some checks.

In short, tests (and fixtures) can declare their dependencies using parameters.
Pytest will then automatically call the corresponding `@fixture` and pass its return value as arguments.
A test/fixture can have as many dependencies it wants.

`@fixture`s solve the shortcomings mentioned above: only those fixtures that are mentioned in the parameter list will be created.
This will cause the tests to run faster, but most importantly, no tests will fail due to errors occurring in unrelated code.

## Task

Update the `TaskList` tests so as to use `@fixture` instead of `setup_function`.
Create fixture functions for

* `today`
* `tomorrow`
* `yesterday`
* `calendar`
* `sut`

Declare the necessary dependencies using parameters.
This includes both "test depends on fixture" and "fixture depends on other fixture".
