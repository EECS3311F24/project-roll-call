import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret")
    CLIENT_SECRETS_FILE = os.getenv("CLIENT_SECRETS_FILE", "client_secret.json")

    SCOPES = [
        'https://www.googleapis.com/auth/calendar.readonly',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/userinfo.email',
    ]

    # SCOPES = [
    #     'https://www.googleapis.com/auth/drive.metadata.readonly',
    #     'https://www.googleapis.com/auth/calendar.readonly',
    #     'https://www.googleapis.com/auth/contacts.readonly',
    #     'https://www.googleapis.com/auth/userinfo.profile',
    #     'https://www.googleapis.com/auth/userinfo.email',
    # ]

    # SCOPES = [
    # 'https://www.googleapis.com/auth/userinfo.profile',
    # ]