from google.oauth2 import id_token
from google.auth.transport import requests as google_request
import json 
from flask import session


def credentials_to_dict(credentials):
    """
    Converts credentials object to a dictionary for easy handling.
    """
    return {
        "token": credentials.token,
        "id_token": credentials.id_token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes,
    }
 

def check_granted_scopes(credentials):
    """
    Checks which scopes were granted by the user.
    """
    features = {
        "drive": "https://www.googleapis.com/auth/drive.metadata.readonly" in credentials["scopes"],
        "calendar": "https://www.googleapis.com/auth/calendar.readonly" in credentials["scopes"],
        "profile": "https://www.googleapis.com/auth/userinfo.profile" in credentials["scopes"],
    }
    return features  

def serialize_document(doc):
    """
    Converts MongoDB document ObjectId fields to strings.
    """
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

def save_session():
    session_data = dict(session)
    with open('session_data.json', 'w') as json_file:
        json.dump(session_data, json_file, indent=4)
