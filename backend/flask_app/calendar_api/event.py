import datetime as dt
import os.path
import pytz
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# if modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

class Event:
    def __init__(self):
        self.creds = self.get_credentials()
        self.now = self.get_time_now()
        self.time_min = None
        self.time_max = None
        self.time_period = None

    def get_credentials(self):
        creds = None
        
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        
        return creds

    def get_events(self):
        try:
            service = build("calendar", "v3", credentials=self.creds)
            print (f"Getting the upcoming events for the {self.time_period}...")
            
            events_result = service.events().list(
                calendarId="primary",
                timeMin=self.time_min,
                timeMax=self.time_max,
                singleEvents=True,
                orderBy="startTime"
            ).execute()

            events = events_result.get("items", [])

            if not events:
                print(f"No events found for the {self.time_period}.")
            
            return events
        
        except HttpError as error:
            print(f"An error occurred: {error}")
            
            return None
    
    def get_time_now(self):
        timezone = pytz.timezone("America/New_York")
        now = dt.datetime.now(timezone)
        
        return now
