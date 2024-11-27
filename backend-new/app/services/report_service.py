import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request


import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from flask import session
from app.models import User


def gmail_send_message():
  """Create and send an email message
  Print the returned  message id
  Returns: Message object, including message id

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """

  try:
    """
    Retrieves the Google Calendar API service using credentials from the session.
    """
    # Extract user_google_id from the session
    user_google_id = session.get("user", {}).get("id")
    if not user_google_id:
        raise Exception("User is not authenticated. Missing user ID in session.")

    # Fetch the user from the database
    user = User.objects(google_id=user_google_id).first()
    if not user or not user.creds:
        raise Exception("User is not authenticated or credentials are missing.")
    
    # Construct the Credentials object using the stored credentials
    creds = Credentials(
        token=user.creds.token,
        refresh_token=user.creds.refresh_token,
        token_uri=user.creds.token_uri,
        client_id=user.creds.client_id,
        client_secret=user.creds.client_secret,
        scopes=user.creds.scopes,
    )

    # Check if the token is expired and refresh it if needed
    if creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            # Update the database with the refreshed token
            user.creds.token = creds.token
            user.save()
        except Exception as e:
            raise Exception(f"Failed to refresh the access token: {e}")

    service = build("gmail", "v1", credentials=creds)
    message = EmailMessage()

    message.set_content("This is automated draft mail")

    message["To"] = "saras.rollcall@gmail.com"
    message["From"] = "saras.rollcall@gmail.com"
    message["Subject"] = "Automated draft"

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    # pylint: disable=E1101
    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
    print(f'Message Id: {send_message["id"]}')
  except HttpError as error:
    print(f"An error occurred: {error}")
    send_message = None
  return send_message
