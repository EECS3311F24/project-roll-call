from flask import redirect, session, request, url_for, jsonify
from ..services.auth_service.google_auth import initiate_google_auth, handle_oauth_callback
from app.services.auth_service.token import save_session, decode_google_id_token
from app.services.user_service import create_user, get_user, user_in_db, store_creds
from . import auth


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
    # creates a new session every time a user logs i
    # This is important because for the schedule report email we need to keep the 
    # session alive (it expires after 31)
    session.clear()
    return redirect(initiate_google_auth("auth.callback"))
@auth.route("/callback")
def callback():
    try:
        redirect_uri = url_for("auth.callback", _external=True)
        credentials_dict = handle_oauth_callback(request.url, redirect_uri)
        user_info = decode_google_id_token(credentials_dict["id_token"])

        # store the user in the session
        session["user"] = {
            "id": user_info["google_id"], 
            "email": user_info["email"],
        }
        session.permanent = True
        save_session()  # saves to json just for debugging

        # User already exists !
        if user_in_db(user_info["google_id"]): 
            user = get_user(user_info["google_id"])
            store_creds(user, credentials_dict)  # update creds on login
            # redirect to main page
            return redirect("http://localhost:3000/today")
        
        # new user !
        else:
            user = create_user(user_info) 
            store_creds(user, credentials_dict)  # store creds on signup
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

@auth.route('/get_session')
def get_session():
    print(session)
    return "Check logs for session cookie."

@auth.route("/test")
def test():
    return "Auth Blueprint is working!"


