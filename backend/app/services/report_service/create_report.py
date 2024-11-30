from datetime import datetime
from app.routes.calendar import get_day_events, get_week_events, get_future_events, get_to_do
from app.services.user_service import get_name

def get_report_html(google_id, shared=False):
    """Generate the HTML report."""
    today = get_today_html(google_id)
    week = get_week_html(google_id)
    future = get_future_html(google_id)
    todo = get_todo_html(google_id)
    name = get_name(google_id)

    if shared:
        greeting = f"Hello, {name} shared their Roll Call with you!"
        footer = f"Get your own! http://localhost:3000/"
    else:
        greeting = f"Hello {name}, here is your Roll Call!"
        footer = f"Good luck, see you tomorrow!"


    s = f"""
    <html>
        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0;">
            <h1 style="text-align: center;">{greeting}</h1>
            <table style="width: 100%; max-width: 1200px; margin: 0 auto; border-collapse: collapse;">
                <tr>
                    <td style="border: 1px solid #ccc; padding: 15px; vertical-align: top; width: 25%;">
                        <div>{today}</div>
                    </td>
                    <td style="border: 1px solid #ccc; padding: 15px; vertical-align: top; width: 25%;">
                        <div>{week}</div>
                    </td>
                    <td style="border: 1px solid #ccc; padding: 15px; vertical-align: top; width: 25%;">
                        <div>{future}</div>
                    </td>
                    <td style="border: 1px solid #ccc; padding: 15px; vertical-align: top; width: 25%;">
                        <div>{todo}</div>
                    </td>
                </tr>
            </table>
            <h2 style="text-align: center;">{footer}</h2>
        </body>
    </html>
    """
    return s.strip()


def get_today_html(google_id):
    """Get today's schedule in HTML format, sorted by period and time."""
    response = get_day_events(google_id)
    if response.status_code == 200:
        data = response.json  # Extract the JSON payload

        # Sort the periods (morning, afternoon, evening) and events by time
        sorted_data = {}
        for period in ["morning", "afternoon", "evening"]:
            events = data.get(period, [])
            sorted_events = sorted(events, key=lambda e: e["start"]["dateTime"])
            sorted_data[period] = sorted_events

        return format_day_html(sorted_data)  # Pass the sorted data to the formatting function
    else:
        print(f"Failed to retrieve events. Status Code: {response.status_code}")
        return "<p>Failed to retrieve today's events.</p>"


def get_week_html(google_id):
    """Get the week schedule in HTML format."""
    response = get_week_events(google_id)
    if response.status_code == 200:
        data = response.json  # Extract the JSON payload
        return format_week_html(data)  # Return as HTML
    else:
        print(f"Failed to retrieve events. Status Code: {response.status_code}")
        return "<p>Failed to retrieve this week's events.</p>"


def get_future_html(google_id):
    """Get future events in HTML format."""
    response = get_future_events(google_id)
    if response.status_code == 200:
        data = response.json  # Extract the JSON payload
        return format_future_html(data)  # Return as HTML
    else:
        print(f"Failed to retrieve events. Status Code: {response.status_code}")
        return "<p>Failed to retrieve future events.</p>"


def get_todo_html(google_id):
    """Get to-do list in HTML format."""
    response = get_to_do(google_id)
    if response.status_code == 200:
        data = response.json  # Extract the JSON payload
        return format_todo_html(data)  # Return as HTML
    else:
        print(f"Failed to retrieve events. Status Code: {response.status_code}")
        return "<p>Failed to retrieve the to-do list.</p>"


def format_day_html(data):
    """Format and return the schedule as HTML in the order: Morning, Afternoon, Evening."""
    schedule = "<h2>Up on the Agenda Today</h2>"
    periods = ["morning", "afternoon", "evening"]  # Define the desired order

    for period in periods:
        events = data.get(period, [])  # Retrieve events for the period, default to an empty list
        if events:
            schedule += f"<p><strong>{period.capitalize()}</strong></p><ul>"
            # Sort events by time within the period
            sorted_events = sorted(events, key=lambda e: e["start"]["dateTime"])
            for event in sorted_events:
                time = format_time(event["start"]["dateTime"])
                schedule += f"<li>{time} - {event['summary']}</li>"
            schedule += "</ul>"

    return schedule


def format_week_html(data):
    """Format the week's schedule as HTML."""
    output = "<h2>Upcoming This Week</h2>"
    for day_entry in data:
        day = day_entry["day"]
        events = day_entry["events"]
        output += f"<p><strong>{day}</strong></p><ul>"
        for event in events:
            start = event["start"]
            summary = event["summary"]
            if "date" in start:
                time_str = "All Day"
            else:
                time_str = datetime.fromisoformat(start["dateTime"]).strftime("%I:%M %p").lstrip("0")
            output += f"<li>{time_str}: {summary}</li>"
        output += "</ul>"
    return output


def format_future_html(data):
    """Format the future events as HTML."""
    output = "<h2>Future at a Glance</h2>"
    for category in data:
        category_type = category["type"]
        events = category["events"]
        output += f"<p><strong>{category_type}</strong></p><ul>"
        for event in events:
            day = event["day"]
            summary = event["summary"]
            output += f"<li>{day}: {summary}</li>"
        output += "</ul>"
    return output


def format_todo_html(events_data):
    """Format the to-do list as HTML."""
    output = "<h2>Suggested To-Do</h2><ul>"
    for event in events_data:
        summary = event.get("summary", "No Summary")
        output += f"<li> {summary}</li>"
    output += "</ul>"
    return output

# Define format_time if not already defined elsewhere
def format_time(date_time_str):
    """Convert ISO 8601 to a readable time format."""
    dt = datetime.fromisoformat(date_time_str)
    return dt.strftime("%I:%M %p").lstrip("0")  # Format as 12-hour clock, strip leading zero

# Other functions, including format_day_html
def format_day_html(data):
    """Format and return the schedule as HTML."""
    schedule = "<h2>Up on the Agenda Today</h2>"
    for period, events in data.items():
        if events:
            schedule += f"<p><strong>{period.capitalize()}</strong></p><ul>"
            for event in events:
                time = format_time(event["start"]["dateTime"])
                schedule += f"<li>{time} - {event['summary']}</li>"
            schedule += "</ul>"
    return schedule
