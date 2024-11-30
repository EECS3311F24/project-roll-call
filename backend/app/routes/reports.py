from ..services.report_service.email_service import gmail_send_message
from . import report

# this is just a testing route as this task is automated 
@report.route("/send_self", methods=['GET'])
def send_self():
    gmail_send_message("saras.rollcall@gmail.com", "110125061098661425360")
    return "check inbox and logs"









   