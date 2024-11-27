from flask import redirect, session, request, url_for, jsonify
from app.services.auth_service import initiate_google_auth, handle_oauth_callback, decode_google_id_token
from app.utils.common import credentials_to_dict, serialize_document, save_session
from app.services.user_service import create_user, get_user, user_in_db, store_creds
import json
import google.oauth2.credentials
import google_auth_oauthlib.flow
from . import auth
import requests
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
        credentials_dict, id_token = handle_oauth_callback(request.url, redirect_uri)
        user_info = decode_google_id_token(id_token)

        # store the user in the session
        session["user"] = {
            "id": user_info["google_id"], 
            "email": user_info["email"],
        }
        save_session()  # just for debugging

        # User already exists !
        if user_in_db(user_info["google_id"]): 
            # redirect to main page
            return redirect("http://localhost:3000/today")
        
        # new user !
        else:
            user = create_user(user_info) 
            store_creds(user, credentials_dict)
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



# @auth.route('/revoke')
# def revoke():
#     if 'credentials' not in session:
#         return ('You need to <a href="/authorize">authorize</a> before ' 
#                 +'testing the code to revoke credentials.')
    
#     credentials = session['credentials']
#     token = credentials["token"]
    
#     revoke = requests.post('https://oauth2.googleapis.com/revoke',
#         params={'token': token},
#         headers = {'content-type': 'application/x-www-form-urlencoded'})

#     status_code = getattr(revoke, 'status_code')
#     return(status_code)


### TESTING ROUTES ----------------------------------------------------------------

@auth.route('/debug_session_cookie')
def debug_session_cookie():
    print(f"Session cookie: {request.cookies.get('session')}")
    return "Check logs for session cookie."

@auth.route("/test")
def test():
    return "Auth Blueprint is working!"


