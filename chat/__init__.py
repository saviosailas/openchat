from flask import Flask
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


from .urls import *

from .utils import *
