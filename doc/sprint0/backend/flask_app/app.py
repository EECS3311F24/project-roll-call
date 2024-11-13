# Import necessary libraries and modules
from flask import Flask, jsonify, request
from flask_cors import CORS    
from pymongo import MongoClient

# Initialize a Flask app
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for the app, allowing other domains to access this app's resources
CORS(app)

client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB running on the localhost on port 27017 (default port)
db = client["appDB"]                                # Select or create (if it doesn't exist yet) the appDB database
users = db["users"]                                 # Select or create (if it doesn't exist yet) the users collection in the appDB database

# Define a route to handle GET requests for retrieving data
@app.route("/api/data", methods=['GET'])
def get_data():
    data = list(db.users.find())        # Retrieve all documents from the users collection in appDB and convert them to a list
    for item in data:
        item['_id'] = str(item['_id'])  # Convert the _id field of each document from an ObjectId to a string for JSON serialization
    return jsonify(data)                # Return the data as a JSON response

# Define a route to handle POST requests for adding new data
@app.route("/api/data", methods=['POST'])
def post_data():
    new_data = request.json                 # Get the JSON data sent in the request body
    db.users.insert_one(new_data)           # Insert the new document into the 'users' collection
    new_data['_id'] = str(new_data['_id'])  # Convert the _id field to a string for JSON serialization
    return jsonify(new_data), 201           # Return the newly added data with a 201 (Created) status

# Start the Flask app on the default port (5000) in debug mode
if __name__ == "__main__":
    app.run(debug = True)
