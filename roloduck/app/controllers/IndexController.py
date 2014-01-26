__author__ = 'pjo336'

# Import our database connection and application
from flask import render_template, request, redirect

from app import app, db
from app.models.user import UserDao, User
from flask.ext.login import login_required


# Create our UserDao to connect to the user collection
user_dao = UserDao.UserDao(db)

# This will handle routes to our splash screen
@app.route("/index", methods=['GET'])
@app.route("/", methods=['GET'])
def roloduck_index():
    userlist = user_dao.find_users()
    return render_template('index.html', userlist=userlist)

# For now this is attached to posting the form in the navbar, but its a basic
# mechanism to insert a user based off a form
@app.route("/", methods=['POST'])
def insert_new_user():
    # TODO Take out this hard coding when names are added into the forms
    fname = 'herp'
    lname = 'derp'
    useremail = request.form.get("useremail")
    new_user = {'firstname': fname, 'lastname': lname, 'useremail': useremail}
    user_dao.insert_user(new_user)
    return redirect("/")

