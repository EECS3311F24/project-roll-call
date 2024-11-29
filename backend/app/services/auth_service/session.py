import requests
from flask import request, jsonify
from functools import wraps
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def user_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"message": "Token is missing!"}), 403

        token = token.split(" ")[1] if " " in token else token

        try:
            # Create Google Credentials object
            creds = Credentials(token=token)

            # Refresh the token if expired
            if creds.expired:
                creds.refresh(Request())

            # Use the token to get user info from Google's userinfo endpoint
            userinfo_response = requests.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {token}"}
            )
            
            if userinfo_response.status_code != 200:
                return jsonify({"message": "Invalid token!"}), 403

            userinfo = userinfo_response.json()
            email = userinfo.get("email")
            if not email:
                return jsonify({"message": "Unable to retrieve user email!"}), 403

            # Optionally, you can check the email in your database
            # user = User.objects(email=email).first()
            # if not user:
            #     return jsonify({"message": "Unauthorized user!"}), 403

        except Exception as e:
            return jsonify({"message": f"Invalid token: {e}"}), 403

        # Pass valid credentials to the wrapped function
        return f(creds=creds, *args, **kwargs)

    return wrapper