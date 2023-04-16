from datetime import date
from calendars import CalendarStub
from tasks import Task, TaskList


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
