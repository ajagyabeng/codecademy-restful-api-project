from flask_restful import Resource, marshal_with, fields, reqparse
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import find_dotenv, load_dotenv
from flask_cors import cross_origin
from flask_login import login_user, login_required, logout_user, current_user
import os
import datetime
import uuid

from ..common.models import User
from ..common.errors import UserErrors as UE
from ..common.errors import UserLogin as UL

# Locate .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

post_parser = reqparse.RequestParser()
post_parser.add_argument("username", type=str, help="Login Username")
post_parser.add_argument("password", type=str, help="Login Password")
post_parser.add_argument("email", type=str, help="Email")

# user_fields shows how the response will be rendered
user_fields = {
    "user": {
        "id": fields.Integer,
        "username": fields.String,
        "email": fields.String,
        "public_id": fields.String,
        "registered_on": fields.DateTime
    }
}


class UsersApi(Resource):
    @cross_origin()
    @marshal_with(user_fields)
    def get(self):
        """Gets all users."""
        users = User.query.all()
        return users, 200

    @marshal_with(user_fields)
    def post(self):
        """Adds a new user."""
        data = post_parser.parse_args()
        user = User.query.filter_by(email=data.email).first()
        if not user:
            new_user = User(
                username=data.username,
                password=generate_password_hash(
                    data.password, method=os.getenv("HASH_METHOD")),
                email=data.email,
                registered_on=datetime.datetime.utcnow(),
                public_id=str(uuid.uuid4())
            )
            new_user.insert()
            added_user = User.query.filter_by(email=data.email).first()
            return added_user, 201
        UE.abort_if_user_already_exists()


class UserApi(Resource):
    @cross_origin()
    @marshal_with(user_fields)
    def get(self, pk):
        """Gets a user with the specified ID."""
        user = User.query.get(pk)
        if not user:
            UE.abort_if_user_doesnt_exist(pk)
        return user, 200

    @marshal_with(user_fields)
    def put(self, pk):
        """Updates the username of a user with the specified ID."""
        data = post_parser.parse_args()
        user = User.query.get(pk)
        if not user:
            UE.abort_if_user_doesnt_exist(pk)
        user.username = data.username
        user.update()
        return user, 200


class UserLogin(Resource):
    @marshal_with(user_fields)
    def get(self):
        """Checks login credentials."""
        data = post_parser.parse_args()
        user = User.query.filter_by(email=data.email).first()
        if user:
            if check_password_hash(user.password, data.password):
                return user, 200
            UL.abort_if_wrong_password()
        UL.abort_if_login_user_doesnt_exist(data.email)
