from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from calendar_api.day_event import DayEvent
from calendar_api.week_event import WeekEvent
from calendar_api.future_event import FutureEvent
from calendar_api.todo_event import SuggestedToDo


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

# route for getting the events for today from Google Calendar API
@app.route("/day_events", methods=['GET'])
def get_day_events():
    events = DayEvent().get_events()
    return jsonify(events)

# route for getting the events for the next week from Google Calendar API
@app.route("/week_events", methods=['GET'])
def get_week_events():
    events = WeekEvent().get_events()
    return jsonify(events)

# route for getting the events for this month from Google Calendar API
@app.route("/future_events", methods=['GET'])
def get_future_events():
    events = FutureEvent().get_events()
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug=True)

# route for getting the events for the suggested To-Do List from Google Calendar API
@app.route("/to_do", methods=['GET'])
def get_to_do():
    events = SuggestedToDo().get_suggested_tasks()
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug=True)
