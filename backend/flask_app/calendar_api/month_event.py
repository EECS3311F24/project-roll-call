import datetime as dt
import calendar
from .event import Event

# this class is a subclass of the Event class
# it initializes the time range for events from the start of this month to the end of this month
class MonthEvent(Event):
    
    # constructor
    def __init__(self):
        # calls superclass constructor
        super().__init__()
        # get the time at the beginning of the current month
        start_of_month = self.now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        # get the time at the end of the current month
        days_in_month = calendar.monthrange(self.now.year, self.now.month)[1]
        end_of_month = (start_of_month + dt.timedelta(days=days_in_month - 1)).replace(hour=23, minute=59, second=59, microsecond=999999)
        # stores variables to be used when get_events function is called
        self.time_min = start_of_month.isoformat()
        self.time_min = end_of_month.isoformat()
        self.time_period = "month"
