import datetime as dt
from .event import Event

class WeekEvent(Event):
    def __init__(self):
        super().__init__()

        now = self.get_time_now()

        # get the time at start of tomorrow
        start_of_tomorrow = (now + dt.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)

        # get the time at the end of 6 days from now
        end_of_week = (now + dt.timedelta(days=6)).replace(hour=23, minute=59, second=59, microsecond=999999)

        self.time_min = start_of_tomorrow.isoformat()
        self.time_max = end_of_week.isoformat()
        self.time_period = "week"
