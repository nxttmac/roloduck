__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from pymongo import MongoClient

# Connect to our MongoDB roloduck database
client = MongoClient()
db = client.roloduck