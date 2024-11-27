import requests
import google_auth_oauthlib.flow
from flask import url_for, session
from app.config import Config
from app.utils.common import credentials_to_dict, check_granted_scopes
from google.auth.transport.requests import Request
from google.oauth2.id_token import verify_oauth2_token


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
        access_type="offline",  ## we only have 100 per user
        include_granted_scopes="true",
        # prompt="consent"
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


    # Convert credentials to a dictionary for session storage
    credentials_dict = credentials_to_dict(credentials)
    session['credentials'] = credentials_dict

    # Check which scopes user granted
    features = check_granted_scopes(credentials_dict)
    session['features'] = features

    # Return the dictionary instead of the object
    return credentials_dict


def decode_google_id_token(id_token):
    """
    Decodes the Google ID token and extracts user information.
    Returns a dictionary with email, given_name, family_name, and picture and ID
    """
    try:
        # Verify the token and extract the payload
        payload = verify_oauth2_token(id_token, Request())

        # Extract user information
        user_info = {
            "google_id" :payload.get("sub"),
            "email": payload.get("email"),
            "f_name": payload.get("given_name"),
            "l_name": payload.get("family_name"),
            "pfp": payload.get("picture"),
        }

        # print(user_info)
        return user_info

    except ValueError as e:
        raise Exception(f"Invalid ID token: {str(e)}")



# def fetch_google_profile(access_token):
#     """
#     Fetches the user's Google profile using the access token.
#     """
#     response = requests.get(
#         "https://www.googleapis.com/oauth2/v2/userinfo",
#         headers={"Authorization": f"Bearer {access_token}"}
#     )

#     if response.status_code != 200:
#         raise Exception("Failed to fetch user profile.")
#     # print(response.json())
#     return response.json()


