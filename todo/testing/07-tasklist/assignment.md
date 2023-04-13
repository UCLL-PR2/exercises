# Tasklist

In this exercise, we'll have you write two classes that will be used as working example for the next few exercises.

We do not provide any way to validate your work, as you'll be writing your own tests later on.

## `Task`

In a file `tasks.py`, write a class `Task`.

* It has a readonly property `description` that is initialized using a constructor parameter.
* It has a readonly property `due_date` that is initialized using a constructor parameter.
* It has a settable field `finished` which is initially set to `False`.

To represent dates, we use the standard `date` class from the [`datetime` module](https://docs.python.org/3/library/datetime.html).

Example usage:

```python
>>> from datetime import date
>>> task = Task('bake birthday cake', date(2023, 10, 1))
>>> task.description
'bake birthday cake'

>>> task.due_date
datetime.date(2023, 10, 1)

>>> task.finished
False

>>> task.finished = True
>>> task.finished
True
```

## `TaskList`

A `TaskList` keeps track of a list of `Task`s.
It offers the following functionality:

* `TaskList()` creates an empty task list.
* `task_list.add_task(task)` adds a `Task` to the list.
  The `Task`'s `due_date` must be in the future.
  In case its `due_date` is in the past, a `RuntimeErrror` should be thrown.
* `len(task_list)` gives the number of tasks in the list.
* `task_list.finished_tasks` returns a list of all finished tasks, i.e., those tasks whose `task.finished` is `True`.
* `task_list.due_tasks` returns a list of all unfinished tasks, i.e., those tasks whose `task.finished` is `False`.
* `task_list.overdue_tasks` returns a list of all unfinished tasks whose `task.due_date` is in the past.

In order to implement the `overdue_tasks` property, you'll need the following `date` functionality:

* You can use `<` to compare dates. If `date1 < date2` evaluates to `True`, this means that `date1` takes place before `date2`.
* Getting today's date (i.e., the date at the time the code is executed) is done using `date.today()`.

Example usage:

```python
>>> from datetime import date, timedelta
>>> tasks = TaskList()
>>> len(tasks)
0

>>> tomorrow = date.today + timedelta(days=1)
>>> yesterday = date.today - timedelta(days=1)

# Adding task with due_date in past is forbidden
>>> task_in_past = Task('some description', yesterday)
>>> tasks.add_task(task_in_past)
RuntimeError

# Adding task with due_date in future works
>>> task = Task('some description', tomorrow)
>>> tasks.add_task(task)
>>> len(tasks)
1

>>> tasks.finished_tasks
[]

>>> tasks.due_tasks
[task]                 # not exactly what's shown, but we simplified for the sake of clarity

>>> tasks.overdue_tasks
[]

# Wait 2 days...

>>> tasks.finished_tasks
[]

>>> tasks.due_tasks
[task]

>>> tasks.overdue_tasks
[task]

>>> task.finished = True
>>> tasks.finished_tasks
[task]

>>> tasks.due_tasks
[]

>>> tasks.overdue_tasks
[]
```

Implement this class in the same file `tasks.py`.
