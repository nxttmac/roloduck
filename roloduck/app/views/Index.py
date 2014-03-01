__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

# Import our database connection and application
from flask import render_template, request, redirect, session, url_for, flash

from app import app
from app.db import db
from app.db.UserDao import UserDao
from app.db.PartnerDao import PartnerDao
from app.db.ProjectDao import ProjectDao
from app.models.User import User
from app.models.User import COMPANY_TYPE_FREE, ROLE_ADMIN
from flask.ext.login import login_required, login_user

# Create our UserDao to connect to the user collection
user_dao = UserDao(db)
project_dao = ProjectDao(db)
partner_dao = PartnerDao(db)


@app.route("/index", methods=['GET'])
@app.route("/index.html", methods=['GET'])
@app.route("/", methods=['GET'])
def roloduck_index():
    """
    Route users who are not logged in to the index.
    If they are logged in, send them to the projects index
    """
    try:
        if session['logged_in'] is not None:
            return redirect('/projects')
        else:
            return render_template('index.html')
    except KeyError:
        return render_template('index.html')


@app.route("/signup", methods=['GET'])
def serve_signup_form():
    """
    Serve the signup form to the user
    """
    return render_template('signup.html')


@app.route("/signup", methods=['POST'])
def post_signup_form():
    """
    Post the signup form, register the user, and sign them in
    """
    # Retrieve the information from the form
    name = request.form.get('userName')
    email = request.form.get('userEmail')
    # Hash the password
    password = User.hide_user_password(request.form.get('userPassword'))
    company_name = request.form.get('companyName')
    # TODO hardcoded sub type
    company_subscription_type = COMPANY_TYPE_FREE
    # Create the company
    company = {'companyName': company_name, 'companySubscriptionType': company_subscription_type}
    # TODO hardcoded role to admin
    role = ROLE_ADMIN
    new_user = User(name, email, password, role, company)
    if new_user is not None:
        user_dao.insert_obj(new_user.get_user_map())
        hash = new_user.get_login_hash()
        session['logged_in'] = hash
        login_user(new_user)
        flash(u'Welcome to Roloduck!', 'success')
        return redirect('/')


@app.route("/adduser", methods=['GET'])
def serve_create_company_user():
    """
    Serve the page to add a new user to your team/client/company
    """
    try:
        user_hash = session['logged_in']
    except KeyError:
        return redirect(url_for('login_page.html'))
    user = user_dao.find_user_by_hash(user_hash)
    if user is not None:
        if user['role'] == 1:
            return render_template('create-user.html', currentUser=user)
    return redirect(url_for('login_page.html'))

@app.route("/wipe")
def wipe_db():
    user_dao.remove_all()
    partner_dao.remove_all()
    project_dao.remove_all()
    return redirect('/')
