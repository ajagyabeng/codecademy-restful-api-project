from flask import Blueprint, request, render_template, redirect, url_for
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from ..form import SignupForm, LoginForm
from ..models import User

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    """Makes a post request to add a new user to the api."""
    form = SignupForm()
    if request.method == "POST" and form.validate_on_submit():
        data = request.form.to_dict()

        # SEND REQUEST TO API
        headers = {"Content-Type": "application/json"}
        body = {
            "username": data["username"],
            "password": data["password"],
            "email": data["email"]
        }
        res = requests.post("http://127.0.0.1:8080/api/users",
                            headers=headers, json=body)
        # print(res.json())
    return render_template("signup.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = request.form.to_dict()["email"]
        password = request.form.to_dict()["password"]

        headers = {"Content-Type": "application/json"}
        body = {
            "password": password,
            "email": email
        }
        res = requests.get("http://127.0.0.1:8080/api/users",
                           headers=headers, json=body)
        if res.status_code == 200:
            user = User.query.filter_by(email=email).first()
            login_user(user, remember=True)
            return redirect(url_for("views.home"))
        print(res.json())
    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    """login required decorator ensures that the logout function isnt accessed whiles not logged in"""
    logout_user()
    return redirect(url_for("auth.login"))
