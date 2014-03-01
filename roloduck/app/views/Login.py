__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from flask import render_template, redirect, request, session, flash
from flask.ext.login import logout_user, login_user, login_required
from app import app, login_manager
from app.db import db
from app.db.UserDao import UserDao
from app.models.User import User

# Create our user_dao
user_dao = UserDao(db)


@app.route("/login", methods=['GET'])
def login_page_get():
    return render_template('login-page.html')


@app.route("/login", methods=['POST'])
def login_page_post():
    email = request.form['useremail']
    password = User.hide_user_password(request.form['userpassword'])
    user = user_dao.find_user_by_email(email)
    # Login was not successful
    if user is None or user['password'] != password:
        flash(u'Invalid login!  Please try again.', 'danger')
        return redirect('/login')
    # Login was successful so officially log the user is and add their hash to the session
    session['logged_in'] = user['login_hash']
    # TODO make sure this is safe, we dont want to create a diff User object
    # and log it in instead of the original user
    user_obj = User(user['name'], user['email'], user['password'],
                    user['role'], user['company'], user['login_hash'])
    login_user(user_obj)
    flash(u'Welcome back, %s.' % user_obj.name, 'success')
    return redirect('/')


# Create user loader function
@login_manager.user_loader
def load_user(userid):
    if session['logged_in'] is not None:
        user = user_dao.find_user_by_hash(session['logged_in'])
        if user is not None:
            user_obj = User(user['name'], user['email'], user['password'],
                            user['role'], user['company'], user['login_hash'])
            return user_obj


@app.route("/logout")
#@login_required
def logout():
    logout_user()
    session.pop('logged_in', None)
    return redirect('/')