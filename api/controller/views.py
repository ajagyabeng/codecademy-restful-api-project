from flask import Blueprint, render_template, abort, jsonify, request, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/api")
@login_required
def home():
    return render_template("index.html", user=current_user)
