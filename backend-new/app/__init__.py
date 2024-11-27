from flask import Flask, session
from datetime import timedelta
from flask_cors import CORS
from dotenv import load_dotenv
import os


def create_app():
    """
    App factory function to create and configure the Flask application.
    """
    # Load environment variables from `.env` file
    load_dotenv()

    app = Flask(__name__)
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3000"}})
    app.secret_key = os.getenv("SECRET_KEY", "fallback_secret_key")
    app.permanent_session_lifetime = timedelta(days=7)

    print(f"App initialized with secret key: {app.secret_key}") 


    # Register Blueprints
    from app.routes.auth import auth
    app.register_blueprint(auth, url_prefix="/auth")

    from app.routes.calendar import cal
    app.register_blueprint(cal, url_prefix="/cal")

    from app.routes.gemini import gem
    app.register_blueprint(gem, url_prefix="/gem")

    # @app.before_request
    # def log_secret_key():
    #     print(f"Secret key for this request: {app.secret_key}") 


    return app