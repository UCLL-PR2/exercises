from datetime import date, timedelta


class Calendar:
    @property
    def today(self):
        return date.today()


class ManualCalendar:
    def __init__(self, today):
        self.today = today
