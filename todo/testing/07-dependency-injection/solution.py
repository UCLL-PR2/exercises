from datetime import date, timedelta


class Calendar:
    @property
    def today(self):
        return date.today()


class ManualCalendar:
    def __init__(self, today):
        self.today = today


class Task:
    def __init__(self, description, due_date):
        self.__description = description
        self.finished = False
        self.__due_date = due_date

    @property
    def description(self):
        return self.__description

    @property
    def due_date(self):
        return self.__due_date


class TaskList:
    def __init__(self, calendar):
        self.__calendar = calendar
        self.__tasks = []

    def __len__(self):
        return len(self.__tasks)

    def add_task(self, task):
        if task.due_date < self.__calendar.today:
            raise RuntimeError()
        self.__tasks.append(task)

    @property
    def finished_tasks(self):
        return [task for task in self.__tasks if task.finished]

    @property
    def due_tasks(self):
        return [task for task in self.__tasks if not task.finished]

    @property
    def overdue_tasks(self):
        return [task for task in self.__tasks if not task.finished and task.due_date < self.__calendar.today]


def test_overdue_tasks():
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = ManualCalendar(today)
    task = Task('description', tomorrow)
    task_list = TaskList(calendar)

    task_list.add_task(task)
    calendar.today = next_week

    assert [task] == task_list.overdue_tasks
