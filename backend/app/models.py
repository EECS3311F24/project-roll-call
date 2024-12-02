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
        "e1": {"color": 11, "category": "Deadlines/Tests", "priority": "High Priority"},
        "e2": {"color": 4, "category": "None", "priority": "None"},
        "e3": {"color": 6, "category": "Appointments", "priority": "High Priority"},
        "e4": {"color": 5, "category": "None", "priority": "None"},
        "e5": {"color": 2, "category": "None", "priority": "None"},
        "e6": {"color": 10, "category": "Work", "priority": "Low Priority"},
        "e7": {"color": 9, "category": "Workouts", "priority": "Low Priority"},
        "e8": {"color": 1, "category": "Social Events", "priority": "Medium Priority"},
        "e9": {"color": 3, "category": "Unique Events", "priority": "Medium Priority"},
        "e10": {"color": 8, "category": "None", "priority": "None"},
        "e11": {"color": "-", "category": "Classes/Meetings", "priority": "Low Priority"},
        "notification": True,
        "notification_time": "08:00"
        })  
    creds = EmbeddedDocumentField(Creds)          

