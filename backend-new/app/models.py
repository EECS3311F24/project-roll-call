from mongoengine import *

class User(Document):
    google_id = StringField(required=True, unique=True)  
    email = EmailField(required=True, unique=True)       
    f_name = StringField(required=True)                 
    l_name = StringField(required=True)                  
    pfp = URLField()                                     
    settings = DictField(default={})                     

