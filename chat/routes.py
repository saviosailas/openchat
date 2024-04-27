from flask import render_template
from flask import request
from flask import make_response
from flask import redirect
from flask import url_for
from .models import User
from .utils import user_loggedin
from random import randint
from . import db

_dummy_token = " "

def home():
    if user_loggedin():
        return redirect(url_for("dashboard"))
    if request.method == "GET":
        return render_template("signup.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        print(username, password)
        if username is None or username == "":
            return render_template("signup.html", error="User name cannot be empty!"), 409
        elif password is None or password == "":
            return render_template("signup.html", error="Password cannot be empty!"), 409
        elif User.query.filter_by(username=username).first():
            return render_template("signup.html", error="Try another user name ({}{})?".format(username, randint(1111, 9999))), 409
        try:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
        except Exception as exp:
            return render_template("signup.html", error="Something went wrong!"), 500
        response = make_response(redirect(url_for("dashboard")))
        response.set_cookie("username", username)
        response.set_cookie("password", password)
        response.set_cookie("jwt_token", _dummy_token)
        return response

def login():
    if request.method == "GET":
        if user_loggedin():
            return redirect(url_for("dashboard"))
        return render_template("login.html")
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        response = make_response(redirect(url_for("dashboard")))
        response.set_cookie("username", username)
        response.set_cookie("password", password)
        response.set_cookie("jwt_token", _dummy_token)
        return response
    return render_template("login.html", error = "Invalid username or password")

def dashboard():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    jwt_token = request.cookies.get("jwt_token")
    if user_loggedin() == False:
        print("failure")
        return redirect(url_for("home"))
    return render_template("dashboard.html", username=username, password=password, jwt_token=jwt_token)