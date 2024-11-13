from .event import Event

# this class is a subclass of the Event class
# it initializes the time range for events from the start of today to the end of today
class DayEvent(Event):
    
    # constructor
    def __init__(self):
        # calls superclass constructor
        super().__init__()
        # get the time at the start of the day
        start_of_day = self.now.replace(hour=0, minute=0, second=0, microsecond=0)
        # get the time at the end of the day
        end_of_day = self.now.replace(hour=23, minute=59, second=59, microsecond=999999)
        # stores variables to be used when get_events function is called
        self.time_min = start_of_day.isoformat()
        self.time_max = end_of_day.isoformat()
        self.time_period = "day"
