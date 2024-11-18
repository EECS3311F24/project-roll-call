from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from calendar_api.day_event import DayEvent
from calendar_api.week_event import WeekEvent
from calendar_api.future_event import FutureEvent
from calendar_api.todo_event import SuggestedToDo
from gemini_api.word_gen import WordGen
from gemini_api.quote_gen import QuoteGen

app = Flask(__name__)

# enable CORS so that React can communicate with Flask
CORS(app)

# # set up MongoDB
# client = MongoClient("mongodb://localhost:27017/")
# db = client["appDB"]
# users = db["users"]

# # helper function to convert db document ID into a string
# def convert_id_to_string(doc):
#     doc['_id'] = str(doc['_id'])
#     return doc

# # route for getting data from db
# @app.route("/api/data", methods=['GET'])
# def get_data():
#     data = [convert_id_to_string(item) for item in users.find()]
#     return jsonify(data)

# # route for adding new data into the db
# @app.route("/api/data", methods=['POST'])
# def post_data():
#     new_data = request.json
#     users.insert_one(new_data)
#     return jsonify(convert_id_to_string(new_data)), 201

# creating necessary objects
day_event = DayEvent()
week_event = WeekEvent()
future_event = FutureEvent()
word_gen = WordGen()
quote_gen = QuoteGen()

# route for getting the events for today from Google Calendar API
@app.route("/day_events", methods=['GET'])
def get_day_events():
    events = day_event.get_events()
    events = day_event.categorize_events(events)
    return jsonify(events)

# route for getting the events for the next week from Google Calendar API
@app.route("/week_events", methods=['GET'])
def get_week_events():
    events = week_event.get_events()
    events = week_event.categorize_events(events)
    return jsonify(events)

# route for getting the events for this month from Google Calendar API
@app.route("/future_events", methods=['GET'])
def get_future_events():
    events = future_event.get_events()
    events = future_event.categorize_events(events)
    return jsonify(events)

# route for getting the events for the suggested To-Do List from Google Calendar API
@app.route("/to_do", methods=['GET'])
def get_to_do():
    events = SuggestedToDo().get_suggested_tasks()
    return jsonify(events)

@app.route("/generate_word", methods=['GET'])
def get_word():
    word = word_gen.get_word()
    return jsonify(word)

@app.route("/generate_quote", methods=['GET'])
def get_quote():
    quote = quote_gen.get_quote()
    return jsonify(quote)

if __name__ == "__main__":
    app.run(debug=True)
