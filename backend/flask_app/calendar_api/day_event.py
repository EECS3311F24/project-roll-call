from .event import Event

class DayEvent(Event):
    def __init__(self):
        super().__init__()

        # get the time at the start of the day
        start_of_day = self.now.replace(hour=0, minute=0, second=0, microsecond=0)

        # get the time at the end of the day
        end_of_day = self.now.replace(hour=23, minute=59, second=59, microsecond=999999)

        self.time_min = start_of_day.isoformat()
        self.time_max = end_of_day.isoformat()
        self.time_period = "day"
