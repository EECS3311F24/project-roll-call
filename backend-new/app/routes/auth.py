from flask import redirect, session, request, url_for, jsonify
from app.services.auth_service import initiate_google_auth, handle_oauth_callback, decode_google_id_token
from app.utils.common import credentials_to_dict, serialize_document
from app.services.user_service import create_user, get_user, user_in_db
import json
from app.db import get_db
from . import auth
from bson import ObjectId


"""
This route is used both signup and login (first and revisiting user). 
This route is connected with /callback which fetches the user's profile information
from the id_token generated from google's Oauth2. The google id is extracted from the token 
and checked against the cloud mongo db.
If this id already exists in the db then the user is directed to the /today page 
If this id is not in the db, then a new user is created using the info from their google account 
(accessed from the token_id). They are then directed to the dashboard so they can set up their account.  
"""
@auth.route("/login")
def login():
    return redirect(initiate_google_auth("auth.callback"))
@auth.route("/callback")
def callback():
    try:
        redirect_uri = url_for("auth.callback", _external=True)
        credentials = handle_oauth_callback(request.url, redirect_uri)

        user_info = decode_google_id_token(credentials["id_token"])

        # user already exists !
        if (user_in_db(user_info["google_id"])):
            user = get_user(user_info["google_id"])

            # Store user data in the session (optional)
            session["user"] = {
                "id": str(user["_id"]),  # MongoDB document ID
                "email": user["email"],
                "token": credentials["token"]
            }
            # redirect to main page
            return redirect("http://localhost:3000/test")
        
        # new user !
        else:
            user = create_user(user_info)
            # Store user data in the session (optional)
            session["user"] = {
                "id": str(user["google_id"]),  # MongoDB document ID
                "email": user["email"],
                "token": credentials["token"]
            }
            # redirect to the user dashboard to get their settings 
            return redirect("http://localhost:3000/dashboard")

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

