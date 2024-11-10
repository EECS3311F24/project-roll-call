import datetime as dt
import calendar
from .event import Event
from datetime import datetime


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

        high_priority_events = filter_events_by_color(all_events, "11") + filter_events_by_color(all_events, "6")
        high_priority_events = sort_events_by_date(high_priority_events)
        
        med_priority_events = filter_events_by_color(all_events, "1") + filter_events_by_color(all_events, "3")
        med_priority_events = sort_events_by_date(med_priority_events)
        if (len(med_priority_events) > 5):
            med_priority_events = med_priority_events[:5]
        
        filtered_events = high_priority_events + med_priority_events

        print_events(filtered_events)

        return filtered_events


# Helper functions
def sort_events_by_date(events):
    events = sorted(
        events,
        key=lambda event: event.get("start").get("dateTime") or event.get("start").get("date"))
    return events


def filter_events_by_color(events, colorId):
    """Filters events by the given color.
    11 = Tomato (Red)               Deadlines/tests     High
    4  = Flamingo (Pink)            
    6  = Tangerine (Orange)         Appointments        High
    5  = Banana (Yellow)
    2  = Sage (Light Green)
    10 = Basil (Dark Green)         Work                Low
    9  = Blueberry (Dark blue)      Workouts            Low
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
    
def filter_events_by_title(events, title):
    """Filters events by the given title."""
    return [event for event in events if event.get("summary", "").strip() == title]

# Printing testing function
def print_events(events):
    print("-------------------------------------------------------------")
    for event in events:
        name = event.get("summary", "No Title")
        start = event.get("start", {})
        date_time = start.get("dateTime")
        
        if date_time:
            date, time = date_time.split('T', 1)
        else:
            date = start.get("date", "Unknown Date")
            time = ""

        print(f"{name.ljust(30)}: {date} - {time}")
        print("-------------------------------------------------------------")
