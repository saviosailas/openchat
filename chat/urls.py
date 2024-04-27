from .routes import home
from .routes import login
from .routes import dashboard
from . import app


app.add_url_rule("/", view_func=home, methods=["GET", "POST"])
app.add_url_rule("/login", view_func=login, methods=["POST", "GET"])
app.add_url_rule("/dashboard", view_func=dashboard)