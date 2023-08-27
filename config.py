import os
import pathlib

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


basedir = pathlib.Path(__file__).parent.resolve()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')

#DB_URL = 'postgresql://postgres:root@localhost:5432/postgres'
#app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)