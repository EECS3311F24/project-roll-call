import base64
from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from ..auth_service.token import get_creds_by_id
from ..user_service import get_email
from app.services.report_service.create_report import get_report_html

def gmail_send_message(recipient, google_id):
    """Create and send an HTML email message via Gmail API."""

    try:
        # Retrieve credentials with Gmail send scope
        creds = get_creds_by_id(google_id, ["https://www.googleapis.com/auth/gmail.send"])

        # Build the Gmail service
        service = build("gmail", "v1", credentials=creds)

        # Create the email message
        message = EmailMessage()
        users_email = get_email(google_id)

        # Generate the HTML report
        if recipient == users_email:
            report_html = get_report_html(google_id)  
        else:
            report_html = get_report_html(google_id, shared=True)  

        message.set_content("Your email client does not support HTML.")  # Add plain text fallback
        message.add_alternative(report_html, subtype="html")  # Add HTML content

        # Set email metadata
        message["To"] = recipient
        message["From"] = users_email
        message["Subject"] = "Roll Call Report"

        # Encode the email message for the Gmail API
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        # Create the Gmail API request payload
        create_message = {"raw": encoded_message}

        # Send the email using the Gmail API
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )

        print(f'Message Id: {send_message["id"]}')
        return send_message

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None
