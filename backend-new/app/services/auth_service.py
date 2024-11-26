import google_auth_oauthlib.flow
from flask import url_for, session
from app.config import Config
from app.utils.common import credentials_to_dict

def initiate_google_auth():
    """
    Initiates the Google OAuth flow by generating the authorization URL.
    """
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        Config.CLIENT_SECRETS_FILE,
        scopes=Config.SCOPES
    )
    flow.redirect_uri = url_for("auth.callback", _external=True)

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true"
    )
    session["state"] = state  # Store state for verification in the callback
    return authorization_url


def handle_oauth_callback(authorization_response):
    """
    Exchanges the authorization code for credentials and retrieves user info.
    """
    state = session["state"]
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        Config.CLIENT_SECRETS_FILE,
        scopes=Config.SCOPES,
        state=state
    )

    flow.redirect_uri = url_for("auth.callback", _external=True)

    # Exchange the authorization code for tokens
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials

    return credentials_to_dict(credentials)

