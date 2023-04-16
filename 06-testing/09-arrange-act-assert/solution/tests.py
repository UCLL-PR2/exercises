import pytest
from datetime import date, timedelta
from calendars import CalendarStub
from tasks import Task, TaskList


def test_creation():
    # Arrange
    today = date(2000, 1, 1)
    calendar = CalendarStub(today)

    # Act
    sut = TaskList(calendar)

    # Assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_future():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = TaskList(calendar)

    # Act
    sut.add_task(task)

    # Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks


def test_adding_task_with_due_day_in_past():
    # Arrange
    today = date(2000, 1, 1)
    yesterday = today - timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task('description', yesterday)
    sut = TaskList(calendar)

    # Act/Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)


def test_task_becomes_overdue():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(weeks=1)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks


def test_task_becomes_finished():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    # Act
    task.finished = True

    # Assert
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
