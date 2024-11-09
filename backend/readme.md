# Flask Backend Initialization

## Overview
This repository contains the backend for a Flask application designed to help users manage their tasks, track progress, and gain insights into their productivity.

## Requirements
- Python 3.x
- Flask
- Additional dependencies specified in `requirements.txt`

## Getting Started


### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/EECS3311F24/project-roll-call/
cd backend/flask_app
```


### 2. Create and activate the virtual environment
```bash
python -m venv venv
```

On Windows:
```bash
venv\Scripts\activate
```

On MacOS/Linux:
```bash
source venv/bin/activate
```


### 3. Install dependencies
```bash
pip install -r requirements.txt
```


### 4. Start the Application
```bash
flask run
```
or 
```bash
python app.py
```

#### If flask not running in debug mode try:

    python -m flask --app app:app run --debug




# Running Google API

Make sure requirements are installed

    pip install -r requirements.txt

run quickstart in terminal (do not worry if imports are highlighted in red)

    python quickstart.py

- this should open a Google authorization window
- return the next 10 scheduled events
- you only have to sign in once, as a token will be created which will be used the next time.
- To sign into another account, delete the token.json

###  **To access the Google Project:**

- Go to: https://console.cloud.google.com/
- Sign in as: 
  - saras.rollcall@gmail.com
  - pass: eecs3311

To retrieve info from your own personal account you need to add your account as a test user: 
https://console.cloud.google.com/apis/credentials/consent?project=rollcall-440018







