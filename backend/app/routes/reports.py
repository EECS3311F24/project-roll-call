from ..services.report_service import gmail_send_message, create_report
from . import report
from flask import session
from flask import request, jsonify
import requests



@report.route("/send_self", methods=['GET'])
def send_self():
    user_email = session.get("user", {}).get("email")
    gmail_send_message(user_email)
    return "check inbox and logs"

@report.route("/send_other/<other_email>", methods=['GET'])
def send_other(other_email):
    gmail_send_message(other_email)
    return f"Check {other_email}'s inbox and logs"

@report.route("/test", methods=['POST'])
def test():
    # Get the Bearer token from the Authorization header
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token is missing!"}), 403

    # Remove "Bearer " prefix if present
    token = token.split(" ")[1] if " " in token else token

    # Call create_report with the token
    return create_report(token)







   