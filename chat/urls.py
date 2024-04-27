from .routes import home
from . import app


app.add_url_rule("/", view_func=home)