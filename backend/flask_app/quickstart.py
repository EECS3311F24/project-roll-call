import datetime as dt
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pytz

# if modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def get_month():
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

    try:
        service = build("calendar", "v3", credentials=creds)

        print("Getting the upcoming events for the month...")

        # Set the start time to the beginning of the current month
        timezone = pytz.timezone("America/New_York")
        now = dt.datetime.now(timezone)
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        start_of_month_iso = start_of_month.isoformat()
        
        # Set the end time to the end of the month
        next_month = start_of_month + dt.timedelta(days=31)
        end_of_month = next_month.replace(day=1, hour=0, minute=0, second=0, microsecond=0) - dt.timedelta(seconds=1)
        end_of_month_iso = end_of_month.isoformat()

        events_result = service.events().list(
            calendarId="primary",
            timeMin=start_of_month_iso,
            timeMax=end_of_month_iso,
            singleEvents=True,
            orderBy="startTime"
        ).execute()
        
        events = events_result.get("items", [])

        if not events:
            print("No events found for the month.")
        
        return events
    
    except HttpError as error:
        print(f"An error occurred: {error}")

def get_week():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        print("Getting the upcoming events for the week...")
        
        # set now to the time right now, and time_max to the time 7 days from now
        # now = dt.datetime.now(dt.UTC)
        now = dt.datetime.now(dt.timezone.utc)
        now_iso = now.isoformat()
        time_max = (now + dt.timedelta(days=7)).isoformat()

        events_result = (
            service.events().list(
                calendarId="primary",
                timeMin=now_iso,
                timeMax=time_max,
                singleEvents=True,
                orderBy="startTime",
            ).execute()
        )

        events = events_result.get("items", [])

        if not events:
            print("No weekly events...")

        return events
    
    except HttpError as error:
        print(f"An error occurred: {error}")

def get_day():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        # set now to the time right now, and end_of_day to the time at the end of today
        timezone = pytz.timezone("America/New_York")
        now = dt.datetime.now(timezone)
        now_iso = now.isoformat()
        end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999).isoformat()

        print("Getting today's events")
        
        events_result = service.events().list(
            calendarId="primary",
            timeMin=now_iso,
            timeMax=end_of_day,
            singleEvents=True,
            orderBy="startTime"
        ).execute()
        
        events = events_result.get("items", [])

        if not events:
            print("No events found for today.")

        return events
    
    except HttpError as error:
        print(f"An error occurred: {error}")