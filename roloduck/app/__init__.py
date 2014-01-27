__author__ = 'pjo336'

from flask import Flask
from flask.ext.login import LoginManager
from pymongo import MongoClient


# Setup the app as a Flask application
app = Flask('RoloDuck')

# Connect to our MongoDB roloduck database
client = MongoClient()
db = client.roloduck

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"
app.secret_key = '_`lVF)*H0b+$e Ge00?4sI]RDh:C6Dx!e._1}=-}@QSFiAMoK-4ocB#q:>L-K?q-'

from controllers import ProjectController
from controllers import IndexController
from controllers import Login