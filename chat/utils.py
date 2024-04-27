from . import app
from . import db
from .models import User
from flask import request

# Flask shell commands

@app.cli.command()
def create_database():
    db.create_all()

# helper functions

def user_loggedin():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    if username is None or password is None:
        return False
    else:
        return True
    
def valid_user():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    if username is None or password is None:
        return False
    if username == "" or password == "":
        return False
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return True
    else:
        return False