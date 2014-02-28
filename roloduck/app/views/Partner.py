__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from flask import render_template, url_for, redirect, flash, request
from flask.ext.login import session, login_required
from app import app
from app.db import db
from app.db.UserDao import UserDao
from app.db.PartnerDao import PartnerDao
from app.db.ProjectDao import ProjectDao
from app.models.Partner import Partner

# Create our Daos to connect to the collections
user_dao = UserDao(db)
project_dao = ProjectDao(db)
partner_dao = PartnerDao(db)

# Serve the partner list page
@app.route("/partners", methods=['GET'])
@login_required
def partner_index():
    user = user_dao.find_user_by_hash(session['username'])
    partners = partner_dao.find_partners()
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return redirect(url_for('login_page.html'))
    else:
        return render_template('partner/partners.html', user=user, partners=partners,page="partners")

# Serve the create partner template
@app.route("/partner/create", methods=['GET'])
@login_required
def serve_partner_create_page():
    user = user_dao.find_user_by_hash(session['username'])
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return redirect(url_for('login_page.html'))
    else:
        return render_template('partner/create.html', user=user, page="partners")

# Create the actual partner based on the submitted form
@app.route("/partner/create", methods=['POST'])
@login_required
def post_partner_create_page():
    user = user_dao.find_user_by_hash(session['username'])
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return render_template('index.html', user=user)
    else:
        partner_name = request.form.get('partnername')
        partner_description = request.form.get('partnerdescription')
        # Build the new partner using the info from our form
        # And the user that created it
        # TODO Use getters for company and id
        new_partner = Partner(partner_name, partner_description, user.company, user.id)
        if new_partner is not None:
            partner_dao.insert_partner(new_partner)
            flash(u'You have successfully added a new partner', 'success')
            return redirect('/partners')