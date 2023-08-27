import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app
from routes import blueprint


app.register_blueprint(blueprint)
app.run(host = '0.0.0.0', port = 8080, debug = True)