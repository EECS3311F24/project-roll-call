import logging
import atexit
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from flask import current_app
from mongoengine import Document, StringField
from app.models import User
from app.services.report_service.email_service import gmail_send_message

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Scheduler job
def send_daily_email(app):
    """Send a daily email to all users."""
    with app.app_context():  # Use the app passed to this function
        users = User.objects()
        success_count = 0
        failure_count = 0

        for user in users:
            try:
                if user.settings.get('notification', False): 
                    if gmail_send_message(user.email, user.google_id):
                        success_count += 1
                    else:
                        failure_count += 1
            except Exception as e:
                logger.error(f"Failed to process user {user.email}: {e}")
                failure_count += 1

        logger.info(f"Daily email job completed: {success_count} successes, {failure_count} failures.")

# Initialize and schedule the job
scheduler = BackgroundScheduler()
def schedule_jobs(app):
    """Initialize and schedule jobs with the Flask app."""
    scheduler = BackgroundScheduler()

    # Add the email job
    scheduler.add_job(
        send_daily_email,  # Pass the function
        args=[app],        # Pass the app as an argument
        trigger=IntervalTrigger(minutes=4),  # For testing
        # trigger=CronTrigger(hour=10, minute=30),
        id="daily_email_job",
        replace_existing=True
    )

    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=False))
    logger.info("Scheduler started.")



