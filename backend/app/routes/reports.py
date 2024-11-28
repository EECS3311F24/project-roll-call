from ..services.report_service import gmail_send_message
from . import report
from flask import session


@report.route("/send_self", methods=['GET'])
def send_self():
    user_email = session.get("user", {}).get("email")
    gmail_send_message(user_email)
    return "check inbox and logs"

@report.route("/send_other/<other_email>", methods=['GET'])
def send_other(other_email):
    gmail_send_message(other_email)
    return f"Check {other_email}'s inbox and logs"




   