import datetime as dt
import calendar
from .event import Event

class MonthEvent(Event):
    
    def __init__(self):
        super().__init__()
        
        now = self.get_time_now()

        # get the time at the beginning of the current month
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        
        # get the time at the end of the current month
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        end_of_month = (start_of_month + dt.timedelta(days=days_in_month - 1)).replace(hour=23, minute=59, second=59, microsecond=999999)

        self.time_min = start_of_month.isoformat()
        self.time_min = end_of_month.isoformat()
        self.time_period = "month"
