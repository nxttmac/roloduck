from flask import Flask, render_template, request, redirect
import os
from pymongo import MongoClient
import models.user.UserDao as UserDao

# Setup the app as a Flask application
app = Flask(__name__)

# Connect to our MongoDB roloduck database 
client = MongoClient()
db = client.roloduck
# Create our UserDao to connect to the user collection
user_dao = UserDao.UserDao(db)

# This will handle routes to our splash screen
@app.route("/index" ,methods=['GET'])
@app.route("/", methods=['GET'])
def roloduck_index():
    #user_dao.insert_user('Peter Johnston', 'pjohnston@roloduck.com')
    userlist = user_dao.find_users()
    return render_template('index.html', userlist = userlist)
    #return 'This is the index'
    
@app.route("/", methods=['POST'])
def insert_new_user():
    username = request.form.get("username")
    useremail = request.form.get("useremail")
    user_dao.insert_user(username, useremail)
    return redirect("/")

@app.route("/deleteUsers")
def delete_all_users():
    user_dao.delete_all_users()
    return redirect("/")

# Debug mode on
if __name__ == '__main__':
    app.debug = True
    app.run()