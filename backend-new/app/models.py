from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, URLField, ListField, EmailField, DictField


class Creds(EmbeddedDocument):
    token = StringField(required=True) 
    refresh_token = StringField() 
    token_uri = URLField(required=True) 
    client_id = StringField(required=True) 
    client_secret = StringField(required=True) 
    scopes = ListField(URLField(), required=True)        


class User(Document):
    google_id = StringField(required=True, unique=True)  
    email = EmailField(required=True, unique=True)       
    f_name = StringField(required=True)                 
    l_name = StringField(required=True)                  
    pfp = URLField() 
    settings = DictField(default={})  
    creds = EmbeddedDocumentField(Creds)          

