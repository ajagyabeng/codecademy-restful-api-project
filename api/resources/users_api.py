from flask_restful import Resource, marshal_with, fields, reqparse
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import find_dotenv, load_dotenv
import os

from ..models import User
from ..common.errors import UserErrors as UE

# Locate .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

post_parser = reqparse.RequestParser()
post_parser.add_argument("username", type=str, help="Login Username")
post_parser.add_argument("password", type=str, help="Login Password")

user_fields = {
    "user": {
        "id": fields.Integer,
        "username": fields.String
    }
}


class UsersApi(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users, 200

    @marshal_with(user_fields)
    def post(self):
        data = post_parser.parse_args()
        user = User(username=data.username, password=generate_password_hash(
            data.password, method=os.getenv("HASH_METHOD")))
        try:
            user.insert()
        except:
            UE.abort_if_user_wasnt_added()
        users = User.query.all()
        return users, 201


class UserApi(Resource):
    @marshal_with(user_fields)
    def get(self, pk):
        user = User.query.get(pk)
        if not user:
            UE.abort_if_user_doesnt_exist(pk)
        return user, 200

    @marshal_with(user_fields)
    def put(self, pk):
        data = post_parser.parse_args()
        user = User.query.get(pk)
        if not user:
            UE.abort_if_user_doesnt_exist(pk)
        user.username = data.username
        user.update()
        return user, 200
