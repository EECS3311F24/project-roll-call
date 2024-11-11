import datetime as dt
import calendar
from .event import Event
from datetime import datetime


# this class is a subclass of the Event class
# it initializes the time range for events from the start of this month to the end of this month
class FutureEvent(Event):
    
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
        self.time_period = "Future at a glance"


    def get_events(self):
        print("FutureEvent get_events called...")
        # Fetch all events from the parent class method
        all_events = super().get_events()

        high_priority_events = self.filter_events_by_color(all_events, "11") + super().filter_events_by_color(all_events, "6")
        high_priority_events = self.sort_events_by_date(high_priority_events)
        
        med_priority_events = self.filter_events_by_color(all_events, "1") + super().filter_events_by_color(all_events, "3")
        med_priority_events = self.sort_events_by_date(med_priority_events)
        if (len(med_priority_events) > 5):
            med_priority_events = med_priority_events[:5]
        
        filtered_events = high_priority_events + med_priority_events

        print_events(filtered_events)

        return filtered_events


# Helper functions

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
