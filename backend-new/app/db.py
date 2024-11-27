from pymongo import MongoClient
from mongoengine import connect
from flask import g  # Flask's request-scoped global
import os
from dotenv import load_dotenv

def get_db():
    """
    Provides a MongoDB connection for the app.
    """
    load_dotenv()
    if "db" not in g:
        client = MongoClient(os.getenv("MONGO_URI"))
        g.db = client["test"] 
    return g.db