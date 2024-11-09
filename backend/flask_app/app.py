from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from calendar_api.day_event import DayEvent
from calendar_api.week_event import WeekEvent
from calendar_api.month_event import MonthEvent


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
@app.route("/month_events", methods=['GET'])
def get_month_events():
    print("Entering /month_events route...")  # Debug route entry
    events = MonthEvent().get_events()
    return jsonify(events)

# --------------------------------------------------------------------------
@app.route("/future_events", methods=['GET'])
def get_future_events():
    print("Entering /future_events route...")  # Debug route entry

    # Get the current time
    now = dt.datetime.now().isoformat()

    # Create a MonthEvent instance
    month_event = MonthEvent()

    # Filter events to only include future events
    def filter_future_events(events):
        return [
            event for event in events
            if event.get("start", {}).get("dateTime", "") > now
        ]

    # Apply the future filter
    future_events = month_event.get_events(filter_function=filter_future_events)

    return jsonify(future_events)

if __name__ == "__main__":
    # python -m flask --app app:app run --debug
    app.run(debug=True)
