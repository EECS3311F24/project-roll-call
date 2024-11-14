import google.generativeai as genai
import os

# this class creates a generator that calls google gemini
class Generator:

    # constructor
    def __init__(self):
        genai.configure(api_key="AIzaSyD2knqjGupxgTSOoi7unDQQxr1KmTpdPzc")
        self.model = genai.GenerativeModel("gemini-1.5-flash")
