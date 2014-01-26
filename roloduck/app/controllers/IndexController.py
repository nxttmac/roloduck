__author__ = 'pjo336'

from flask import render_template, request, redirect
# Import our database connection and application
from app import app, db
from app.models.user import UserDao


# Create our UserDao to connect to the user collection
user_dao = UserDao.UserDao(db)

# This will handle routes to our splash screen
@app.route("/index", methods=['GET'])
@app.route("/", methods=['GET'])
def roloduck_index():
    userlist = user_dao.find_users()
    return render_template('index.html', userlist=userlist)

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
