__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from flask import render_template, url_for, redirect, flash, request
from app import app
from app.db import db
from flask.ext.login import session, login_required
from app.db.UserDao import UserDao
from app.db.ContactDao import ContactDao
from app.models.Contact import Contact

# Create our Daos to connect to the collections
user_dao = UserDao(db)
contact_dao = ContactDao(db)


# Serve the contact list page
@app.route("/contacts", methods=['GET'])
@login_required
def contact_index():
    user = user_dao.find_user_by_hash(session['logged_in'])
    contacts = contact_dao.find_all()
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return redirect(url_for('login_page.html'))
    else:
        return render_template('contact/contacts.html', user=user, contacts=contacts, page="contacts")


# Serve the create contact template
@app.route("/contact/create", methods=['GET'])
@login_required
def serve_contact_create_page():
    user = user_dao.find_user_by_hash(session['logged_in'])
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return redirect(url_for('login_page.html'))
    else:
        return render_template('contact/create.html', user=user, page="contacts")


# Create the actual contact based on the submitted form
@app.route("/contact/create", methods=['POST'])
@login_required
def post_contact_create_page():
    user = user_dao.find_user_by_hash(session['logged_in'])
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return render_template('index.html', user=user)
    else:
        contact_first_name = request.form.get('contactfirstname')
        contact_last_name = request.form.get('contactlastname')
        contact_role = request.form.get('contactrole')
        contact_title = request.form.get('contacttitle')
        contact_email = request.form.get('contactemail')
        contact_phone = request.form.get('contactphone')
        # Build the new contact using the info from our form
        # And the user that created it
        # TODO Use getters for company and id
        new_contact = Contact(contact_first_name, contact_last_name, contact_role, contact_title,
                                      contact_email, contact_phone, user.company, user.id)
        if new_contact is not None:
            contact_dao.insert_obj(new_contact.get_contact_map())
            flash(u'You have successfully added a new contact', 'success')
            return render_template('contact/contacts.html', contact=new_contact, page="contacts")

# Serve a page for an individual contact
@app.route("/contact/<contact_id>")
@login_required
def serve_individual_contact_page(contact_id):
    user = user_dao.find_user_by_hash(session['logged_in'])
    if user is None:
        flash(u'Please log in to see this page', 'warning')
        return render_template('index.html', user=user)
    else:
        # Find this contact in the database
        contact = contact_dao.find_contact_by_id(contact_id)
        return render_template('contact/single-contact.html', contact=contact, user=user, page="contacts")