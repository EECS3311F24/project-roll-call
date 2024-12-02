import datetime as dt
from .event import Event
from datetime import datetime, timedelta
from ...models import User


# this class is a subclass of the Event class
# it initializes the time range for events from now to 30 days from now

class FutureEvent(Event):
    # constructor
    def __init__(self, creds):
        # calls superclass constructor
        super().__init__(creds)
        # set the end of the time range as today + 30 days
        future_weeks = self.user.settings["future_weeks"]
        end_of_month = self.now + dt.timedelta(days=7*future_weeks)
        self.time_min = self.now.isoformat()
        self.time_max = end_of_month.isoformat()
        self.time_period = "Future at a glance"
    

    def categorize_events(self, events):
        high_priority_colors = []
        med_priority_colors = []
        high_priority_events = []
        med_priority_events = []
    
        # Find High Priority Color IDs
        for key,value in self.user.settings.items():
            if isinstance(value, dict) and value.get("priority") == "High Priority":
                high_priority_colors.append(value.get("color"))

        # Find Med Priority Color IDs
        for key,value in self.user.settings.items():
            if isinstance(value, dict) and value.get("priority") == "Medium Priority":
                med_priority_colors.append(value.get("color"))     

        for i in high_priority_colors:
            high_priority_events += self.filter_events_by_color(events, str(i))

        for i in med_priority_colors:
            med_priority_events += self.filter_events_by_color(events, str(i))

        # print(high_priority_colors)
        # print(med_priority_colors)

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

            if (self.user.settings["organize_by"] == "category"): # check user setting
                event_type = self.get_event_type(event)
            else: 
                event_type = self.get_event_priority(event)
     
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
