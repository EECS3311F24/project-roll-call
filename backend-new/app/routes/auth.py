from flask import redirect, session, request, url_for, jsonify
from app.services.auth_service import initiate_google_auth, handle_oauth_callback, decode_google_id_token
from app.utils.common import credentials_to_dict, serialize_document
from app.services.user_service import create_user, get_user
import json
from app.db import get_db
from . import auth
from bson import ObjectId


"""
This route is used when a user first sign ups (user visits for the first time)
This route is connected with /signup_callback, which handles the OAuth callback from Google, 
fetches the user's profile information, creates and fetches their account in the database, 
and initializes their session with relevant user data.
"""
@auth.route("/signup")
def signup():
    return redirect(initiate_google_auth("auth.signup_callback"))
@auth.route("/signup_callback")
def signup_callback():
    try:
        redirect_uri = url_for("auth.signup_callback", _external=True)
        credentials = handle_oauth_callback(request.url, redirect_uri)

        user_info = decode_google_id_token(credentials["id_token"])
        user = create_user(user_info)

        # Store user data in the session (optional)
        session["user"] = {
            "id": str(user["google_id"]),  # MongoDB document ID
            "email": user["email"],
            "token": credentials["token"]
        }

        # TODO we want to redirect to the user dashboard to get their settings 
        return redirect("http://localhost:5000/auth/users_mongo")

    except Exception as e:
        return f"An error occurred during the OAuth process: {str(e)}", 400



"""
This route is used when a user logins (returns)
This route is connected with /login_callback, which handles the OAuth callback from Google, 
fetches the user's profile information, creates and fetches their account in the database, 
and initializes their session with relevant user data.
"""
@auth.route("/login")
def login():
    """
    Initiates the Google OAuth flow.
    """
    return redirect(initiate_google_auth("auth.login_callback"))
@auth.route("/login_callback")
def login_callback():
    try:
        redirect_uri = url_for("auth.login_callback", _external=True)
        credentials = handle_oauth_callback(request.url, redirect_uri)
        user_info = decode_google_id_token(credentials["id_token"])

        user = get_user(user_info["google_id"])

        # Store user data in the session (optional)
        session["user"] = {
            "id": str(user["_id"]),  # MongoDB document ID
            "email": user["email"],
            "token": credentials["token"]
        }

        # Redirect to a /today page
        # TODO we want to redirect to the user's today page
        return redirect("http://localhost:5000/auth/users_mongo")

    except Exception as e:
        return f"An error occurred during the OAuth process: {str(e)}", 400


@auth.route("/logout")
def logout():
    """
    Clears the session to log out the user.
    """
    session.clear()
    print(session)
    return "You have been logged out, check logs!"




### TESTING ROUTES ----------------------------------------------------------------
@auth.route("/test")
def test():
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

@auth.route("/users_mongo")
def users_mongo():
    """
    Test MongoDB connection and return all users in the 'users' collection.
    """
    db = get_db()
    users_collection = db["users"]

    users = users_collection.find()

    users_list = [serialize_document(user) for user in users]

    return jsonify(users_list)

