from ..services.calendar_service.day_event import DayEvent
from ..services.calendar_service.week_event import WeekEvent
from ..services.calendar_service.future_event import FutureEvent
from ..services.calendar_service.todo_event import SuggestedToDo
from flask import jsonify, redirect, session, request
from . import cal


@cal.route('/test_permission')
def calendar_api_request():
    if 'credentials' not in session:
        return jsonify(session)

    features = session['features']

    if features['calendar']:
    # User authorized Calendar read permission.
    # Calling the APIs, etc.
        return ('<p>User granted the Google Calendar read permission. </p>')
    else:
    # User didn't authorize Calendar read permission.
    # Update UX and application accordingly
        return '<p>Calendar feature is not enabled.</p>'

# route for getting the events for today from Google Calendar API
@cal.route("/day_events", methods=['GET'])
def get_day_events():
    day_event = DayEvent()
    events = day_event.get_events()
    events = day_event.categorize_events(events)
    return jsonify(events)

# route for getting the events for the next week from Google Calendar API
@cal.route("/week_events", methods=['GET'])
def get_week_events():
    week_event = WeekEvent()
    events = week_event.get_events()
    events = week_event.categorize_events(events)
    return jsonify(events)

# route for getting the events for this month from Google Calendar API
@cal.route("/future_events", methods=['GET'])
def get_future_events():
    future_event = FutureEvent()
    events = future_event.get_events()
    events = future_event.categorize_events(events)
    return jsonify(events)

# route for getting the events for the suggested To-Do List from Google Calendar API
@cal.route("/to_do", methods=['GET'])
def get_to_do():
    events = SuggestedToDo().get_suggested_tasks()
    return jsonify(events)