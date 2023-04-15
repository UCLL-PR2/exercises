# Arrange Act Assert

Let's add some structure to our tests.
By following a convention, we will improve the readability and overall quality of our tests.

Let us take a look at a possible implementation for `test_task_becomes_overdue` from the previous exercise:

```python
def test_task_becomes_overdue():
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    task_list = TaskList(calendar)
    task_list.add_task(task)
    calendar.today = next_week
    assert [task] == task_list.overdue_tasks
```

We can distinguish three stages:

* **Arrange** The first stage gathers all necessary objects that will be necessary for the test.
* **Act** The second stage performs the operation whose consequences need to be checked.
* **Assert** The third stage checks that the operation has had the desired effects.

We can make these three stages more explicit:

```python
def test_task_becomes_overdue():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    task_list = TaskList(calendar)
    task_list.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == task_list.overdue_tasks
```

It can also be useful to clearly identify which object it is we're testing.
In our case, `task_list` is at the center of attention: it is this object that we're testing the behavior of.
To make this explicit, we can adopt the convention of using the name `sut` which stands for *system under test*:

```python
def test_task_becomes_overdue():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks
```

Note that these conventions are just that: conventions.
They don't magically make your tests perfect, and it's not always possible or beneficial to follow them to the letter.

Remember that updating your code can make the tests unexpectedly fail.
You will need to inspect the failing tests to understand what exactly goes wrong, after which you can pinpoint the location in the code that contains a bug and fix it.
Adopting a consistent structure make tests easier to understand.

> In case you are wondering why we set `today` to `date(2000, 1, 1)` instead of `date.today()`: tests must be 100% deterministic and always check the same things every time they're run.
> Using `date.today()` would have the tests run on different values each day.
> If you want the tests to run for different values of `today`, you should use parametrized tests.

## Tasks

Add the following tests:

* `test_creation` creates a new `TaskList` and checks the initial values of `len(task_list)`, `due_tasks`, `overdue_tasks` and `finished_tasks`.
* `test_adding_task_with_due_day_in_future` adds a `Task` whose `due_date` is set in the future.
* `test_adding_task_with_due_day_in_past` adds a `Task` whose `due_date` is in the past.
  It should expect a `RuntimeError` to be thrown.
* `test_task_becomes_finished` adds a `Task`, then sets its `finished` member to `True`.
  The `Task` should have moved from `task_list.due_tasks` to `task_list.finished_tasks`.
