__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from flask import render_template, url_for, redirect, flash, request
from flask.ext.login import session, login_required
from app import app
from app.db import db
from app.db.UserDao import UserDao
from app.db.ProjectDao import ProjectDao
from app.models import Project

# Create our Daos to connect to the collections
user_dao = UserDao(db)
project_dao = ProjectDao(db)

# Serve the project list page
@app.route("/projects", methods=['GET'])
@login_required
def project_index():
    user = user_dao.find_user_by_hash(session['logged_in'])
    projects = project_dao.find_all()
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return redirect(url_for('login_page.html'))
    else:
        return render_template('project/projects.html', user=user, projects=projects, page="projects")

# Serve the create project template
@app.route("/project/create", methods=['GET'])
@login_required
def serve_project_create_page():
    user = user_dao.find_user_by_hash(session['logged_in'])
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return redirect(url_for('login_page.html'))
    else:
        return render_template('project/create.html', user=user, page="projects")

# Create the actual project based on the submitted form
@app.route("/project/create", methods=['POST'])
@login_required
def post_project_create_page():
    user = user_dao.find_user_by_hash(session['logged_in'])
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return render_template('index.html', user=user)
    else:
        project_name = request.form.get('projectname')
        project_description = request.form.get('projectdescription')
        # Build the new project using the info from our form
        # And the user that created it
        # TODO Use getters for company and id
        new_project = Project.Project(project_name, project_description, user.company, user.id)
        if new_project is not None:
            project_dao.insert_obj(new_project.get_project_map())
            flash(u'You have successfully added a new project', 'success')
            return render_template('project/single-project.html', user=user, project=new_project, page="projects")

# Serve a page for an individual project
@app.route("/project/<project_id>")
@login_required
def serve_individual_project_page(project_id):
    user = user_dao.find_user_by_hash(session['logged_in'])
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return render_template('index.html', user=user)
    else:    
        # Find this project in the database
        project = project_dao.find_project_by_id(project_id)
        return render_template('project/single-project.html', project=project, user=user, page="projects")
        