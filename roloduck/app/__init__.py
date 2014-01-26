__author__ = 'pjo336'

from flask import Flask
from pymongo import MongoClient


# Setup the app as a Flask application
app = Flask('RoloDuck')

# Connect to our MongoDB roloduck database
client = MongoClient()
db = client.roloduck

from controllers import ProjectController
from controllers import IndexController