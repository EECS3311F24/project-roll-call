import datetime as dt
import pytz
from flask import session
from googleapiclient.discovery import build
from ...models import User

from app.services.auth_service.token import get_user_id
from flask import session


class Event:
    def __init__(self, creds):   
        self.creds = creds 
        self.timezone = pytz.timezone("America/New_York")
        self.now = dt.datetime.now(self.timezone)
        self.time_min = None
        self.time_max = None
        self.time_period = None

        self.google_id = get_user_id(session)
        self.user = User.objects.get(google_id=self.google_id)
        
    
    # this function gets the events from Google Calendar
    def get_events(self):
        try:
            # builds service for Google Calendar API
            service = build("calendar", "v3", credentials=self.creds)
            events_result = service.events().list(
                calendarId="primary",
                timeMin=self.time_min,
                timeMax=self.time_max,
                singleEvents=True,
                orderBy="startTime"
            ).execute()
            # stores the events in events
            events = events_result.get("items", [])
            # prints to the console to test functionality (no events found in the Calendar)
            if not events:
                print(f"No events found for the {self.time_period}.")
            return events
        # handles exception
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None
    
    # this function gets the event type based on colorId
    def get_event_type(self, event):

        color_id = event.get("colorId", "")

        if color_id == "11":
            return self.user.settings["e1"]["category"]
        if color_id == "4":
            return self.user.settings["e2"]["category"]
        if color_id == "6":
            return self.user.settings["e3"]["category"]
        if color_id == "5":
            return self.user.settings["e4"]["category"]
        if color_id == "2":
            return self.user.settings["e5"]["category"]
        if color_id == "10":
            return self.user.settings["e6"]["category"]
        if color_id == "9":
            return self.user.settings["e7"]["category"]
        if color_id == "1":
            return self.user.settings["e8"]["category"]
        if color_id == "3":
            return self.user.settings["e9"]["category"]
        if color_id == "8":
            return self.user.settings["e10"]["category"]
        if color_id == "-":
            return self.user.settings["e11"]["category"]
        
        return "category not found"
    
    # this function gets the event type based on colorId
    def get_event_priority(self, event):

        color_id = event.get("colorId", "")

        if color_id == "11":
            return self.user.settings["e1"]["priority"]
        if color_id == "4":
            return self.user.settings["e2"]["priority"]
        if color_id == "6":
            return self.user.settings["e3"]["priority"]
        if color_id == "5":
            return self.user.settings["e4"]["priority"]
        if color_id == "2":
            return self.user.settings["e5"]["priority"]
        if color_id == "10":
            return self.user.settings["e6"]["priority"]
        if color_id == "9":
            return self.user.settings["e7"]["priority"]
        if color_id == "1":
            return self.user.settings["e8"]["priority"]
        if color_id == "3":
            return self.user.settings["e9"]["priority"]
        if color_id == "8":
            return self.user.settings["e10"]["priority"]
        if color_id == "-":
            return self.user.settings["e11"]["priority"]
        
        return "category not found"


    # this function gets the events of a certain color
    def filter_events_by_color(self, events, colorId):
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
        
    # this function sorts a list of events by their start date/time in ascending order    
    def sort_events_by_date(self, events):
        events = sorted(
            events,
            key=lambda event: event.get("start").get("dateTime") or event.get("start").get("date")
        )
        return events

    # this function prints received events to console, for debugging
    def print_events(self, events):
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
