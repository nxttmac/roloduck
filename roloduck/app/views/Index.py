__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

# Import our database connection and application
from flask import render_template, request, redirect, session, url_for, flash

from app import app
from app.db import db
from app.db.UserDao import UserDao
from app.models.User import User
from app.models.User import COMPANY_TYPE_FREE, ROLE_ADMIN
from flask.ext.login import login_required, login_user


# Create our UserDao to connect to the user collection
user_dao = UserDao(db)

# This will handle routes to our splash screen
@app.route("/index", methods=['GET'])
@app.route("/index.html", methods=['GET'])
@app.route("/", methods=['GET'])
def roloduck_index():
    # No exception thrown for lists
    userlist = user_dao.find_all()
    try:
        if session['username'] is not None:
            return redirect('/projects')
        else:
            return render_template('index.html', userlist=userlist)
    except KeyError:
        return render_template('index.html', userlist=userlist)

# Welcome page after a user signs in
@app.route("/welcome", methods=['GET'])
@login_required
def welcome_page():
    user = user_dao.find_user_by_hash(session['username'])
    return render_template('welcome.html', user=user)

# Serve the signup form
@app.route("/signup", methods=['GET'])
def serve_signup_form():
    return render_template('signup.html')

# For now this is attached to posting the form in the navbar, but its a basic
# mechanism to insert a user based off a form
@app.route("/signup", methods=['POST'])
def post_signup_form():
    # Retrive the information from the form
    name = request.form.get('userName')
    email = request.form.get('userEmail')
    password = request.form.get('userPassword')
    companyName = request.form.get('companyName')
    # TODO hardcoded sub type
    companySubscriptionType = COMPANY_TYPE_FREE
    # Create the company
    company = {'companyName': companyName, 'companySubscriptionType': companySubscriptionType}
    # TODO hardcoded role to admin
    role = ROLE_ADMIN
    new_user = User(name, email, password, role, company)
    if new_user is not None:
        user_dao.insert_obj(new_user.get_user_map())
        login_user(new_user)
        session['username'] = email+password
        flash(u'Welcome to Roloduck!', 'success')
        return redirect('/')

# A page only to be shown for debugging purposes
# Will be updated to show current database content/state
@app.route("/db", methods=['GET'])
def serve_database_info():
    userlist = user_dao.find_users()
    return render_template('database-view.html', userlist=userlist)

# Serve the page to add a new user to your team/client/company
@app.route("/adduser", methods=['GET'])
def serve_create_company_user():
    user = user_dao.find_user_by_hash(session['username'])
    if user is not None:
        if user['role']== 1:
            return render_template('create-user.html', currentUser=user)
    return redirect(url_for('login_page.html'))