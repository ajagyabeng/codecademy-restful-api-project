from flask import Flask
from flask_cors import CORS

from dotenv import find_dotenv, load_dotenv
import os

from .models import setup_db


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


def create_app():
    """Creates and initialize app with modules"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
    CORS(app)
    setup_db(app)

    return app
