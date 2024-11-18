import google.generativeai as genai

# this class creates a generator that calls google gemini
class Generator:

    # constructor
    def __init__(self):
        genai.configure(api_key = "AIzaSyBcmGr7e32c8U1lSPxMllIYiO-yQtgZNKI")
        self.model = genai.GenerativeModel("gemini-1.5-flash")
