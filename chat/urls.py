from .routes import home
from .routes import login
from . import app


app.add_url_rule("/", view_func=home)
app.add_url_rule("/login", view_func=login, methods=["POST", "GET"])