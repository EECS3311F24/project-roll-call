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
        # set the start time is the start of the current day
        start_of_month = self.now.replace(hour=0, minute=0, second=0, microsecond=0)
        # set the end of the month as today + 30 days
        end_of_month = start_of_month + dt.timedelta(days=30)


        self.time_min = start_of_month.isoformat()
        self.time_max = end_of_month.isoformat()
        self.time_period = "month"

        print(f"MonthEvent initialized with time_min={self.time_min}, time_max={self.time_max}")


    def get_events(self):
        print("MonthEvent get_events called...")
        # Fetch all events from the parent class method
        all_events = super().get_events()
        
        filtered_events = filter_events_by_title(all_events, "TEST")
        # filtered_events = filter_events_by_color(all_events, "11")

        
        # Return the filtered list
        return filtered_events


# Helper functions
def filter_events_by_title(events, title):
    """Filters events by the given title."""
    return [event for event in events if event.get("summary", "").strip() == title]


def filter_events_by_color(events, colorId):
    """Filters events by the given color.
    11 = Tomato (Red)               Deadlines/tests     High
    4  = Flamingo (Pink)            Workouts            Low
    6  = Tangerine (Orange)         Appointments        High
    5  = Banana (Yellow)
    2  = Sage (Light Green)
    10 = Basil (Dark Green)         Work                Low
    9  = Blueberry (Dark blue)
    1  = Lavender (Light purple)    Social Events       Medium
    3  = Grape (Dark purple)        Unique Events       Medium
    8  = Graphite (Grey)
    -  = Peacock (Blue)             Classes/Meetings    Low
    """
    #  peacock is Google's default color therefore there is no colorId field
    if colorId == "-":  
        return [event for event in events if "colorId" not in event]
    else:
        return [event for event in events if event.get("colorId") == colorId]