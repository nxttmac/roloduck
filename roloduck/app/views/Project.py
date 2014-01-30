__author__ = 'Peter Johnston'

from flask import render_template, url_for, redirect
from app import app, db
from flask.ext.login import session, login_required
from app.models.user import UserDao

# Create our UserDao to connect to the user collection
user_dao = UserDao.UserDao(db)

# Serve the project list page
@app.route("/project", methods=['GET'])
@login_required
def project_index():
    user = user_dao.find_user_by_hash(session['username'])
    if user is None:
        return redirect(url_for('login_page.html'))
    else:
        return render_template('project/projects-list.html')

# Serve the create project template
@app.route("/project/create", methods=['GET'])
@login_required
def serve_project_create_page():
    return render_template('project/create-project.html')

# Serve a page for an individual project
#@app.route("/project/project-<projectId>")
#@login_required
#def serve_individual_project_page(projectId):
    # Find this project in the database
