__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from flask import render_template, redirect, request, session, flash
from flask.ext.login import logout_user, login_user, login_required
from app import app, login_manager
from app.db import db
from app.db.UserDao import UserDao
#import hashlib

# Create our user_dao
user_dao = UserDao(db)

@app.route("/login", methods=['GET'])
def login_page_get():
    return render_template('login-page.html')

@app.route("/login", methods=['POST'])
def login_page_post():
    email = request.form['useremail']
    password = request.form['userpassword']
    hash_formula = email + password
    user = user_dao.find_user_by_hash(hash_formula)
    # Login was not successful
    if user is None:
        flash(u'Invalid login!  Please try again.', 'danger')
        return redirect('/login')
    # Login was successful so officially log the user is and add their hash to the session
    login_user(user)
    #sha = hashlib.sha1(email + password)
    session['username'] = hash_formula
    flash(u'Welcome back, %s.' % user.name, 'success')
    return redirect('/')

# Create user loader function
@login_manager.user_loader
def load_user(userid):
    if session['username'] is not None:
        user = user_dao.find_user_by_hash(session['username'])
        if user is not None:
            return user

@app.route("/logout")
#@login_required
def logout():
    logout_user()
    session.pop('username', None)
    return redirect('/')