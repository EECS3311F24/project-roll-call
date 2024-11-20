import datetime as dt
import os.path
import pytz
import google_auth_oauthlib.flow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from account_api.creds_manager import CredentialsManager

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

class Event:
    def __init__(self, credentials_file="credentials.json", scopes=SCOPES):
        self.creds = CredentialsManager.load_creds(credentials_file, default_scopes=scopes)
        if not self.creds:
            print("No valid credentials loaded.")  # Debug no credentials
            raise Exception("No valid credentials found. Please authenticate.")
        if not self.creds.valid:
            print("Credentials are not valid. Checking refresh status...")  # Debug invalid credentials
            if self.creds.expired and self.creds.refresh_token:
                print("Credentials expired. Refreshing...")
                self.creds.refresh(Request())
            else:
                print("No valid or refreshable token. Re-authentication required.")
                raise Exception("No valid credentials found. Please authenticate.")
        self.timezone = pytz.timezone("America/New_York")
        self.now = dt.datetime.now(self.timezone)
        self.time_min = None
        self.time_max = None
        self.time_period = None
        self.scopes = scopes

    # this function gets the events from Google Calendar
    def get_events(self):
        try:
            # builds service for Google Calendar API
            service = build("calendar", "v3", credentials=self.creds)
            # print to console to test functionality
            # print (f"Getting the upcoming events for the {self.time_period}...")
            # gets the events from Google Calendar API
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
            return "Deadlines & Assessments"
        if color_id == "6":
            return "Appointments"
        if color_id == "1":
            return "Social Events"
        if color_id == "3":
            return "Unique Events"
        if color_id == "10":
            return "Works"
        if color_id == "9":
            return "Workouts"
        
        return "not found"

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