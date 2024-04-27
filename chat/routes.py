from flask import render_template
from flask import request
from flask import make_response
from .models import User


def home():
    return render_template("login.html")

def login():
    if request.method == "GET":
        return render_template("login.html")
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return "Login"
    return render_template("login.html", error = "{} {}".format(username, password))