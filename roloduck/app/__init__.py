__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from flask import Flask
from flask.ext.login import LoginManager
from pymongo import MongoClient
from app.secretkey import secret_key


# Setup the app as a Flask application
app = Flask('RoloDuck')

# Connect to our MongoDB roloduck database
client = MongoClient()
db = client.roloduck

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"
app.secret_key = secret_key

from views import Contact
from views import Partner
from views import Project
from views import Index
from views import Login