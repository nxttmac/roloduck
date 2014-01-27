__author__ = 'pjo336'

from flask import render_template, url_for, redirect
from app import app, db
from flask.ext.login import session, login_required
from app.models.user import UserDao

# Create our UserDao to connect to the user collection
user_dao = UserDao.UserDao(db)

@app.route("/project", methods=['GET'])
@login_required
def project_index():
    user = user_dao.find_user_by_hash(session['username'])
    if user is None:
        return redirect(url_for('login_page.html'))
    else:
        return render_template('project/create-project.html')