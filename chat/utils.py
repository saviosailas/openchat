# Flask shell commands

from . import app
from . import db

@app.cli.command()
def create_database():
    db.create_all()