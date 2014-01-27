__author__ = 'Peter Johnston'

# Import our database connection and application
from flask import render_template, request, redirect, session

from app import app, db
from app.models.user import UserDao, User
from flask.ext.login import login_required, login_user


# Create our UserDao to connect to the user collection
user_dao = UserDao.UserDao(db)

# This will handle routes to our splash screen
@app.route("/index", methods=['GET'])
@app.route("/index.html", methods=['GET'])
@app.route("/", methods=['GET'])
def roloduck_index():
    userlist = user_dao.find_users()
    return render_template('index.html', userlist=userlist)

# Welcome page after a user signs in
@app.route("/welcome", methods=['GET'])
@login_required
def welcome_page():
    user = user_dao.find_user_by_hash(session['username'])
    return render_template('welcome.html', user=user)

@app.route("/signup", methods=['Get'])
def serve_signup_form():
    return render_template('signup.html')

# For now this is attached to posting the form in the navbar, but its a basic
# mechanism to insert a user based off a form
@app.route("/signup", methods=['POST'])
def post_signup_form():
    name = request.form.get('username')
    email = request.form.get('useremail')
    password = request.form.get('userpassword')
    # TODO hardcoded role to admin
    role = 1
    new_user = User.User(name, email, password, role)
    login_user(new_user)
    session['username'] = email+password
    user_dao.insert_user(new_user)
    return redirect('/welcome')

