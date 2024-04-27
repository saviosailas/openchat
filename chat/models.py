from . import db
from datetime import datetime

class User(db.Model):

    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    # messages = db.relationship("Messages", backref="sender", lazy="dynamic")

class Message(db.Model):

    __tablename__ = "message"

    message_id = db.Column(db.Integer, primary_key=True)
    message_text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    username = db.Column(db.String(30), db.ForeignKey("user.username"), nullable=False)
    from_admin = db.Column(db.Boolean, nullable=False, default=False)

    