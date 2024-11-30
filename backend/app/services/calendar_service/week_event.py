import datetime as dt
from .event import Event
from datetime import datetime, timedelta

# this class is a subclass of the Event class
# it initializes the time range for events from the start of tomorrow to the end of the 6th day from today
class WeekEvent(Event):
    
    # constructor
    def __init__(self, creds):
        # calls superclass constructor
        super().__init__(creds)
        # get the time at start of tomorrow
        start_of_tomorrow = (self.now + dt.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        # get the time at the end of 6 days from now
        end_of_week = (self.now + dt.timedelta(days=6)).replace(hour=23, minute=59, second=59, microsecond=999999)
        # stores variables to be used when get_events function is called
        self.time_min = start_of_tomorrow.isoformat()
        self.time_max = end_of_week.isoformat()
        self.time_period = "week"

    def categorize_events(self, events):
        week_start = datetime.fromisoformat(self.time_min)
        events_by_day = {i: [] for i in range(7)}
        
        for event in events:
            event_start = event["start"].get("dateTime") or event["start"].get("date")

            if "dateTime" in event["start"]:
                event_start = datetime.fromisoformat(event_start)
            else:
                event_start = datetime.fromisoformat(event_start + "T00:00:00").astimezone(self.timezone)
            
            days_diff = (event_start - week_start).days

            if 0 <= days_diff < 7:
                events_by_day[days_diff].append({
                    "id": event["id"],
                    "summary": event["summary"],
                    "start": event["start"],
                    "end": event["end"],
                })

        categorized = []
        
        for day_index in range(7):
            events_for_day = events_by_day.get(day_index, [])

            if events_for_day:
                day_label = (week_start + timedelta(days=day_index)).strftime("%A, %b %d")
                categorized.append({"day": day_label, "events": events_for_day})
        
        return categorized
