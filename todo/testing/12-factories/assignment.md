# Factory Functions

Consider the following tests:

```python
@pytest.fixture
def task(tomorrow):
    return Task('xxx', tomorrow)

# more code

def test_task_creation(task, tomorrow):
    assert task.description == 'xxx'
    assert task.due_date == tomorrow
    assert task.finished == False
```

While `test_task_creation` passes and is quite to the point, it suffers from a lack of readability.
The problem is that the initial values for each member (`xxx`, `tomorrow` and `False`) have been chosen somewhere outside the test.
If the test fails, we'd have to look around our code to find out what the values actually should be.
In other words, the test isn't self contained.

## Descriptive Variable Names

We can alleviate this problem a bit by using a more descriptive variable name:

```python
@pytest.fixture
def unfinished_task_due_by_tomorrow(tomorrow):
    return Task('xxx', tomorrow)

# more code

def test_task_creation(unfinished_task_due_by_tomorrow, tomorrow):
    assert unfinished_task_due_by_tomorrow.due_date == tomorrow
    assert unfinished_task_due_by_tomorrow.finished == False
```

The test feels a lot less arbitrary now.
It's not just some "task", it's an *unfinished task due by tomorrow*!
Sadly, the description is still missing.
Should we change the name to `unfinished_task_due_by_tomorrow_described_as_xxx`?
It's obvious that this approach can become very impractical very quickly.

## Mutable Fixtures

Another issue arises when we start modifying our fixtures.

```python
@pytest.fixture
def unfinished_task(tomorrow):
    return Task('xxx', tomorrow)


def test_task_becomes_finished(sut, unfinished_task):
    # Arrange
    sut.add_task(unfinished_task)

    # Act
    unfinished_task.finished = True

    # Assert
    assert [] == sut.due_tasks
    assert [unfinished_task] == sut.finished_tasks
```

The test receives an unfinished task, but then sets it to finished.
We end up with a variable `unfinished_task` that contains a finished `Task`.
The second `assert` does not make sense: it states that the list of finished tasks contains an unfinished task.
Such misleading names ought to be avoided at all costs.

On the one hand, the variable's name should convey all important information.
The test doesn't care about the task's description or its due date, but in order for the test to make sense it is crucial that the task be unfinished.
So, the rule above tells us that we should use the name `unfinished_task`.

On the other hand, a basic variable naming rule says to pick a name that, at all times, describes the value accurately.
We know we have a task, so the name should at least include the word `task`.
However, during its lifetime the task goes from unfinished to finished, meaning the name must remain vague enough and can't mention anything about its "finishedness".

Quite a dilemma we've got on our hands.

## Factory Functions

Factory functions are functions whose sole purpose is to create an object.
Here is how we can use them:

```python
def create_unfinished_task():
    return Task('xxx', date(2000, 1, 1))


def test_task_becomes_finished(sut):
    # Arrange
    task = create_unfinished_task()
    sut.add_task(unfinished_task)

    # Act
    task.finished = True

    # Assert
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
```

This approach has the same advantages as `@fixture`: no unneeded objects are created.
It also solves the problem we described above:

* The factory function has an accurate and precise name:
  * It makes clear that the returned task is unfinished.
  * It doesn't convey any extra information that would be irrelevant to the test.
* The variable name at no point contradicts the variable's value.

## Flexible Factory Function

Different tests might need different kinds of tasks.
While it is possible to create distinct factory functions (`create_finished_task`, `create_unfinished_task`, `create_task_due_tomorrow`, etc.), a single parametrized factory function might be preferable:

```python
def create_task(*, description='default description', due_date=None, finished=False):
    due_date = due_date or date(2000, 1, 1)
    task = Task(description, due_date)
    if finished:
        task.finished = True
    return task


def test_task_becomes_finished(sut):
    # Arrange
    task = create_task(finished=True)
    sut.add_task(unfinished_task)

    # Act
    task.finished = True

    # Assert
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
```

This factory function allows you to only mention the relevant properties for the `Task` to be created.
It automatically fills in with defaults for the other members.

> The `*` in `create_task`'s parameter list forces callers to use keyword arguments, i.e., `create_task('description')` is invalid, but `create_task(description='description')` is okay.

## Summary

We've discussed three ways of factoring out shared dependencies:

* `setup_function`
* `@fixture`
* Factory functions

`setup_function` is generally discouraged as it provides [no advantages](https://docs.pytest.org/en/7.3.x/explanation/fixtures.html#improvements-over-xunit-style-setup-teardown-functions) compared to the latter two approaches.
Whether to use `@fixture` or factory functions can be a matter of opinion.
Try to keep in mind what makes a good test and decide based on that.

We'd like to add that [pytest's fixtures](https://docs.pytest.org/en/7.3.x/explanation/fixtures.html#about-fixtures) have some extra functionality we didn't discuss:

* We can [parametrize](https://docs.pytest.org/en/7.3.x/how-to/fixtures.html#parametrizing-fixtures) fixtures so that they yield multiple values.
  A test requesting this fixture will be run multiple times, once for each of these values.
* Fixtures that provide resources that need to be cleaned up (e.g., database connections need closing, temporary files need to be deleted, ...) can easily specify [teardown](https://docs.pytest.org/en/7.3.x/how-to/fixtures.html#yield-fixtures-recommended) logic.
* [Smart caching](https://docs.pytest.org/en/7.3.x/how-to/fixtures.html#fixtures-can-be-requested-more-than-once-per-test-return-values-are-cached)
* [Scoping](https://docs.pytest.org/en/7.3.x/how-to/fixtures.html#scope-sharing-fixtures-across-classes-modules-packages-or-session) to reuse fixtures across classes/modules/packages.

## Task

Replace the fixtures by factory functions.
Also make use of `create_task` for tests that need a `Task`.