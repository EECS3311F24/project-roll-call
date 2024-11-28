import datetime as dt
from .event import Event
from datetime import datetime


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


    def categorize_events(self, events):
        high_priority_events = self.filter_events_by_color(events, "11") + self.filter_events_by_color(events, "6")
        med_priority_events = self.filter_events_by_color(events, "1") + self.filter_events_by_color(events, "3")

        if (len(med_priority_events) > 5):
            med_priority_events = med_priority_events[:5]
        
        filtered_events = high_priority_events + med_priority_events

        categorized = {}

        for event in filtered_events:
            event_start = event["start"].get("dateTime") or event["start"].get("date")
            if "dateTime" in event["start"]:
                event_start = datetime.fromisoformat(event_start)
                day_label = event_start.strftime('%b %d')
            else:
                event_start = datetime.fromisoformat(event_start + "T00:00:00").astimezone(self.timezone)
                day_label = event_start.strftime('%b %d')

            event_type = self.get_event_type(event)
            
            if event_type not in categorized:
                categorized[event_type] = []

            categorized[event_type].append({
                "id": event["id"],
                "summary": event["summary"],
                "day": day_label
            })

        categorized_events = []
        for event_type, events in categorized.items():
            categorized_events.append({
                "type": event_type,
                "events": events
            })

        return categorized_events

# Helper functions

def filter_events_by_title(events, title):
    """Filters events by the given title."""
    return [event for event in events if event.get("summary", "").strip() == title]
