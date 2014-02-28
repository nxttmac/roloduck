__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

import time


class Partner():
    """
    This class represents a Partner object which holds a list of connected Contacts
    """

    def __init__(self, partner_name, partner_description, client_id, created_by_user, contacts=None):
        self.partner_name = partner_name
        self.partner_description = partner_description
        # Pass in the linked client id
        self.client_id = client_id
        # Store who created this Project
        self.created_by_user = created_by_user
        self.date_created = time.strftime("%c")
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts

    def add_contact_to_container(self, contact):
        """
        Add an contact to the contacts list
        """
        self.contacts.append(contact)

    def get_id(self):
        """
        Return the current Partners id
        """
        return unicode(self.id)

    def get_date_created(self):
        """
        Return the date the current Partner was created
        """
        return self.date_created

    def get_partner_map(self):
        """
        Return a JSON version of the current Partner. Used to store in a database
        Note: Anytime we add or remove a field from the Partner class, if we want the
        change reflected in the database, we'll have to change it here as well
        """
        return {'partner_name': self.partner_name,
                'partner_description': self.partner_description,
                'client_id': self.client_id,
                'created_by_user': self.created_by_user,
                'date_created': self.date_created,
                'contacts': self.contacts
                }