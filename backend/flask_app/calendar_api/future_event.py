import datetime as dt
from .event import Event


# this class is a subclass of the Event class
# it initializes the time range for events from now to 30 days from now
class FutureEvent(Event):
    
    # constructor
    def __init__(self):
        # calls superclass constructor
        super().__init__()
        # set the end of the time range as today + 30 days
        end_of_month = self.now + dt.timedelta(days=30)

        self.time_min = self.now.isoformat()
        self.time_max = end_of_month.isoformat()
        self.time_period = "Future at a glance"


    def get_events(self):
        print("FutureEvent get_events called...")
        # Fetch all events from the parent class method
        all_events = super().get_events()

        high_priority_events = self.filter_events_by_color(all_events, "11") + self.filter_events_by_color(all_events, "6")
        
        med_priority_events = self.filter_events_by_color(all_events, "1") + self.filter_events_by_color(all_events, "3")
        if (len(med_priority_events) > 5):
            med_priority_events = med_priority_events[:5]
        
        filtered_events = high_priority_events + med_priority_events
        filtered_events = self.sort_events_by_date(filtered_events)
        # self.print_events(filtered_events)

        return filtered_events


# Helper functions

def filter_events_by_title(events, title):
    """Filters events by the given title."""
    return [event for event in events if event.get("summary", "").strip() == title]
