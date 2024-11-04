import datetime as dt
from .event import Event

# this class is a subclass of the Event class
# it initializes the time range for events from the start of tomorrow to the end of the 6th day from today
class WeekEvent(Event):
    
    # constructor
    def __init__(self):
        # calls superclass constructor
        super().__init__()
        # get the time at start of tomorrow
        start_of_tomorrow = (self.now + dt.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        # get the time at the end of 6 days from now
        end_of_week = (self.now + dt.timedelta(days=6)).replace(hour=23, minute=59, second=59, microsecond=999999)
        # stores variables to be used when get_events function is called
        self.time_min = start_of_tomorrow.isoformat()
        self.time_max = end_of_week.isoformat()
        self.time_period = "week"
