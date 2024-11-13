import datetime as dt
import os.path
import pytz
import calendar
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# if modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# def get_month():
#     # get the time at start of tomorrow
#     now = get_time_now()
#     start_of_tomorrow = (now + dt.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
#     start_of_tomorrow_iso = start_of_tomorrow.isoformat()

#     # get the time at the end of 6 days from now
#     end_of_week = (now + dt.timedelta(days=6)).replace(hour=23, minute=59, second=59, microsecond=999999)
#     end_of_week_iso = end_of_week.isoformat()

#     return get_events(start_of_tomorrow_iso, end_of_week_iso, "week")

# def get_week():
#     # get the time at start of tomorrow
#     now = get_time_now()
#     start_of_tomorrow = (now + dt.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
#     start_of_tomorrow_iso = start_of_tomorrow.isoformat()

#     # get the time at the end of 6 days from now
#     end_of_week = (now + dt.timedelta(days=6)).replace(hour=23, minute=59, second=59, microsecond=999999)
#     end_of_week_iso = end_of_week.isoformat()

#     return get_events(start_of_tomorrow_iso, end_of_week_iso, "week")

# def get_day():
#     now = get_time_now()

#     # get the time at the start of the day
#     start_of_day_iso = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()

#     # get the time at the end of the day
#     end_of_day_iso = now.replace(hour=23, minute=59, second=59, microsecond=999999).isoformat()

#     return get_events(start_of_day_iso, end_of_day_iso, "day")

def get_credentials():
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

def get_events(time_min, time_max, time_period):
    creds = get_credentials()

    try:
        service = build("calendar", "v3", credentials=creds)
        print (f"Getting the upcoming events for the {time_period}...")
        
        events_result = service.events().list(
            calendarId="primary",
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True,
            orderBy="startTime"
        ).execute()

        events = events_result.get("items", [])

        if not events:
            print(f"No events found for the {time_period}.")
        
        return events
    
    except HttpError as error:
        print(f"An error occurred: {error}")
        
        return None

def get_time_now():
    timezone = pytz.timezone("America/New_York")
    now = dt.datetime.now(timezone)
    
    return now