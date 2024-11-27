from ..services.report_service import gmail_send_message
from . import report

@report.route("/send_self", methods=['GET'])
def send_self():
    gmail_send_message()
    return "Hello"


   