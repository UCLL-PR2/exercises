# Dependency Injection

In the previous exercise, you implemented the classes `Task` and `TaskList`.
We now want to write some tests.
Let's focus on `TaskList`'s `overdue_date` functionality.
We expect the following behavior:

```python
from datetime import date, timedelta


def test_task_becomes_overdue():
    tomorrow = date.today + timedelta(days=1)
    task = Task('some description', tomorrow)
    tasks = TaskList()

    tasks.add_task(task)

    # Wait 2 days...

    assert [task] == tasks.overdue_tasks
```

Make sure you understand the code above:

* We first create a `Task` that's due tomorrow.
* At this time, the task is not considered to be overdue, as its `due_date` is still in the future.
* We wait two days (and don't do to complete the task).
* The `Task` becomes *overdue*: we're past its `due_date`.
  It should now appear in the `overdue_tasks` list.

The test shown above has a rather large flaw: it has to wait for two days in order for the `Task` to become overdue.
We really don't want to have to wait that long.
As mentioned earlier, tests should run *fast*.

We could of course choose to pick a better due date, one just one microsecond in the future.
There are two problems with this:

* We are working with the `date` class.
  This class does not know anything smaller than a day.
  We would have to use the `datetime` class which combines date and time of day.
* In other contexts, the time delay simply cannot be chosen.
  For example, a game's rules might state that building a certain unit takes a full minute.
  A test would then have to wait this full minute, which is still unacceptably long.

We could also actually change the date your computer is set on, quickly check `overdue_tasks` and then set the date back.
This would be a horrible idea though as all other software running on the machine might get very confused.
But allowing us to change date would be so very handy...

Your code for `TaskList` probably looks a bit like this:

```python
class TaskList:
    # ...

    @property
    def overdue_tasks(self):
        return [
            task for task in self.__tasks
            if not task.finished and task.due_date < date.today()
        ]
```

This code relies on `date.today()`.
This method directly returns the machine's date.
The only ways to influence what it returns is to actually wait, or to change your computer's date.
We can, however, introduce an _indirection_: what if we develop our _own_ `today()` method?

## `Calendar`

In `calendars.py`, write a new class `Calendar`.
It has a single property: `today`.
It returns today's date, i.e., `date.today()`.

Next, have `TaskList` receive a `Calendar` object at creation.
It stores this `Calendar` in a private field and relies on it wherever it needs today's date.

Example usage:

```python
>>> calendar = Calendar()
>>> calendar.today
# shows today's date
```

After these changes, everything should still work exactly as before.

## `CalendarStub`

Also in `calendars.py`, now write another class `CalendarStub`.

* To the outside world, it should work the same as `Calendar`, i.e., it should have a member named `today`.
* It gives the user complete control over the date returned by `today`.

Example usage:

```python
# The constructor allows picking our own date
>>> calendar = CalendarStub(date(2000, 1, 1))
>>> calendar.today
datetime.date(2000, 1, 1)

# We can change the date as we see fit
>>> calendar.today = date(2001, 1, 1)
>>> calendar.today
datetime.date(2001, 1, 1)
```

## Dependency Injection

Our original `TaskList` code directly used `date.today()` to determine the current date.
There was no way to "parametrize" this: the link between `TaskList` and `date.today()` was hardcoded.

[Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) is simply the idea that if a class depends on something, that this dependency shouldn't be hardcoded.
Instead, the dependency should be configurable, for example using constructor parameters.
We achieved this by introducing the calendar classes.

```python
>>> calendar = Calendar()
>>> task_list = TaskList(calendar)
```

This effectively states "`TaskList`, please use this `calendar` object to determine the current date".
Put differently, we were able to "inject" the dependency.
It makes code more modular, which increases reusability and testability.

We now have two calendars:

* `Calendar` will be used in production, that is, the code that ends up running on the end user's machine.
* `CalendarStub` will come in handy during testing as it allows us to easily set the date.

## Other Examples

There are many cases where dependency injection can be useful:

* Say you write a game involving dice and your code relies on [`random.randint()`](https://docs.python.org/3/library/random.html#random.randint) to generate random numbers between `1` and `6`.
  However, this makes testing arduous: you want to be able to simulate certain rolls, so the tests will start having to roll the dice until a certain outcome is reached.
  Instead, you can introduce `RandomDice` and `ControlledDice` classes where the former returns actual random values while the latter can be configured to return certain dice rolls.
* The built-in `print` and `input` should typically not be used directly as again you would be hardcoding the destination and source of your IO.
  What if the data should be received/sent on a network instead?
  Again, an intermediate object can help out here.
* When your application has external dependencies such as a database, being able to work with smaller fake in-memory databases can simplify testing a lot.

## Testing

In a separate file `tests.py`, write the test `test_task_becomes_overdue` that performs the same checks as the code shown at the top of this file.
Run the test and make sure it passes.
