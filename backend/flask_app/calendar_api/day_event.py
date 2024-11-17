from .event import Event
from datetime import datetime

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

    def categorize_events(self, events):        
        categorized = {
            "allDay": [],
            "morning": [],
            "afternoon": [],
            "evening": []
        }

        for event in events:
            start_time = event["start"].get("dateTime")
            end_time = event["end"].get("dateTime")
            start_date = event["start"].get("date")
            end_date = event["end"].get("date")
            
            if start_time and end_time:
                start = datetime.fromisoformat(start_time)
                end = datetime.fromisoformat(end_time)
            elif start_date and end_date:
                start = datetime.fromisoformat(start_date + "T00:00:00").astimezone(self.timezone)
                end = datetime.fromisoformat(end_date + "T23:59:59").astimezone(self.timezone)

            if end < self.now:
                event_status = "past"
            elif start <= self.now <= end:
                event_status = "ongoing"
            else:
                event_status = "upcoming"

            hour = start.hour

            event_data = {
                "id": event["id"], 
                "summary": event["summary"],
                "start": event["start"],
                "end": event["end"],
                "status": event_status
            }

            if start_date and end_date:
                categorized["allDay"].append(event_data)
            else:
                if hour < 12:
                    categorized["morning"].append(event_data)
                elif 12 <= hour < 18:
                    categorized["afternoon"].append(event_data)
                else:
                    categorized["evening"].append(event_data)
        
        return categorized
