from flask import Flask
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

from dotenv import find_dotenv, load_dotenv
import os

from .models import setup_db


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
csrf = CSRFProtect()


def create_app():
    """Creates and initialize app with modules"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
    # CORS(app)
    # csrf.init_app(app)

    from .controller.auth import auth
    app.register_blueprint(auth, url_prefix="/")

    setup_db(app)

    return app
