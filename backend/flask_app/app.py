from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from quickstart import *

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

# route for getting the upcoming events from today from Google Calendar api
@app.route("/day_events", methods=['GET'])
def get_day_events():
    events = get_day()
    return jsonify(events)

# route for getting the upcoming events within a week from Google Calendar api
@app.route("/week_events", methods=['GET'])
def get_week_events():
    events = get_week()
    return jsonify(events)

# route for getting the upcoming events within a week from Google Calendar api
@app.route("/month_events", methods=['GET'])
def get_month_events():
    events = get_month()
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug = True)
