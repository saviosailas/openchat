from .routes import home
from .routes import login
from .routes import dashboard
from .routes import message
from .routes import get_message
from . import app


app.add_url_rule("/", view_func=home, methods=["GET", "POST"])
app.add_url_rule("/login", view_func=login, methods=["POST", "GET"])
app.add_url_rule("/dashboard", view_func=dashboard)
app.add_url_rule("/message", view_func=message, methods=["POST"])
app.add_url_rule("/getmessage", view_func=get_message)