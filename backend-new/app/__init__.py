from flask import Flask
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
    app.secret_key = os.getenv("SECRET_KEY", "fallback_secret_key")

    CORS(app)

    # Register Blueprints
    from app.routes.auth import auth
    app.register_blueprint(auth, url_prefix="/auth")


    return app