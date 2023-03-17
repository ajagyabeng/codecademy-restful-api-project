from flask import Blueprint, request, render_template
import requests

from ..form import SignupForm

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    """Makes a post request to add a new user to the api."""
    form = SignupForm()
    if request.method == "POST" and form.validate_on_submit():
        data = request.form.to_dict()
        headers = {"Content-Type": "application/json"}
        body = {
            "username": data["username"],
            "password": data["password"],
            "email": data["email"]
        }
        res = requests.post("http://127.0.0.1:8080/api/users",
                            headers=headers, json=body)
        # print(res.json())
    return render_template("index.html", form=form)
