import datetime as dt
import os.path
import pytz
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# if modifying these scopes, delete the file token.json
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# this class gets the credentials for Google Calendar and gets the events from Google Calendar
class Event:

    # constructor
    def __init__(self):
        # calls get_credentials and stores it in creds
        self.creds = self.get_credentials()
        # calls get_time_now and stores it in now
        self.now = self.get_time_now()
        # defines but does not initialize values of time range and time period (done by subclasses)
        self.time_min = None
        self.time_max = None
        self.time_period = None

    # this function gets the credentials for Google Calendar
    def get_credentials(self):
        creds = None
        # uses token.json if it exists which is created on the first log in to Google
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # otherwise gets and saves token
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        return creds

    # this function gets the events from Google Calendar
    def get_events(self):
        try:
            # builds service for Google Calendar API
            service = build("calendar", "v3", credentials=self.creds)
            # print to console to test functionality
            print (f"Getting the upcoming events for the {self.time_period}...")
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
    
    # this function gets the time right now for EST time zone
    def get_time_now(self):
        timezone = pytz.timezone("America/New_York")
        now = dt.datetime.now(timezone)
        return now

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
            key=lambda event: event.get("start").get("dateTime") or event.get("start").get("date"))
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