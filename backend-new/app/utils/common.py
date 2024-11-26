def credentials_to_dict(credentials):
    """
    Converts credentials object to a dictionary for easy handling.
    """
    return {
        "token": credentials.token,
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