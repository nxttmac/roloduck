__author__ = 'pjo336'

from flask import render_template

from app import app


@app.route("/project", methods=['GET'])
def project_index():
    return render_template('project/create-project.html')