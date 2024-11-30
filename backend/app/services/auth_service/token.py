from google.oauth2 import id_token
from google.auth.transport import requests as google_request
import json
from flask import session
from google.auth.transport.requests import Request
from google.oauth2.id_token import verify_oauth2_token
from app.services.user_service import create_user, get_user, user_in_db, store_creds
from google.oauth2.credentials import Credentials


def credentials_to_dict(credentials):
    """
    Converts credentials object to a dictionary for easy handling.
    """
    return {
        "token": credentials.token,
        "id_token": credentials.id_token,
        "refresh_token": credentials.refresh_token or "Not enabled",
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes,
    }

def decode_google_id_token(id_token):
    """
    Decodes the Google ID token and extracts user information.
    Returns a dictionary with email, given_name, family_name, and picture and ID
    """
    try:
        # Verify the token and extract the payload
        payload = verify_oauth2_token(id_token, Request(), clock_skew_in_seconds=5)

        # Extract user information
        user_info = {
            "google_id" :payload.get("sub"),
            "email": payload.get("email"),
            "f_name": payload.get("given_name"),
            "l_name": payload.get("family_name"),
            "pfp": payload.get("picture"),
        }

        return user_info

    except ValueError as e:
        raise Exception(f"Invalid ID token: {str(e)}")

def check_granted_scopes(credentials):
    """
    Checks which scopes were granted by the user.
    """
    features = {
        "drive": "https://www.googleapis.com/auth/drive.metadata.readonly" in credentials["scopes"],
        "calendar": "https://www.googleapis.com/auth/calendar.readonly" in credentials["scopes"],
        "profile": "https://www.googleapis.com/auth/userinfo.profile" in credentials["scopes"],
        "email": "https://www.googleapis.com/auth/userinfo.email" in credentials["scopes"],
        "send-email": "https://www.googleapis.com/auth/gmail.send" in credentials["scopes"],
    }
    return features 

def get_user_id(session):
    """
    Extracts the user ID from the session dictionary.

    :param session: A dictionary containing session data.
    :return: The user ID as a string, or None if the ID is not present or the session is empty.
    """
    if not session or not isinstance(session, dict):  # Check if session is empty or not a dictionary
        print("Session is empty or invalid.")
        return None
    
    try:
        return session.get("user", {}).get("id")
    except AttributeError:
        # Handle cases where session structure is not as expected
        print("Invalid session format.")
        return None


def get_creds_by_id(google_id, required_scope):
    """
    This function returns the required token to make Google API calls. 
    The token is retrieved from the database using the user_id stored in the session.
    Before returning the token, a series of checks are done to make sure it is valid:
        - Checks if session valid
        - Checks token against required scopes for the API call
        - Checks if expired 
            - Attempts to refresh if expired
    """  
    user_scope = get_user_scopes(google_id)
    # Check if all required scopes are in user_scope
    if not set(required_scope).issubset(set(user_scope)):
        raise Exception("User is missing required permission for API call.")
    
    # fetch access and refresh token -> convert it to google cred object
    token = get_access_token(google_id)
    refresh_token, refresh_uri = get_refresh_token(google_id)
    cred = Credentials(
        token=token,
        refresh_token=refresh_token,
        token_uri=refresh_uri
    )
    # Attempt to refresh the token 
    if cred.expired:
        if cred.refresh_token == "Not enabled":
            raise Exception("Token expired and offline use not enabled. REAUTHENTICATE!")
        else:
            try:
                cred.refresh(Request())
                user = get_user(google_id)
                # Update the database with the refreshed token
                user.creds.token = cred.token
                user.save()
            except Exception as e:
                raise Exception(f"Failed to refresh the access token: {e}")

    return cred

def get_creds(session, required_scope):
    """
    This function returns the required token to make Google API calls. 
    The token is retrieved from the database using the user_id stored in the session.
    Before returning the token, a series of checks are done to make sure it is valid:
        - Checks if session valid
        - Checks token against required scopes for the API call
        - Checks if expired 
            - Attempts to refresh if expired
    """
    id = get_user_id(session)
    if not id:
        raise Exception("User is not authenticated. Missing user ID in session.")
    
    user_scope = get_user_scopes(id)
    
    # Check if all required scopes are in user_scope
    if not set(required_scope).issubset(set(user_scope)):
        raise Exception("User is missing required permission for API call.")
    
    # fetch access and refresh token -> convert it to google cred object
    token = get_access_token(id)
    refresh_token, refresh_uri = get_refresh_token(id)
    cred = Credentials(
        token=token,
        refresh_token=refresh_token,
        token_uri=refresh_uri
    )

    # Attempt to refresh the token 
    if cred.expired:
        if cred.refresh_token == "Not enabled":
            raise Exception("Token expired and offline use not enabled. REAUTHENTICATE!")
        else:
            try:
                cred.refresh(Request())
                user = get_user(id)
                # Update the database with the refreshed token
                user.creds.token = cred.token
                user.save()
            except Exception as e:
                raise Exception(f"Failed to refresh the access token: {e}")

    return cred

    
def get_access_token(google_id):
    user = get_user(google_id)
    return user.creds.token

def get_refresh_token(google_id):
    user = get_user(google_id)
    return user.creds.refresh_token, user.creds.token_uri

def get_user_scopes(google_id):
    user = get_user(google_id)
    return user.creds.scopes

# def print_session():
#     session_data = dict(session)
#     print(session_data)

def print_session(session):
    session_data = dict(session)
    print(session_data)


def save_session():
    session_data = dict(session)
    with open('session_data.json', 'w') as json_file:
        json.dump(session_data, json_file, indent=4)
