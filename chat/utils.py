from . import app
from . import db

from flask import request

# Flask shell commands

@app.cli.command()
def create_database():
    db.create_all()

# helper functions

def user_loggedin():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    jwt_token = request.cookies.get("jwt_token")
    if username is None or password is None or jwt_token is None:
        return False
    else:
        return True