from flask import Flask
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

from dotenv import find_dotenv, load_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
csrf = CSRFProtect()


def create_app():
    """Creates and initialize app with modules"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
    # csrf.init_app(app)

    # import and register blueprints
    from .controller.auth import auth
    from .controller.views import views
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    from .common.models import setup_db, User

    # initialize aa with database to create tables and also track migrations,
    setup_db(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """tells a flask app how to load a user"""
        return User.query.get(int(id))

    return app
