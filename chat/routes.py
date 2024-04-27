from flask import render_template
from flask import request
from flask import make_response
from flask import redirect
from flask import url_for
from .models import User
from .models import Message
from .utils import user_loggedin
from .utils import valid_user
from random import randint
from . import db
from os import environ
from flask import jsonify


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
        return response
    return render_template("login.html", error = "Invalid username or password")

def dashboard():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    if user_loggedin() == False or valid_user() == False:
        response = make_response(redirect(url_for("home")))
        response.delete_cookie("username")
        response.delete_cookie("password")
        return response
    if username == environ.get("SYSTEM_ADMIN_USER"):
        users = User.query.all()
        return render_template("sysadmin.html", users=users)
    else:
        return render_template("dashboard.html", username=username, flash_message="", super_user=environ.get("SUPER_USER"))
    
def message():
    message = request.get_json().get("message")
    try:
        sender = User.query.filter_by(username=request.cookies.get("username")).first()
        if sender is None:
            return "failed", 409
        new_message = Message()
        new_message.message_text = message
        new_message.username = sender.username
        db.session.add(new_message)
        db.session.commit()

    except Exception as exp:
        print(exp)
        return "failed", 409
    print(f"message >> [{request.cookies.get('username')}]  {message}")
    return "OK"

def get_message():
    try:
        user = User.query.filter_by(username=request.cookies.get("username")).first()
        if user is None:
            return "invalid user", 403
        messages = Message.query.filter_by(username=user.username).order_by(Message.timestamp.desc()).limit(5).all()

        message_data = [
            {
                "msg": message.message_text,
                "fromAdmin": message.from_admin
            }
            for message in messages
        ]
        return jsonify(message_data)
    
    except Exception as exp:
        print(exp)
    return []