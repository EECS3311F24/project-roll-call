import requests
import google_auth_oauthlib.flow
from flask import url_for, session
from app.config import Config
from app.services.auth_service.token import credentials_to_dict, credentials_to_dict, check_granted_scopes


def initiate_google_auth(callback_route):
    """
    Initiates the Google OAuth flow by generating the authorization URL.
    """
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        Config.CLIENT_SECRETS_FILE,
        scopes=Config.SCOPES
    )
    flow.redirect_uri = url_for(callback_route, _external=True)

    authorization_url, state = flow.authorization_url(
        # access_type="offline",  ## we only have 100 per user
        include_granted_scopes="true",
        # prompt="consent"      ## try turning this on if you have issues
    )
    session["state"] = state  # Store state for verification in the callback
    return authorization_url


def handle_oauth_callback(authorization_response, redirect_uri):
    """
    Exchanges the authorization code for credentials.
    """
    if "state" not in session:
        raise Exception("OAuth state is missing or invalid.")
    state = session["state"]

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        Config.CLIENT_SECRETS_FILE,
        scopes=Config.SCOPES,
        state=state
    )
    flow.redirect_uri = redirect_uri
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials

    credentials_dict = credentials_to_dict(credentials)  # to be used to access google calendar api
    features = check_granted_scopes(credentials_dict)
    session['features'] = features

    # Return the dictionary instead of the object
    return credentials_dict






