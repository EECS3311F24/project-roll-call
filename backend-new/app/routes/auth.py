from flask import redirect, session, request, url_for
from app.services.auth_service import initiate_google_auth, handle_oauth_callback
from app.utils.common import credentials_to_dict

import json
from . import auth



@auth.route("/login")
def login():
    """
    Initiates the Google OAuth flow.
    """
    return redirect(initiate_google_auth())

@auth.route("/callback")
def callback():
    """
    Handles the OAuth callback and stores credentials.
    """
    try:
        credentials_dict = handle_oauth_callback(request.url)
        session["credentials"] = credentials_dict

        # Save credentials for debugging (optional)
        with open("credentials.json", "w") as cred_file:
            json.dump(credentials_dict, cred_file)

        return redirect(url_for("auth.test_redirect"))  # Redirect to a test page or frontend

    except Exception as e:
        return f"An error occurred during the OAuth process: {str(e)}", 400
    

@auth.route("/logout")
def logout():
    """
    Clears the session to log out the user.
    """
    session.clear()
    return "You have been logged out."


@auth.route("/test")
def test():
    print("Importing routes in app/routes/auth.py")
    return "Auth Blueprint is working!"

@auth.route("/test_redirect")
def test_redirect():
    """
    Temporary test route to display session data after login.
    """
    from flask import jsonify

    # Check if credentials are in session
    credentials = session.get("credentials")
    if not credentials:
        return "No credentials found in session. Please log in again.", 401

    # Display session data
    return jsonify({
        "message": "OAuth flow successful!",
        "user_features": session.get("features"),
        "user_credentials": credentials
    })

