from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, URLField, ListField, EmailField, DictField
from datetime import time

class Creds(EmbeddedDocument):
    token = StringField(required=True) 
    refresh_token = StringField(required=True) 
    token_uri = URLField(required=True) 
    id_token = StringField(required=True) 
    client_id=StringField(required=True) 
    client_secret=StringField(required=True) 
    scopes = ListField(URLField(), required=True)        

class User(Document):
    google_id = StringField(required=True, unique=True)  
    email = EmailField(required=True, unique=True)       
    f_name = StringField(required=True)                 
    l_name = StringField(required=True)                  
    pfp = URLField() 
    settings = DictField(default={
        "greeting": "word", 
        "future_weeks": 4, 
        "organize_by": "category",
        "e1": {"color": 11, "category": "Deadlines/Tests", "priority": "high"},
        "e2": {"color": 4, "category": "", "priority": ""},
        "e3": {"color": 6, "category": "Appointments", "priority": "high"},
        "e4": {"color": 5, "category": "", "priority": ""},
        "e5": {"color": 2, "category": "", "priority": ""},
        "e6": {"color": 10, "category": "Work", "priority": "low"},
        "e7": {"color": 9, "category": "Workouts", "priority": "low"},
        "e8": {"color": 1, "category": "Social Events", "priority": "medium"},
        "e9": {"color": 3, "category": "Unique Events", "priority": "medium"},
        "e10": {"color": 8, "category": "", "priority": ""},
        "e11": {"color": "-", "category": "Classes/Meetings", "priority": "low"},
        "notification": True,
        "notification_time": "08:00"
        })  
    creds = EmbeddedDocumentField(Creds)          

