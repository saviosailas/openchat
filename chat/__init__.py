from flask import Flask
from flask import request
from flask import redirect
from os import environ
from os import getcwd
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask("chat_app")

app.config["SECRET_KEY"] = environ.get("FLASK_SECRET")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(getcwd(), "database", "chat.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app=app)

migrate = Migrate(app=app, db=db)

@app.before_request
def force_https():
    if environ.get("FLASK_ENV") == "development":
        return
    if request.is_secure:
        return
    return redirect(request.url.replace("http://", "https://", 1), code=301)

from .urls import *

from .utils import *
