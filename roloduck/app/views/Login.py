__author__ = 'Peter Johnston'

from flask import render_template, redirect, request, session
from flask.ext.login import logout_user, login_user, login_required
from app import app, db, login_manager
from app.models.user import UserDao
#import hashlib

# Create our user_dao
user_dao = UserDao.UserDao(db)

@app.route("/login", methods=['GET'])
def login_page_get():
    return render_template('login-page.html')

@app.route("/login", methods=['POST'])
def login_page_post():
    email = request.form['useremail']
    password = request.form['userpassword']
    hash_formula = email + password
    user = user_dao.find_user_by_hash(hash_formula)
    if user is None:
        return redirect('/login')
    login_user(user)
    # Create the user name for the session based on our hash sequence
    #sha = hashlib.sha1(email + password)
    session['username'] = hash_formula
    return redirect('/welcome')

# Create user loader function
@login_manager.user_loader
def load_user(userid):
    if session['username'] is not None:
        user = user_dao.find_user_by_hash(session['username'])
        if user is not None:
            return user

@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop('username', None)
    return redirect('/')