# **RollCall**

## Motivation

*Google Calendar is one of the most popular tools for staying organized and tracking deadlines, but have you ever found yourself surprised by tasks, even though they were on your schedule? That's because a calendar is only as useful as the effort you put into reviewing and deciphering it. RollCall takes that mental load off your plate by summarizing your day for you, so you can stay productive and on top of your tasks without constantly managing your schedule.*

**PROBLEM**

People with busy schedules (professionals, students, etc.) often struggle to stay organized, especially when managing multiple tasks and meetings. Traditional daily stand-ups or personal check-ins require manual effort, and there’s no easy, automated way to generate a summary of daily tasks and priorities from a calendar.

**WHY IT EXISTS?**

This is a problem because we either:
- Believe if we have it written down, it will get done
- Are too busy with our actual tasks that we don't have time to think about how to efficiently get them done

**SOLUTION**

RollCall will automatically generate a daily roll-call or stand-up report based on an individual's Google Calendar. The app will summarize meetings, tasks, and even suggest a personal TODO all without manual input.

**KEY FEATURES**
- 3 concise reports at varying temporal levels of personal events, tasks and responsibilities
    - Your day
    - Your week
    - Your future (1 month +)
- A personalized suggested TODO list which takes into consideration priority and urgency of your upcoming tasks

# Installation

### Technologies

#### Frontend:
- **React**: front-end JavaScript library
- **TypeScript**: JavaScript with static typing
- **Vite**: JavaScript package bundler

#### Backend:
- **Python**: high-level programming language
- **Flask**: web server framework for Python
- **MongoDB**: NoSQL document database platform

## Running on your Machine

```
git clone https://github.com/EECS3311F24/project-roll-call.git
```

### Frontend

1. Install node.js https://nodejs.org/en/download/prebuilt-installer

2. Install dependencies
```
cd frontend
npm install
```

3. Run Frontend
```
npm run dev
```

### Backend
1. Install python https://www.python.org/downloads

2. Create and activate the virtual environment
```
cd backend/flask_app
python -m venv venv
```

On Windows:
```
venv\Scripts\activate
```

On MacOS/Linux:
```
source venv/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set Up Your Own Environment Variables


5. Start the Server
```
flask run
```
or 
```
python app.py
```

### Backend (Database)
1. Install MongoDB https://www.mongodb.com/try/download/community?tck=docs_server (ensure MongoDB Compass installation is selected)

2. On MongoDB Compass (GUI) select "Add new connection", then ensure that under "URI" the following is shown: "mongodb://localhost:27017/" 

3. Click "Connect"

###  **To Run the App:**

- Sign in as: 
  - saras.rollcall@gmail.com
  - pass: eecs3311


# Contributions

Trello Board is used to create tickets which define work need to be completed.

Branches from main will be based on tickets.

We plan to implement pull requests which will be reviewed by the developer team when merging to main.
